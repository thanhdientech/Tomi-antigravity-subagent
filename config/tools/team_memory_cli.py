#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INFOASIA Team Memory & Javis Wiki Bridge CLI (Python313)
Mang logic bộ nhớ phân tầng & ghim tài liệu nguồn của JavisOS sang 11 Team Antigravity.

Cách dùng:
  & $PY team_memory_cli.py --list-teams
  & $PY team_memory_cli.py --read team-sap-b1-sql
  & $PY team_memory_cli.py --search-wiki "WIP 154"
  & $PY team_memory_cli.py --log-run team-web-wordpress-seo --agent web-wp-builder --task "Fix wp-config" --status PASS --summary "..." --evidence "HTTP 200"
  & $PY team_memory_cli.py --learn team-web-wordpress-seo --lesson "Không để trùng 2 dòng define WP_HOME trong wp-config.php"
  & $PY team_memory_cli.py --update-project --name "Web Tuoi Nong Nghiep" --path "D:\\xampp\\htdocs\\tuoinongnghiep" --team "Team 2" --status "HTTP 200" --next "QA Visual"
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CONFIG_ROOT = Path(__file__).resolve().parent.parent
MEM_ROOT = CONFIG_ROOT / "team_memory"
MANIFEST_FILE = MEM_ROOT / "teams_manifest.json"
PROJECTS_FILE = MEM_ROOT / "PROJECTS_INDEX.md"

_JAVIS_ENV = os.environ.get("JAVIS_BRAIN_DIR", "")
JAVIS_SEARCH_ROOTS = (
    [
        Path(_JAVIS_ENV) / "brains" / "Brain Default" / "wiki",
        Path(_JAVIS_ENV) / "brains" / "Brain Default" / "sources",
    ]
    if _JAVIS_ENV
    else []
)


def load_manifest() -> dict:
    if not MANIFEST_FILE.is_file():
        raise FileNotFoundError(f"Missing manifest: {MANIFEST_FILE}")
    return json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))


def cmd_list_teams():
    manifest = load_manifest()
    print(f"=== 11 TEAM ANTIGRAVITY x JAVIS MEMORY ({len(manifest)} teams) ===")
    for tname, info in manifest.items():
        runs_dir = MEM_ROOT / "teams" / tname / "runs"
        run_cnt = len(list(runs_dir.glob("*.md"))) if runs_dir.is_dir() else 0
        print(
            f"  - {tname:27s} | Leader: {info['leader']:25s} | "
            f"Members: {len(info['members'])} | Pinned: {len(info['pinned_paths']):2d} | Runs: {run_cnt}"
        )


def resolve_niche_memory_file(team: str, niche: str, create_if_missing: bool = False) -> Path:
    safe_niche = re.sub(r"[^a-zA-Z0-9._-]", "_", niche.strip())
    if not safe_niche:
        print("ERROR: Tên --niche không hợp lệ.", file=sys.stderr)
        sys.exit(1)
    ndir = MEM_ROOT / "teams" / team / "niches" / safe_niche
    mfile = ndir / "MEMORY.md"
    if create_if_missing and not mfile.is_file():
        ndir.mkdir(parents=True, exist_ok=True)
        mfile.write_text(
            f"# MEMORY — NGÁCH `{safe_niche}`\n\n"
            f"- **Team:** `{team}`\n"
            f"- **Phạm vi cách ly:** Chỉ lưu cấu hình & bài học riêng của ngách `{safe_niche}`.\n\n"
            f"## Bài Học Tích Lũy Riêng (Learned Patterns)\n",
            encoding="utf-8",
        )
    return mfile


