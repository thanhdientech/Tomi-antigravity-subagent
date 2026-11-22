#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Antigravity Official SessionStart Hook — Javis-Grade Team Memory Loader (Portable)
Chạy ĐÚNG 1 LẦN khi mở hội thoại mới (0 phình context các lượt sau).
Tự động nạp danh bạ dự án đang làm (PROJECTS_INDEX.md), nhận diện Team phù hợp với workspace hiện tại
và nhắc đường dẫn tra cứu Wiki/Sources + Workflow 4 pha chuẩn Javis.
"""

import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_DIR = SCRIPT_DIR.parent
MEM_DIR = CONFIG_DIR / "team_memory"
PROJECTS_FILE = MEM_DIR / "PROJECTS_INDEX.md"
MEM_CLI = CONFIG_DIR / "tools" / "team_memory_cli.py"
WORKFLOW_FILE = CONFIG_DIR / "workflows" / "javis_team_runner.py"
PY_EXE = str(Path(sys.executable).resolve())


def read_stdin() -> dict:
    try:
        if not sys.stdin.isatty():
            raw = sys.stdin.read()
            if raw and raw.strip():
                data = json.loads(raw)
                if isinstance(data, dict):
                    return data
    except Exception:
        pass
    return {}


def detect_team_from_workspaces(workspaces: list[str]) -> str:
    joined = " ".join(str(w).lower() for w in workspaces)
    rules = [
        (["javisos", "javis-os", "infoasia_ai_agent", "n8n"], "team-javisos-n8n"),
        (["sap", "sql", "beas", "erp"], "team-sap-b1-sql"),
        (["htdocs", "wordpress", "flatsome", "landing", "web"], "team-web-wordpress-seo"),
        (["tiep thi lien ke shoppe", "shopee_kol_studio", "nghien_cuu_kenh_moi", "shopee affiliate", "reels"], "team-short-video-affiliate"),
        (["xây kênh youtube", "tim ngach", "ngach_", "omniflash", "before us decoded", "every myth", "kosmosgeist"], "team-youtube-factory"),
        (["video", "edit", "remotion", "manim", "recordly"], "team-video-editing-motion"),
        (["youtube", "kenh", "drama", "myth", "kosmos", "kol"], "team-video-film-channel"),
        (["vps", "server", "hosting", "directadmin", "linux"], "team-server-vps-hosting"),
        (["ads", "marketing", "google ads", "content"], "team-marketing-ads"),
        (["design", "brand", "logo", "ui", "ux"], "team-design-creative"),
        (["javis"], "team-orchestrator-qa"),
    ]
    for keywords, team in rules:
        if any(k in joined for k in keywords):
            return team
    return ""


def main():
    payload = read_stdin()
    workspaces = payload.get("workspacePaths") or []
    matched_team = detect_team_from_workspaces(workspaces)

    lines = [
        "🧠 [SESSION START — 11 TEAMS x JAVIS-GRADE TEAM MEMORY LOADED]:",
        f"- Kho bộ nhớ 11 Phòng Ban: `{MEM_DIR}` (PROJECTS_INDEX.md, WIKI_BRIDGE.md, teams/<team>/MEMORY.md + runs/).",
        f"- Tra cứu Wiki/Sources & đọc/ghi bộ nhớ nhóm: `& \"{PY_EXE}\" \"{MEM_CLI}\" --read <team> | --search-wiki \"<tu_khoa>\" | --log-run ... | --learn ...`",
        f"- Dây chuyền nhóm 4 pha chuẩn Javis (`plan -> work -> verify+retry -> memory`): `run_workflow` với `{WORKFLOW_FILE}`.",
    ]

    if matched_team:
        mfile = MEM_DIR / "teams" / matched_team / "MEMORY.md"
        lines.append(f"- Workspace khớp tự động với phòng ban: `{matched_team}` (đọc nhanh `{mfile}` trước khi thực thi).")

    if PROJECTS_FILE.is_file():
        p_rows = [
            ln.strip()
            for ln in PROJECTS_FILE.read_text(encoding="utf-8", errors="replace").splitlines()
            if ln.strip().startswith("| **")
        ][:8]
        if p_rows:
            lines.append("- Dự án đang theo dõi (`PROJECTS_INDEX.md`):")
            lines.extend(f"  {r[:180]}" for r in p_rows)

    msg = "\n".join(lines)
    out = {
        "injectSteps": [
            {
                "systemMessage": {
                    "systemMessage": msg
                }
            }
        ]
    }
    sys.stdout.write(json.dumps(out, ensure_ascii=False) + "\n")
    sys.stdout.flush()
    sys.exit(0)


if __name__ == "__main__":
    main()
