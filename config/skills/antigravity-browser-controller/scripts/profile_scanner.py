#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
profile_scanner.py — Công cụ Dò, Mở & Kết Nối Bất Kỳ Profile Trình Duyệt Nào Trên Máy Tính
Cho hệ thống 14 Team Antigravity × Antigravity Omni-Browser Controller (WS :8765 / HTTP :8766).

Cách dùng:
  python profile_scanner.py --ensure-bridge          # Đảm bảo Bridge :8765/:8766 đang sống (chống lỗi 10048)
  python profile_scanner.py --scan                   # Quét mọi Profile Chrome/Cốc Cốc/Edge/Brave + trạng thái live :8766
  python profile_scanner.py --scan --json            # Xuất JSON chuẩn cho AI Agent đọc
  python profile_scanner.py --open "rjemma"          # Tự tìm & mở đúng profile + đợi nối Bridge :8766
  python profile_scanner.py --open "Profile 7" --browser chrome
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).resolve().parent
SERVER_PY = SCRIPT_DIR / "server.py"
EXT_DIR = SCRIPT_DIR.parent / "extension"
BRIDGE_STATUS_URL = "http://127.0.0.1:8766/status"


def get_browser_configs() -> list[dict]:
    local_app = Path(os.environ.get("LOCALAPPDATA", ""))
    prog_files = Path(os.environ.get("PROGRAMFILES", r"C:\Program Files"))
    prog_x86 = Path(os.environ.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)"))

    candidates = [
        {
            "id": "chrome",
            "name": "Google Chrome",
            "user_data": local_app / "Google" / "Chrome" / "User Data",
            "exes": [
                prog_files / "Google" / "Chrome" / "Application" / "chrome.exe",
                prog_x86 / "Google" / "Chrome" / "Application" / "chrome.exe",
                local_app / "Google" / "Chrome" / "Application" / "chrome.exe",
            ],
        },
        {
            "id": "coccoc",
            "name": "Coc Coc",
            "user_data": local_app / "CocCoc" / "Browser" / "User Data",
            "exes": [
                prog_files / "CocCoc" / "Browser" / "Application" / "browser.exe",
                prog_x86 / "CocCoc" / "Browser" / "Application" / "browser.exe",
                local_app / "CocCoc" / "Browser" / "Application" / "browser.exe",
            ],
        },
        {
            "id": "edge",
            "name": "Microsoft Edge",
            "user_data": local_app / "Microsoft" / "Edge" / "User Data",
            "exes": [
                prog_x86 / "Microsoft" / "Edge" / "Application" / "msedge.exe",
                prog_files / "Microsoft" / "Edge" / "Application" / "msedge.exe",
            ],
        },
        {
            "id": "brave",
            "name": "Brave",
            "user_data": local_app / "BraveSoftware" / "Brave-Browser" / "User Data",
            "exes": [
                prog_files / "BraveSoftware" / "Brave-Browser" / "Application" / "brave.exe",
                prog_x86 / "BraveSoftware" / "Brave-Browser" / "Application" / "brave.exe",
                local_app / "BraveSoftware" / "Brave-Browser" / "Application" / "brave.exe",
            ],
        },
    ]
    out = []
    for c in candidates:
        exe = next((e for e in c["exes"] if e.is_file()), None)
        if c["user_data"].is_dir() or exe:
            out.append({**c, "exe": str(exe) if exe else ""})
    return out


def fetch_bridge_status(timeout: float = 2.5) -> dict | None:
    try:
        with urllib.request.urlopen(BRIDGE_STATUS_URL, timeout=timeout) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode("utf-8", errors="replace"))
    except Exception:
        return None
    return None


