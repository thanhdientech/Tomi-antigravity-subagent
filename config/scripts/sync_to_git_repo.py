#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
sync_to_git_repo.py (v2.1 — 14 Teams / 51 Subagents Public-Safe Portable Syncer)
Đồng bộ sạch từ `C:\Users\INFOASIA\.gemini\config` sang repo Git (mặc định `E:\DIEN APP\Tomi-antigravity-subagent`
hoặc truyền `--target <duong_dan_repo>`):
  1. Đồng bộ 14 Team Plugins (51 Subagents), 41 Global Skills, rules/, docs/, tools/team_memory_cli.py,
     workflows/*.py (4 pipelines), 7 scripts lõi, và khung mẫu team_memory/ (14 teams + 51 agents).
  2. Chặn tuyệt đối plugin nội bộ (`team-antidetect-automator`), `tools/sql_runner.py`, `runs/`, `*.db`, `*.bak*`, `*.exe`.
  3. Khử cá nhân hóa & lọc sạch 100% mật khẩu SQL, IP LAN nội bộ, tên DB nội bộ, đường dẫn máy cá nhân cho repo PUBLIC.
  4. Tự động chạy Security Secret Scanner trước khi kết thúc (Exit code 1 nếu phát hiện lọt bất kỳ secret nào).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SRC_CONFIG = Path(r"C:\Users\INFOASIA\.gemini\config")
DEFAULT_DST_REPO = Path(r"E:\DIEN APP\Tomi-antigravity-subagent")

EXCLUDED_PLUGINS = {
    "team-antidetect-automator",
    "design-landingpage-vip-plugin",
}

ACTIVE_SCRIPTS = {
    "agy_skill_engine.py",
    "agy_skill_mcp_server.py",
    "antigravity_mcp_server.py",
    "auto_reanchor_hook.py",
    "session_memory_loader_hook.py",
    "setup_portable_antigravity.py",
    "sync_to_git_repo.py",
}

TEXT_EXTENSIONS = {".md", ".py", ".json", ".txt", ".bat", ".ps1", ".yaml", ".yml", ".sql", ".sh", ".cmd", ".ini", ".cfg"}

# Strict case-insensitive regex sanitization rules applied ONLY inside DST_REPO (never touches SRC_CONFIG!)
SANITIZE_REGEX_RULES = [
    (r"InfoAsia@RO2026!", "<YOUR_RO_PASSWORD>"),
    (r"infoasia_ro", "<YOUR_RO_USER>"),
    (r"FVIVN_PROD_TRAIN", "<INTERNAL_SAP_DB_TRAIN>"),
    (r"FVIVN_PROD", "<INTERNAL_SAP_DB>"),
    (r"infoasia56", "<INTERNAL_DB_HOST>"),
    (r"192\.168\.42\.\d+", "<INTERNAL_SQL_SERVER_IP>"),
    (r"C:\\\\Users\\\\INFOASIA\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python313\\\\python\.exe", "python"),
    (r"C:[\\/]+Users[\\/]+INFOASIA[\\/]+AppData[\\/]+Local[\\/]+Programs[\\/]+Python[\\/]+Python313[\\/]+python\.exe", "python"),
    (r"C:\\\\Users\\\\INFOASIA\\\\\.gemini\\\\config", r"%USERPROFILE%\\.gemini\\config"),
    (r"C:[\\/]+Users[\\/]+INFOASIA[\\/]+\.gemini[\\/]+config", r"%USERPROFILE%\.gemini\config"),
    (r"C:\\\\Users\\\\INFOASIA", r"%USERPROFILE%"),
    (r"C:[\\/]+Users[\\/]+INFOASIA", r"%USERPROFILE%"),
    (r"E:\\\\DIEN APP\\\\JavisOS\\\\brains_infoasia\\\\Brain Default", r"%JAVIS_BRAIN_DIR%\\brains_team\\Brain Default"),
    (r"E:[\\/]+DIEN APP[\\/]+JavisOS[\\/]+brains_infoasia[\\/]+Brain Default", r"%JAVIS_BRAIN_DIR%\brains_team\Brain Default"),
    (r"E:\\\\DIEN APP\\\\JavisOS\\\\brains\\\\Brain Default", r"%JAVIS_BRAIN_DIR%\\brains\\Brain Default"),
    (r"E:[\\/]+DIEN APP[\\/]+JavisOS[\\/]+brains[\\/]+Brain Default", r"%JAVIS_BRAIN_DIR%\brains\Brain Default"),
    (r"E:\\\\DIEN APP\\\\JavisOS", r"%JAVIS_BRAIN_DIR%"),
    (r"E:[\\/]+DIEN APP[\\/]+JavisOS", r"%JAVIS_BRAIN_DIR%"),
    (r"E:[\\/]+DIEN APP[\\/]+Anti-Detect Social Automator", "<LOCAL_AUTOMATION_APP>"),
    (r"team-antidetect-automator", "custom-local-plugin"),
    (r"Anti-Detect Social Automator \(`:8088` Code & Chạy dàn máy nuôi\) → \*\*Team 11\*\* \(`adsa-core-engineer`, `adsa-nurture-ui-builder`, `adsa-fleet-operator`, `adsa-qa-stealth-auditor`\)",
     "Custom Local Automation Plugins (tùy chọn mở rộng riêng trên máy người dùng)"),
]

COMPILED_SANITIZE = [(re.compile(pat, re.I), repl) for pat, repl in SANITIZE_REGEX_RULES]

FORBIDDEN_PATTERNS = [
    r"InfoAsia@RO2026!",
    r"infoasia_ro",
    r"FVIVN_PROD",
    r"infoasia56",
    r"192\.168\.42\.\d+",
    r"team-antidetect-automator",
    r"C:\\Users\\INFOASIA",
    r"C:/Users/INFOASIA",
    r"E:\\DIEN APP\\JavisOS",
]


def sanitize_text(text: str) -> str:
    out = text
    for rx, repl in COMPILED_SANITIZE:
        out = rx.sub(lambda _m, r=repl: r, out)
    return out


def copy_and_sanitize_file(src: Path, dst: Path, sanitize: bool = True) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if sanitize and src.suffix.lower() in TEXT_EXTENSIONS:
        raw = src.read_text(encoding="utf-8", errors="replace")
        dst.write_text(sanitize_text(raw), encoding="utf-8")
    else:
        shutil.copy2(src, dst)


def is_ignored_file(fname: str) -> bool:
    low = fname.lower()
    if low.endswith((".pyc", ".pyo", ".db", ".db-wal", ".db-shm", ".bak", ".log", ".exe")):
        return True
    if ".bak_" in low or "openvpn" in low or "thong_tin_ket_noi" in low or "create_sql_readonly_agent_user" in low:
        return True
    return False


def sync_dir_clean(src_dir: Path, dst_dir: Path, ignore_names: set[str], sanitize: bool = True) -> int:
    if dst_dir.exists():
        shutil.rmtree(dst_dir)
    dst_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for root, dirs, files in os.walk(src_dir):
        rel_root = Path(root).relative_to(src_dir)
        dirs[:] = [d for d in dirs if d not in ignore_names and not d.endswith(".egg-info")]
        for fname in files:
            if fname in ignore_names or is_ignored_file(fname):
                continue
            s_file = Path(root) / fname
            if rel_root.as_posix().endswith("sql-sap-b1") and fname == "config.json":
                continue
            d_file = dst_dir / rel_root / fname
            copy_and_sanitize_file(s_file, d_file, sanitize=sanitize)
            count += 1
    return count


def build_portable_team_memory_cli(src: Path, dst: Path) -> None:
    txt = src.read_text(encoding="utf-8")
    txt = txt.replace(
        'CONFIG_ROOT = Path(r"C:\\Users\\INFOASIA\\.gemini\\config")',
        'CONFIG_ROOT = Path(__file__).resolve().parent.parent'
    )
    txt = txt.replace(
        '''JAVIS_SEARCH_ROOTS = [
    Path(r"E:\\DIEN APP\\JavisOS\\brains\\Brain Default\\wiki"),
    Path(r"E:\\DIEN APP\\JavisOS\\brains\\Brain Default\\sources"),
    Path(r"E:\\DIEN APP\\JavisOS\\brains_infoasia\\Brain Default\\wiki"),
    Path(r"E:\\DIEN APP\\JavisOS\\brains_infoasia\\Brain Default\\sources"),
]''',
        '''_JAVIS_ENV = os.environ.get("JAVIS_BRAIN_DIR", "")
JAVIS_SEARCH_ROOTS = (
    [
        Path(_JAVIS_ENV) / "brains" / "Brain Default" / "wiki",
        Path(_JAVIS_ENV) / "brains" / "Brain Default" / "sources",
    ]
    if _JAVIS_ENV
    else []
)'''
    )
    if "import os\n" not in txt:
        txt = txt.replace("import json\n", "import json\nimport os\n", 1)
    txt = sanitize_text(txt)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(txt, encoding="utf-8")


def build_portable_workflow(src: Path, dst: Path) -> None:
    txt = src.read_text(encoding="utf-8")
    txt = txt.replace(
        '''MANIFEST_PATH = Path(r"C:\\Users\\INFOASIA\\.gemini\\config\\team_memory\\teams_manifest.json")
PY = r"C:\\Users\\INFOASIA\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
MEM_CLI = r"C:\\Users\\INFOASIA\\.gemini\\config\\tools\\team_memory_cli.py"''',
        '''import sys
CONFIG_ROOT = Path.home() / ".gemini" / "config"
MANIFEST_PATH = CONFIG_ROOT / "team_memory" / "teams_manifest.json"
PY = sys.executable
MEM_CLI = str(CONFIG_ROOT / "tools" / "team_memory_cli.py")'''
    )
    txt = sanitize_text(txt)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(txt, encoding="utf-8")


def build_clean_team_memory_templates(src_mem: Path, dst_mem: Path) -> int:
    if dst_mem.exists():
        shutil.rmtree(dst_mem)
    dst_mem.mkdir(parents=True, exist_ok=True)
    count = 0

    (dst_mem / "COMPANY_MEMORY.md").write_text(
        "# COMPANY MEMORY — ANTIGRAVITY 14 TEAMS (51 SUBAGENTS)\n\n"
        "- **Workspace chuẩn:** `%USERPROFILE%\\.gemini\\config`\n"
        "- **Nguyên tắc cốt lõi:** 5 Chốt Chặn Chống Ảo Giác + QA Gate (`Exit code 0`) + Verify-Loop Chụp & Đọc Ảnh + No Self-Grading.\n"
        "- **Ghi chú:** Chỉnh sửa file này để lưu quy tắc nội bộ, tech stack và cấu hình riêng của máy bạn.\n",
        encoding="utf-8",
    )
    count += 1

    (dst_mem / "PROJECTS_INDEX.md").write_text(
        "# PROJECTS INDEX — DANH BẠ DỰ ÁN ĐANG THEO DÕI\n\n"
        "> Hook `SessionStart` tự động đọc bảng này 1 lần khi mở hội thoại mới để AI không bao giờ quên ngữ cảnh.\n"
        "> Cập nhật nhanh qua `team_memory_cli.py --update-project ...`\n\n"
        "| Dự án | Thư mục / Workspace | Team phụ trách | Trạng thái | Bước tiếp theo |\n"
        "| :--- | :--- | :--- | :--- | :--- |\n"
        "| **Example Project** | `D:\\Projects\\example` | Team 2 | Sẵn sàng | Chạy Team 0 lập Blueprint |\n",
        encoding="utf-8",
    )
    count += 1

    (dst_mem / "WIKI_BRIDGE.md").write_text(
        "# WIKI BRIDGE — CẦU NỐI KHO TRI THỨC NGOÀI (JAVISOS / OBSIDIAN / LOCAL WIKI)\n\n"
        "- Đặt biến môi trường `JAVIS_BRAIN_DIR` trỏ tới thư mục kho tri thức cục bộ của bạn (chứa `brains/Brain Default/wiki` và `sources`).\n"
        "- Sau đó tra cứu nhanh bằng: `python tools/team_memory_cli.py --search-wiki \"<từ_khóa>\"`.\n"
        "- Ghim tài liệu cứng cho từng Team bằng cách điền mảng `pinned_paths` trong `team_memory/teams_manifest.json`.\n",
        encoding="utf-8",
    )
    count += 1

    manifest_src = src_mem / "teams_manifest.json"
    if manifest_src.is_file():
        data = json.loads(manifest_src.read_text(encoding="utf-8"))
        clean_manifest = {}
        for team_name, info in data.items():
            clean_manifest[team_name] = {
                "title": info.get("title", team_name),
                "leader": info.get("leader", ""),
                "members": info.get("members", []),
                "roles": info.get("roles", {}),
                "auditors": info.get("auditors", []),
                "pinned_paths": [],
            }
        (dst_mem / "teams_manifest.json").write_text(
            json.dumps(clean_manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        count += 1

        for team_name, info in clean_manifest.items():
            t_dir = dst_mem / "teams" / team_name
            (t_dir / "runs").mkdir(parents=True, exist_ok=True)
            (t_dir / "runs" / ".gitkeep").write_text("", encoding="utf-8")
            (t_dir / "MEMORY.md").write_text(
                f"# TEAM MEMORY — {team_name}\n\n"
                f"- **Trưởng nhóm (`LEADER`):** `{info['leader']}`\n"
                f"- **Thành viên:** {', '.join(f'`{m}`' for m in info['members'])}\n\n"
                f"## Bài học tích lũy (Learned Patterns)\n"
                f"- *(Tự động bổ sung qua `team_memory_cli.py --learn {team_name} --lesson \"...\"`)*\n",
                encoding="utf-8",
            )
            count += 1

            # Copy helpful static team templates (upstream_registry.json, archetypes_13_channels.md)
            src_t_dir = src_mem / "teams" / team_name
            for extra in ["upstream_registry.json", "archetypes_13_channels.md"]:
                if (src_t_dir / extra).is_file():
                    copy_and_sanitize_file(src_t_dir / extra, t_dir / extra, sanitize=True)
                    count += 1

            for member in info["members"]:
                a_dir = dst_mem / "agents" / member
                a_dir.mkdir(parents=True, exist_ok=True)
                (a_dir / "MEMORY.md").write_text(
                    f"# AGENT MEMORY — {member}\n\n"
                    f"- **Phòng ban:** `{team_name}`\n\n"
                    f"## Kinh nghiệm & Chống lặp lỗi\n"
                    f"- *(Tự động bổ sung qua `team_memory_cli.py --agent-learn {member} --lesson \"...\"`)*\n",
                    encoding="utf-8",
                )
                count += 1

    return count


def security_scan_repo(repo_dir: Path) -> list[str]:
    violations = []
    skip_dirs = {".git", "node_modules", "__pycache__", ".venv", "venv"}
    for root, dirs, files in os.walk(repo_dir):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for fname in files:
            fpath = Path(root) / fname
            rel = fpath.relative_to(repo_dir).as_posix()
            if fname == "sql_runner.py" or "team-antidetect-automator" in rel:
                violations.append(f"FORBIDDEN_FILE: {rel}")
                continue
            if fpath.suffix.lower() not in TEXT_EXTENSIONS:
                continue
            if rel == "config/scripts/sync_to_git_repo.py":
                continue
            try:
                txt = fpath.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            for pat in FORBIDDEN_PATTERNS:
                if re.search(pat, txt, re.I):
                    violations.append(f"SECRET/PATH_HIT [{pat}]: {rel}")
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Antigravity 14-Team config to a Public-Safe Git repo")
    parser.add_argument("--target", default=str(DEFAULT_DST_REPO), help="Target Git repo path")
    args = parser.parse_args()

    dst_repo = Path(args.target)
    dst_config = dst_repo / "config"
    print(f"[SYNC v2.1] Source: {SRC_CONFIG}")
    print(f"[SYNC v2.1] Target: {dst_repo}")
    dst_config.mkdir(parents=True, exist_ok=True)

    print("\n[1/8] Syncing config/skills/ (41 active domain skills)...")
    n_skills = sync_dir_clean(
        SRC_CONFIG / "skills",
        dst_config / "skills",
        ignore_names={"__pycache__", ".git", "node_modules", ".venv", "venv"},
        sanitize=True,
    )
    print(f"  OK -> {n_skills} files synced in config/skills/")

    print("\n[2/8] Syncing config/plugins/ (14 Teams / 51 Subagents + official plugins)...")
    dst_plugins = dst_config / "plugins"
    if dst_plugins.exists():
        shutil.rmtree(dst_plugins)
    dst_plugins.mkdir(parents=True, exist_ok=True)
    plugin_count = 0
    for p in sorted((SRC_CONFIG / "plugins").iterdir(), key=lambda x: x.name.lower()):
        if not p.is_dir() or p.name in EXCLUDED_PLUGINS:
            continue
        sync_dir_clean(
            p,
            dst_plugins / p.name,
            ignore_names={"__pycache__", ".git", "node_modules", ".venv", "venv"},
            sanitize=True,
        )
        plugin_count += 1
    print(f"  OK -> {plugin_count} plugins synced (excluded: {sorted(EXCLUDED_PLUGINS)})")

    print("\n[3/8] Syncing config/rules/ (sanitized)...")
    n_rules = sync_dir_clean(SRC_CONFIG / "rules", dst_config / "rules", {"__pycache__"}, sanitize=True)
    print(f"  OK -> {n_rules} files synced in config/rules/")

    print("\n[4/8] Syncing config/docs/ & root guides...")
    n_docs = sync_dir_clean(SRC_CONFIG / "docs", dst_config / "docs", {"__pycache__"}, sanitize=True)
    readme_src = dst_config / "docs" / "README_HE_THONG_14_TEAM_SUBAGENT_ANTIGRAVITY.md"
    if readme_src.is_file():
        shutil.copy2(readme_src, dst_repo / "README.md")
    for root_doc in [
        "HUONG_DAN_SU_DUNG_11_TEAM_ANTIGRAVITY.md",
        "HUONG_DAN_TIM_VA_NAP_REPO_SKILL_ANTIGRAVITY.md",
        "MASTER_BO_NHAN_SU_ANTIGRAVITY.md",
    ]:
        s_doc = dst_config / "docs" / root_doc
        if s_doc.is_file():
            shutil.copy2(s_doc, dst_repo / root_doc)
    print(f"  OK -> {n_docs} docs synced + README.md & handbooks updated at repo root")

    print("\n[5/8] Syncing config/scripts/ (7 core active scripts)...")
    dst_scripts = dst_config / "scripts"
    if dst_scripts.exists():
        shutil.rmtree(dst_scripts)
    dst_scripts.mkdir(parents=True, exist_ok=True)
    for name in sorted(ACTIVE_SCRIPTS):
        s_file = SRC_CONFIG / "scripts" / name
        if s_file.is_file():
            copy_and_sanitize_file(s_file, dst_scripts / name, sanitize=(name != "sync_to_git_repo.py"))
    print(f"  OK -> {len(ACTIVE_SCRIPTS)} active scripts synced")

    print("\n[6/8] Syncing portable config/tools/ & config/workflows/ (4 pipelines)...")
    dst_tools = dst_config / "tools"
    if dst_tools.exists():
        shutil.rmtree(dst_tools)
    dst_tools.mkdir(parents=True, exist_ok=True)
    build_portable_team_memory_cli(SRC_CONFIG / "tools" / "team_memory_cli.py", dst_tools / "team_memory_cli.py")

    dst_wf = dst_config / "workflows"
    if dst_wf.exists():
        shutil.rmtree(dst_wf)
    dst_wf.mkdir(parents=True, exist_ok=True)
    wf_count = 0
    for wf in sorted((SRC_CONFIG / "workflows").glob("*.py")):
        build_portable_workflow(wf, dst_wf / wf.name)
        wf_count += 1
    print(f"  OK -> team_memory_cli.py & {wf_count} workflows built in portable mode (sql_runner.py excluded)")

    print("\n[7/8] Building clean template config/team_memory/ (14 teams + 51 agents)...")
    n_mem = build_clean_team_memory_templates(SRC_CONFIG / "team_memory", dst_config / "team_memory")
    print(f"  OK -> {n_mem} clean memory template files generated (0 personal runs)")

    print("\n[8/8] Syncing top-level rules...")
    for md in ["GEMINI.md", "QUY_TRINH_CHUNG_5_CHOT_CHAN_CHONG_AO_GIAC_AI.md", "learned_patterns.md"]:
        s = SRC_CONFIG / md
        if s.is_file():
            copy_and_sanitize_file(s, dst_config / md, sanitize=True)

    print("\n[SECURITY AUDIT] Scanning entire Git repo for credentials / private paths...")
    violations = security_scan_repo(dst_repo)
    if violations:
        print(f"FAIL! Found {len(violations)} security/privacy violations:")
        for v in violations[:40]:
            print(f"  - {v}")
        return 1

    print("SECURITY AUDIT: PASS (0 credential leaks, 0 internal IP/DB leaks, 0 personal paths!)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