def cmd_list_niches(team: str):
    manifest = load_manifest()
    if team not in manifest:
        print(f"ERROR: Unknown team '{team}'. Valid: {', '.join(manifest.keys())}", file=sys.stderr)
        sys.exit(1)
    ndir = MEM_ROOT / "teams" / team / "niches"
    print(f"=== DANH SACH NICHE MEMORY CUA TEAM '{team}' ===")
    if not ndir.is_dir():
        print("  (Chưa có thư mục niches/)")
        return
    found = sorted(ndir.glob("*/MEMORY.md"))
    if not found:
        print("  (Chưa có ngách nào)")
        return
    for mf in found:
        lines = mf.read_text(encoding="utf-8", errors="replace").splitlines()
        learned = sum(1 for ln in lines if ln.strip().startswith("- `["))
        print(f"  - {mf.parent.name:42s} | Bai hoc: {learned:2d} | {mf}")


def cmd_read_team(team: str, niche: str = ""):
    manifest = load_manifest()
    if team not in manifest:
        print(f"ERROR: Unknown team '{team}'. Valid: {', '.join(manifest.keys())}", file=sys.stderr)
        sys.exit(1)
    info = manifest[team]
    tdir = MEM_ROOT / "teams" / team
    mfile = tdir / "MEMORY.md"
    print(f"=== TEAM CONTEXT: {info['title']} ({team}) ===")
    print(f"Leader : {info['leader']}")
    print(f"Members: {', '.join(info['members'])}")
    print("\n--- TEAM MEMORY.md (DUNG CHUNG) ---")
    if mfile.is_file():
        print(mfile.read_text(encoding="utf-8").strip())
    else:
        print("(Chưa có MEMORY.md)")

    if niche:
        nfile = resolve_niche_memory_file(team, niche, create_if_missing=False)
        print(f"\n--- NICHE MEMORY.md ({niche}) ---")
        if nfile.is_file():
            print(nfile.read_text(encoding="utf-8").strip())
        else:
            print(f"(Chưa có MEMORY.md cho ngách '{niche}' tại {nfile})")
    else:
        ndir = tdir / "niches"
        if ndir.is_dir():
            niches = sorted(ndir.glob("*/MEMORY.md"))
            if niches:
                print("\n--- CAC BO NHO NGACH RIENG (dung --niche <ten> de doc) ---")
                for nf in niches:
                    print(f"  • {nf.parent.name} -> {nf}")

    runs_dir = tdir / "runs"
    runs = sorted(runs_dir.glob("*.md"), reverse=True)[:3] if runs_dir.is_dir() else []
    print(f"\n--- {len(runs)} NHAT KY CHAY GAN NHAT (runs/) ---")
    if not runs:
        print("(Chưa có nhật ký chạy nào)")
    for rf in runs:
        snippet = "\n".join(rf.read_text(encoding="utf-8").splitlines()[:12])
        print(f"\n[{rf.name}]\n{snippet}")


def cmd_search_wiki(query: str, limit: int = 8):
    terms = [t.lower() for t in re.split(r"\s+", query.strip()) if len(t) >= 2]
    if not terms:
        print("ERROR: Từ khóa quá ngắn.", file=sys.stderr)
        sys.exit(1)

    hits = []
    for root in JAVIS_SEARCH_ROOTS:
        if not root.is_dir():
            continue
        for fp in root.rglob("*"):
            if not fp.is_file() or fp.suffix.lower() not in {".md", ".txt", ".csv"}:
                continue
            try:
                txt = fp.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            low = txt.lower()
            name_low = fp.name.lower()
            score = 0
            for t in terms:
                if t in name_low:
                    score += 5
                cnt = low.count(t)
                if cnt > 0:
                    score += min(cnt, 10)
            if score > 0:
                # Extract first matching line as snippet
                snip = ""
                for ln in txt.splitlines():
                    if any(t in ln.lower() for t in terms) and ln.strip():
                        snip = ln.strip()[:140]
                        break
                hits.append((score, str(fp), snip))

    hits.sort(key=lambda x: x[0], reverse=True)
    print(f"=== JAVIS WIKI/SOURCES SEARCH: '{query}' ({len(hits)} ket qua, hien top {min(limit, len(hits))}) ===")
    for score, path, snip in hits[:limit]:
        print(f"  [score={score:2d}] {path}")
        if snip:
            print(f"             -> {snip}")


