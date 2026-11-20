#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
session_recorder.py — Quay Phim MP4 & Chụp Ảnh Ngầm Thao Tác Trình Duyệt (0 Cướp Focus / 0 Cướp Chuột)
Dành cho toàn bộ 14 Team Antigravity × Antigravity Omni-Browser Bridge (:8766).

Tính năng:
  - Chụp liên tục đúng nội dung Tab AI đang thao tác bằng Silent CDP (`Page.captureScreenshot`, JPEG nhẹ, focus=false)
    ngay cả khi cửa sổ Chrome nằm chìm hoàn toàn phía sau cửa sổ người dùng đang làm việc.
  - Tự động ghép chuỗi frame thành file `.mp4` chuẩn H.264 (`yuv420p`) bằng FFmpeg + lưu 1 ảnh snapshot cuối để QA đọc.
  - Hỗ trợ `send-back` (đưa cửa sổ Chrome đang bị Minimize về trạng thái nền không focus `SW_SHOWNOACTIVATE + HWND_BOTTOM`
    để Windows giữ GPU surface sống 100% mà KHÔNG làm phiền màn hình người dùng).

Cách dùng:
  python session_recorder.py reload -p "thanhdientraining"
  python session_recorder.py send-back --title "Chrome"
  python session_recorder.py start  -p "thanhdientraining" -o "D:\\out\\demo.mp4" --fps 2 --session rec1
  python session_recorder.py stop   --session rec1
  python session_recorder.py record -p "thanhdientraining" -o "D:\\out\\demo.mp4" --duration 8 --fps 2