def ensure_bridge(wait_sec: float = 8.0) -> tuple[bool, dict | None]:
    st = fetch_bridge_status(timeout=2.0)
    if st:
        return True, st

    if not SERVER_PY.is_file():
        print(f"[ERROR] Khong tim thay Bridge Server: {SERVER_PY}", file=sys.stderr)
        return False, None

    creation_flags = 0
    if os.name == "nt":
        creation_flags = (
            getattr(subprocess, "DETACHED_PROCESS", 0x00000008)
            | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0x00000200)
            | getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)
        )

    subprocess.Popen(
        [sys.executable, "-u", str(SERVER_PY)],
        cwd=str(SCRIPT_DIR),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
        close_fds=True,
    )

    deadline = time.time() + wait_sec
    while time.time() < deadline:
        time.sleep(0.5)
        st = fetch_bridge_status(timeout=1.5)
        if st:
            return True, st
    return False, None


def has_antigravity_extension(profile_path: Path) -> bool:
    pref = profile_path / "Preferences"
    if not pref.is_file():
        return False
    try:
        raw = pref.read_text(encoding="utf-8", errors="ignore")
        return ("Antigravity Browser" in raw) or ("antigravity-browser-controller" in raw)
    except Exception:
        return False


def scan_all_profiles() -> dict:
    bridge = fetch_bridge_status(timeout=2.0)
    live_conns = (bridge or {}).get("connections", [])
    live_emails = {str(c.get("email") or "").lower(): c for c in live_conns if c.get("email")}

    discovered = []
    for br in get_browser_configs():
        ud = br["user_data"]
        ls_file = ud / "Local State"
        info_cache = {}
        if ls_file.is_file():
            try:
                ls_data = json.loads(ls_file.read_text(encoding="utf-8", errors="replace"))
                info_cache = (ls_data.get("profile") or {}).get("info_cache") or {}
            except Exception:
                info_cache = {}

        if not info_cache and ud.is_dir():
            for sub in sorted(ud.iterdir()):
                if sub.is_dir() and (sub.name == "Default" or sub.name.startswith("Profile ")):
                    info_cache[sub.name] = {"name": sub.name, "user_name": ""}

        for prof_dir, meta in sorted(info_cache.items()):
            p_path = ud / prof_dir
            if not p_path.is_dir():
                continue
            email = str(meta.get("user_name") or "").strip()
            disp = str(meta.get("name") or meta.get("gaia_name") or prof_dir).strip()
            live = live_emails.get(email.lower()) if email else None
            discovered.append({
                "browser": br["id"],
                "browser_name": br["name"],
                "exe": br["exe"],
                "profile_dir": prof_dir,
                "display_name": disp,
                "email": email,
                "ext_installed": has_antigravity_extension(p_path),
                "connected": bool(live),
                "bridge_profile_key": (
                    (live.get("declared_profile") if live.get("declared_profile") != "default" else live.get("inferred_profile"))
                    if live else ""
                ),
            })

    return {
        "bridge_online": bridge is not None,
        "ws_port": 8765,
        "http_port": 8766,
        "live_active_profiles": (bridge or {}).get("active_profiles", []),
        "live_connections": live_conns,
        "disk_profiles": discovered,
    }