def cmd_log_run(team: str, agent: str, task: str, status: str, summary: str, evidence: str):
    manifest = load_manifest()
    if team not in manifest:
        print(f"ERROR: Unknown team '{team}'", file=sys.stderr)
        sys.exit(1)
    runs_dir = MEM_ROOT / "teams" / team / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_agent = re.sub(r"[^a-zA-Z0-9_-]", "-", agent.strip()) or "agent"
    out_file = runs_dir / f"{ts}_{safe_agent}.md"
    body = (
        f"# Run Log — {task}\n\n"
        f"- **Thời điểm:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"- **Team:** `{team}`\n"
        f"- **Agent:** `{agent}`\n"
        f"- **Trạng thái:** `{status.upper()}`\n\n"
        f"## Tóm tắt kết quả\n{summary}\n\n"
        f"## Bằng chứng QA\n{evidence}\n"
    )
    out_file.write_text(body, encoding="utf-8")
    print(f"OK LOGGED: {out_file}")


def cmd_learn(team: str, lesson: str, niche: str = ""):
    manifest = load_manifest()
    if team not in manifest:
        print(f"ERROR: Unknown team '{team}'", file=sys.stderr)
        sys.exit(1)
    if niche:
        mfile = resolve_niche_memory_file(team, niche, create_if_missing=True)
    else:
        mfile = MEM_ROOT / "teams" / team / "MEMORY.md"
        if not mfile.is_file():
            print(f"ERROR: Missing {mfile}", file=sys.stderr)
            sys.exit(1)
    clean_lesson = " ".join(lesson.strip().splitlines()).strip()
    existing = mfile.read_text(encoding="utf-8")
    if clean_lesson.lower() in existing.lower():
        print(f"SKIP DUPLICATE: Bài học đã tồn tại trong {mfile}")
        return
    date_str = datetime.now().strftime("%Y-%m-%d")
    new_line = f"- `[{date_str}]` {clean_lesson}\n"
    if not existing.endswith("\n"):
        existing += "\n"
    mfile.write_text(existing + new_line, encoding="utf-8")
    print(f"OK LEARNED -> {mfile}: {new_line.strip()}")


def cmd_agent_read(agent_slug: str):
    amem = MEM_ROOT / "agents" / agent_slug / "MEMORY.md"
    if not amem.is_file():
        print(f"ERROR: Unknown agent '{agent_slug}' (missing {amem})", file=sys.stderr)
        sys.exit(1)
    print(amem.read_text(encoding="utf-8").strip())


def cmd_agent_learn(agent_slug: str, lesson: str):
    amem = MEM_ROOT / "agents" / agent_slug / "MEMORY.md"
    if not amem.is_file():
        print(f"ERROR: Unknown agent '{agent_slug}' (missing {amem})", file=sys.stderr)
        sys.exit(1)
    clean_lesson = " ".join(lesson.strip().splitlines()).strip()
    existing = amem.read_text(encoding="utf-8")
    if clean_lesson.lower() in existing.lower():
        print(f"SKIP DUPLICATE: Bài học đã tồn tại trong {amem}")
        return
    date_str = datetime.now().strftime("%Y-%m-%d")
    new_line = f"- `[{date_str}]` {clean_lesson}\n"
    if not existing.endswith("\n"):
        existing += "\n"
    amem.write_text(existing + new_line, encoding="utf-8")
    print(f"OK AGENT LEARNED -> {amem}: {new_line.strip()}")