"""
from __future__ import annotations

import argparse
import base64
import ctypes
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BRIDGE_ACTION_URL = "http://127.0.0.1:8766/action"
STATE_ROOT = Path(tempfile.gettempdir()) / "antigravity_browser_recordings"


def call_bridge(payload: dict, timeout: float = 10.0) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        BRIDGE_ACTION_URL,
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def send_window_to_background(title_substr: str = "Chrome") -> list[str]:
    """
    Khôi phục cửa sổ Chrome bị Minimize ở chế độ KHÔNG cướp focus (SW_SHOWNOACTIVATE=4)
    và đẩy xuống đáy Z-order (HWND_BOTTOM=1) phía sau các cửa sổ người dùng đang dùng.
    """
    if os.name != "nt":
        return []
    user32 = ctypes.windll.user32
    SW_SHOWNOACTIVATE = 4
    HWND_BOTTOM = 1
    SWP_NOSIZE = 0x0001
    SWP_NOMOVE = 0x0002
    SWP_NOACTIVATE = 0x0010

    matched = []
    q = title_substr.lower()

    @ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)
    def enum_cb(hwnd, _):
        if user32.IsWindowVisible(hwnd):
            n = user32.GetWindowTextLengthW(hwnd)
            if n > 0:
                buf = ctypes.create_unicode_buffer(n + 1)
                user32.GetWindowTextW(hwnd, buf, n + 1)
                t = buf.value
                if q in t.lower():
                    matched.append((hwnd, t))
        return True

    user32.EnumWindows(enum_cb, 0)
    results = []
    for hwnd, title in matched:
        if user32.IsIconic(hwnd):
            user32.ShowWindow(hwnd, SW_SHOWNOACTIVATE)
        user32.SetWindowPos(hwnd, HWND_BOTTOM, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE)
        results.append(title)
    return results


def capture_one_frame(profile: str, fmt: str = "jpeg", quality: int = 80) -> tuple[bytes | None, str]:
    try:
        res = call_bridge(
            {
                "action": "screenshot",
                "profile": profile,
                "format": fmt,
                "quality": quality,
                "focus": False,
                "timeout": 8,
            },
            timeout=10.0,
        )
        if res.get("status") == "ok" and res.get("screenshot"):
            b64 = res["screenshot"]
            if "," in b64:
                b64 = b64.split(",", 1)[1]
            return base64.b64decode(b64), str(res.get("method") or "ok")
        return None, str(res.get("error") or "unknown")
    except Exception as e:
        return None, str(e)


def stitch_mp4(frames_dir: Path, out_mp4: Path, fps: float) -> tuple[bool, str]:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        return False, "Khong tim thay 'ffmpeg' trong PATH!"

    frames = sorted(frames_dir.glob("frame_*.jpg"))
    if not frames:
        return False, "Khong co frame nao duoc ghi lai!"

    out_mp4.parent.mkdir(parents=True, exist_ok=True)
    # Save final snapshot right beside MP4 for easy QA read_file inspection
    last_snap = out_mp4.with_name(out_mp4.stem + "_last_frame.jpg")
    shutil.copy2(frames[-1], last_snap)

    cmd = [
        ffmpeg,
        "-y",
        "-framerate",
        str(max(0.5, fps)),
        "-i",
        str(frames_dir / "frame_%05d.jpg"),
        "-vf",
        "scale=trunc(iw/2)*2:trunc(ih/2)*2",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "+faststart",
        str(out_mp4),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        return False, (proc.stderr or proc.stdout)[-400:]
    return True, f"MP4={out_mp4} ({out_mp4.stat().st_size} bytes, {len(frames)} frames) | SNAP={last_snap}"


def run_worker(session_id: str, profile: str, out_mp4: Path, fps: float, quality: int, max_duration: float) -> int:
    s_dir = STATE_ROOT / session_id
    frames_dir = s_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    stop_flag = s_dir / "STOP"
    done_file = s_dir / "DONE.json"
    if stop_flag.exists():
        stop_flag.unlink()
    if done_file.exists():
        done_file.unlink()

    interval = 1.0 / max(0.5, fps)
    t0 = time.time()
    idx = 0
    errors = 0
    methods = {}

    while True:
        if stop_flag.exists():
            break
        if max_duration > 0 and (time.time() - t0) >= max_duration:
            break
        loop_start = time.time()
        raw, info = capture_one_frame(profile, fmt="jpeg", quality=quality)
        if raw:
            idx += 1
            (frames_dir / f"frame_{idx:05d}.jpg").write_bytes(raw)
            methods[info] = methods.get(info, 0) + 1
        else:
            errors += 1
        elapsed = time.time() - loop_start
        sleep_s = interval - elapsed
        if sleep_s > 0.02:
            time.sleep(sleep_s)

    ok, msg = stitch_mp4(frames_dir, out_mp4, fps=fps)
    summary = {
        "status": "ok" if ok else "error",
        "session": session_id,
        "profile": profile,
        "frames": idx,
        "errors": errors,
        "methods": methods,
        "elapsed_sec": round(time.time() - t0, 2),
        "out_mp4": str(out_mp4),
        "last_frame": str(out_mp4.with_name(out_mp4.stem + "_last_frame.jpg")),
        "message": msg,
    }
    done_file.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Silent Background CDP Browser MP4 Recorder")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_rel = sub.add_parser("reload", help="Reload Extension tren profile de ap dung background.js moi")
    p_rel.add_argument("-p", "--profile", required=True)

    p_bg = sub.add_parser("send-back", help="Day cua so Chrome dang Minimize ve nen khong cuop focus")
    p_bg.add_argument("--title", default="Chrome")

    p_start = sub.add_parser("start", help="Bat dau quay phim ngam trong nen")
    p_start.add_argument("-p", "--profile", required=True)
    p_start.add_argument("-o", "--out", required=True)
    p_start.add_argument("--fps", type=float, default=2.0)
    p_start.add_argument("--quality", type=int, default=80)
    p_start.add_argument("--session", default="default")
    p_start.add_argument("--max-duration", type=float, default=300.0)

    p_stop = sub.add_parser("stop", help="Dung quay va ghep MP4")
    p_stop.add_argument("--session", default="default")

    p_rec = sub.add_parser("record", help="Quay 1 luot co thoi luong co dinh")
    p_rec.add_argument("-p", "--profile", required=True)
    p_rec.add_argument("-o", "--out", required=True)
    p_rec.add_argument("--duration", type=float, default=8.0)
    p_rec.add_argument("--fps", type=float, default=2.0)
    p_rec.add_argument("--quality", type=int, default=80)

    p_worker = sub.add_parser("_worker", help=argparse.SUPPRESS)
    p_worker.add_argument("--session", required=True)
    p_worker.add_argument("-p", "--profile", required=True)
    p_worker.add_argument("-o", "--out", required=True)
    p_worker.add_argument("--fps", type=float, default=2.0)
    p_worker.add_argument("--quality", type=int, default=80)
    p_worker.add_argument("--max-duration", type=float, default=300.0)

    args = parser.parse_args()

    if args.cmd == "reload":
        res = call_bridge({"action": "reload_extension", "profile": args.profile}, timeout=8.0)
        print("RELOAD:", json.dumps(res, ensure_ascii=False))
        return 0 if res.get("status") == "ok" else 1

    if args.cmd == "send-back":
        wins = send_window_to_background(args.title)
        print(f"SENT_TO_BACKGROUND ({len(wins)}): {wins}")
        return 0

    if args.cmd == "_worker":
        return run_worker(args.session, args.profile, Path(args.out).resolve(), args.fps, args.quality, args.max_duration)

    if args.cmd == "record":
        sid = f"oneshot_{int(time.time())}"
        rc = run_worker(sid, args.profile, Path(args.out).resolve(), args.fps, args.quality, args.duration)
        done = STATE_ROOT / sid / "DONE.json"
        if done.is_file():
            print(done.read_text(encoding="utf-8"))
        return rc

    if args.cmd == "start":
        s_dir = STATE_ROOT / args.session
        if s_dir.exists():
            shutil.rmtree(s_dir, ignore_errors=True)
        s_dir.mkdir(parents=True, exist_ok=True)
        flags = 0
        if os.name == "nt":
            flags = (
                getattr(subprocess, "DETACHED_PROCESS", 0x00000008)
                | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0x00000200)
                | getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)
            )
        proc = subprocess.Popen(
            [
                sys.executable,
                "-u",
                str(Path(__file__).resolve()),
                "_worker",
                "--session",
                args.session,
                "-p",
                args.profile,
                "-o",
                str(Path(args.out).resolve()),
                "--fps",
                str(args.fps),
                "--quality",
                str(args.quality),
                "--max-duration",
                str(args.max_duration),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=flags,
            close_fds=True,
        )
        print(f"[RECORDER STARTED] session='{args.session}' | pid={proc.pid} | profile='{args.profile}' | out='{Path(args.out).resolve()}'")
        return 0

    if args.cmd == "stop":
        s_dir = STATE_ROOT / args.session
        if not s_dir.is_dir():
            print(f"[ERROR] Khong tim thay session '{args.session}'", file=sys.stderr)
            return 1
        (s_dir / "STOP").write_text("stop", encoding="utf-8")
        done_file = s_dir / "DONE.json"
        deadline = time.time() + 30.0
        while time.time() < deadline:
            if done_file.is_file():
                txt = done_file.read_text(encoding="utf-8")
                print(txt)
                data = json.loads(txt)
                return 0 if data.get("status") == "ok" else 1
            time.sleep(0.3)
        print("[ERROR] Timeout cho FFmpeg ghep MP4!", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