def open_profile(query: str, browser_filter: str = "", wait_sec: float = 12.0) -> int:
    ok, bridge = ensure_bridge()
    if not ok:
        print("[FAIL] Khong the khoi dong Bridge Server :8765/:8766!", file=sys.stderr)
        return 1

    q = query.strip().lower()
    # 1. Check if already connected live on :8766
    for c in (bridge or {}).get("connections", []):
        fields = [
            str(c.get("declared_profile") or "").lower(),
            str(c.get("inferred_profile") or "").lower(),
            str(c.get("email") or "").lower(),
        ]
        if any(q in f for f in fields if f):
            key = c.get("declared_profile") if c.get("declared_profile") != "default" else c.get("inferred_profile")
            print(f"[READY] Profile da ket noi san tren Bridge :8766 -> key='{key}' | email='{c.get('email')}' | tabs={c.get('tab_count')}")
            return 0

    # 2. Search across all browser profiles on disk
    scan = scan_all_profiles()
    matches = []
    for p in scan["disk_profiles"]:
        if browser_filter and p["browser"] != browser_filter.lower():
            continue
        hay = f"{p['browser']} {p['profile_dir']} {p['display_name']} {p['email']}".lower()
        if q in hay:
            matches.append(p)

    if not matches:
        print(f"[NOT_FOUND] Khong tim thay profile nao khop '{query}'. Hay chay --scan de xem danh sach.", file=sys.stderr)
        return 2

    target = matches[0]
    if not target["exe"]:
        print(f"[ERROR] Khong tim thay file thuc thi cho trinh duyet {target['browser_name']}.", file=sys.stderr)
        return 3

    print(f"[LAUNCH] Mo {target['browser_name']} | profile_dir='{target['profile_dir']}' | name='{target['display_name']}' | email='{target['email']}'")
    cmd = [target["exe"], f"--profile-directory={target['profile_dir']}"]
    subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if not target["ext_installed"]:
        print(
            f"[WARN] Profile '{target['profile_dir']}' chua cai Extension Antigravity Browser.\n"
            f"       Vao chrome://extensions -> Bat Developer mode -> Load unpacked thu muc:\n"
            f"       {EXT_DIR}"
        )

    # 3. Poll Bridge :8766 waiting for extension handshake
    deadline = time.time() + wait_sec
    target_email = target["email"].lower()
    while time.time() < deadline:
        time.sleep(1.0)
        st = fetch_bridge_status(timeout=1.5)
        if not st:
            continue
        for c in st.get("connections", []):
            em = str(c.get("email") or "").lower()
            if (target_email and em == target_email) or (q in str(c.get("declared_profile") or "").lower()) or (q in str(c.get("inferred_profile") or "").lower()):
                key = c.get("declared_profile") if c.get("declared_profile") != "default" else c.get("inferred_profile")
                print(f"[CONNECTED] Profile da bat tay Bridge :8766 -> key='{key}' | email='{c.get('email')}'")
                return 0

    print("[TIMEOUT] Da mo trinh duyet nhung Extension chua bat tay :8765 trong 12s (kiem tra Extension da bat trong profile nay chua).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Antigravity Multi-Browser Profile Scanner & Connector")
    parser.add_argument("--ensure-bridge", action="store_true", help="Dam bao Bridge Server :8765/:8766 dang chay")
    parser.add_argument("--scan", action="store_true", help="Quet tat ca profile Chrome/CocCoc/Edge/Brave & trang thai Bridge")
    parser.add_argument("--open", default="", help="Mo & ket noi 1 profile theo ten/email/thu muc (vd: rjemma, Profile 7)")
    parser.add_argument("--browser", default="", help="Loc theo trinh duyet: chrome|coccoc|edge|brave")
    parser.add_argument("--json", action="store_true", help="Xuat dinh dang JSON")
    args = parser.parse_args()

    if args.ensure_bridge and not args.scan and not args.open:
        ok, st = ensure_bridge()
        if args.json:
            print(json.dumps({"bridge_online": ok, "status": st}, ensure_ascii=False, indent=2))
        else:
            print(f"BRIDGE ONLINE: {ok} | active_profiles={((st or {}).get('active_profiles') or [])}")
        return 0 if ok else 1

    if args.open:
        return open_profile(args.open, browser_filter=args.browser)

    # Default or --scan
    data = scan_all_profiles()
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0

    print(f"=== ANTIGRAVITY OMNI-BROWSER BRIDGE: {'ONLINE (HTTP 200)' if data['bridge_online'] else 'OFFLINE'} ===")
    print(f"Live connected profiles ({len(data['live_connections'])}): {data['live_active_profiles']}\n")
    print(f"Disk browser profiles ({len(data['disk_profiles'])}):")
    for p in data["disk_profiles"]:
        st_icon = f"CONNECTED [key={p['bridge_profile_key']}]" if p["connected"] else ("OFFLINE (Ext OK)" if p["ext_installed"] else "OFFLINE (No Ext)")
        print(f"  - [{p['browser']:6s}] {p['profile_dir']:11s} | {p['display_name'][:22]:22s} | {p['email'][:32]:32s} | {st_icon}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