def cmd_update_project(name: str, path: str, team: str, status: str, next_step: str):
    if not PROJECTS_FILE.is_file():
        print(f"ERROR: Missing {PROJECTS_FILE}", file=sys.stderr)
        sys.exit(1)
    lines = PROJECTS_FILE.read_text(encoding="utf-8").splitlines()
    row = f"| **{name}** | `{path}` | {team} | {status} | {next_step} |"
    updated = False
    out_lines = []
    for ln in lines:
        if ln.startswith("|") and f"**{name}**" in ln:
            out_lines.append(row)
            updated = True
        else:
            out_lines.append(ln)
    if not updated:
        out_lines.append(row)
    PROJECTS_FILE.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    print(f"OK PROJECT {'UPDATED' if updated else 'ADDED'}: {name} -> {PROJECTS_FILE}")


def main():
    p = argparse.ArgumentParser(description="INFOASIA Team Memory & Javis Wiki Bridge CLI")
    p.add_argument("--list-teams", action="store_true", help="Liệt kê 11 Team & thống kê memory")
    p.add_argument("--list-niches", metavar="TEAM", help="Liệt kê các MEMORY.md riêng theo ngách của Team")
    p.add_argument("--read", metavar="TEAM", help="Đọc MEMORY.md, tài liệu ghim và runs gần nhất của Team")
    p.add_argument("--niche", default="", help="Tên ngách riêng (vd: 02_Ngach_KosmosGeist_Sleep_Science_US) cho --read / --learn")
    p.add_argument("--search-wiki", metavar="QUERY", help="Tìm nhanh trong kho JavisOS wiki/ & sources/")
    p.add_argument("--limit", type=int, default=8, help="Số kết quả tìm kiếm tối đa")
    p.add_argument("--log-run", metavar="TEAM", help="Ghi nhật ký chạy vào teams/<TEAM>/runs/")
    p.add_argument("--agent", default="coordinator")
    p.add_argument("--task", default="Task")
    p.add_argument("--status", default="PASS")
    p.add_argument("--summary", default="")
    p.add_argument("--evidence", default="")
    p.add_argument("--learn", metavar="TEAM", help="Lưu bài học thực chiến vào teams/<TEAM>/MEMORY.md (hoặc niches/<NICHE>/MEMORY.md khi có --niche)")
    p.add_argument("--agent-read", metavar="AGENT", help="Đọc bộ nhớ riêng agents/<AGENT>/MEMORY.md")
    p.add_argument("--agent-learn", metavar="AGENT", help="Lưu bài học riêng vào agents/<AGENT>/MEMORY.md")
    p.add_argument("--lesson", default="")
    p.add_argument("--update-project", action="store_true", help="Cập nhật PROJECTS_INDEX.md")
    p.add_argument("--name", default="")
    p.add_argument("--path", default="")
    p.add_argument("--team", default="")
    p.add_argument("--next", dest="next_step", default="")
    args = p.parse_args()

    if args.list_teams:
        cmd_list_teams()
    elif args.list_niches:
        cmd_list_niches(args.list_niches)
    elif args.read:
        cmd_read_team(args.read, args.niche)
    elif args.agent_read:
        cmd_agent_read(args.agent_read)
    elif args.search_wiki:
        cmd_search_wiki(args.search_wiki, args.limit)
    elif args.log_run:
        cmd_log_run(args.log_run, args.agent, args.task, args.status, args.summary, args.evidence)
    elif args.learn:
        if not args.lesson:
            print("ERROR: Thiếu --lesson", file=sys.stderr)
            sys.exit(1)
        cmd_learn(args.learn, args.lesson, args.niche)
    elif args.agent_learn:
        if not args.lesson:
            print("ERROR: Thiếu --lesson", file=sys.stderr)
            sys.exit(1)
        cmd_agent_learn(args.agent_learn, args.lesson)
    elif args.update_project:
        if not args.name:
            print("ERROR: Thiếu --name", file=sys.stderr)
            sys.exit(1)
        cmd_update_project(args.name, args.path, args.team, args.status, args.next_step)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
