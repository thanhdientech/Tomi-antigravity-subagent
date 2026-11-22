"""
Javis-Grade Team Runner cho 11 Team Antigravity (`run_workflow`).
Tái hiện đúng vòng đời 4 bước + Cổng QA + Auto-Retry + Long Memory của JavisOS (`team_runner.py`):
  Phase 1 (plan)       : Đọc MEMORY.md + Javis Wiki Bridge -> Trưởng nhóm lập kế hoạch & tiêu chí QA
  Phase 2 (work)       : Giao thành viên chuyên trách trong Team thực thi (có thể chạy song song)
  Phase 3 (verify)     : Cổng QA độc lập (qa-code-tester + qa-visual-human-tester + Auditor chuyên ngành)
                         Nếu FAIL -> Auto-Retry đúng 1 vòng sửa lỗi gốc rồi kiểm chứng lại
  Phase 4 (synthesize) : qa-ifixai-auditor ký Scorecard A-F -> Ghi nhật ký `runs/` & bài học `MEMORY.md`

Chạy bằng công cụ `run_workflow` với Args:
  {
    "team": "team-web-wordpress-seo" | "team-sap-b1-sql" | ...,
    "goal": "Mục tiêu công việc cần thực hiện",
    "worker": "(Tùy chọn) Tên subagent thực thi chính — mặc định lấy Leader của Team",
    "test_url": "(Tùy chọn) URL web/app cần qa-visual-human-tester dùng thử chụp & đọc ảnh",
    "wiki_query": "(Tùy chọn) Từ khóa tra cứu thêm trong kho JavisOS wiki/ & sources/"
  }
"""

import json
from pathlib import Path

import sys
CONFIG_ROOT = Path.home() / ".gemini" / "config"
MANIFEST_PATH = CONFIG_ROOT / "team_memory" / "teams_manifest.json"
PY = sys.executable
MEM_CLI = str(CONFIG_ROOT / "tools" / "team_memory_cli.py")

TEAM_AUDITORS = {
    "team-web-wordpress-seo": "web-performance-auditor",
    "team-design-creative": "design-ux-cro-auditor",
    "team-video-editing-motion": "video-qa-verifier",
    "team-server-vps-hosting": "infra-qa-security-verifier",
    "team-web-research": "web-fact-checker",
    "team-sap-b1-sql": "sap-accounting-auditor",
    "team-reverse-security": "sec-vulnerability-auditor",
    "team-youtube-factory": "yt-production-qa",
    "team-skill-curator": "skill-security-qa",
    "team-short-video-affiliate": "short-video-qa-auditor",
    "team-javisos-n8n": "javis-n8n-qa-auditor",
}

team = args.get("team", "")
goal = args.get("goal", "")
test_url = args.get("test_url", "")
wiki_query = args.get("wiki_query", "")

if not team or not goal:
    raise ValueError("Bắt buộc truyền args['team'] và args['goal']")

manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
if team not in manifest:
    raise ValueError(f"Team '{team}' không hợp lệ. Các team hợp lệ: {list(manifest.keys())}")

tinfo = manifest[team]
leader = tinfo["leader"]
worker_name = args.get("worker") or leader
domain_auditor = TEAM_AUDITORS.get(team)
pinned_docs = tinfo.get("pinned_paths", [])

phase(f"1. Plan & Load Memory/Javis Wiki ({team})")
plan = await agent(
    prompt=(
        f"Bạn là Trưởng điều phối lập kế hoạch cho {tinfo['title']} (`{team}`).\n"
        f"Mục tiêu: {goal}\n\n"
        f"BẮT BUỘC TRƯỚC KHI LẬP KẾ HOẠCH:\n"
        f"1. Chạy lệnh đọc bộ nhớ nhóm: `& \"{PY}\" \"{MEM_CLI}\" --read {team}`\n"
        f"2. Nếu có từ khóa '{wiki_query}', chạy: `& \"{PY}\" \"{MEM_CLI}\" --search-wiki \"{wiki_query}\"`\n"
        f"3. Tài liệu nguồn Javis ghim cứng cho nhóm này: {pinned_docs}\n\n"
        f"Xuất kế hoạch JSON gồm danh sách bước nhỏ (atomic_steps), rủi ro cần tránh, và tiêu chí QA bắt buộc."
    ),
    type_name="orchestrator-planner",
    role=f"Planner ({team})",
    schema={
        "type": "object",
        "properties": {
            "wiki_refs_used": {"type": "array", "items": {"type": "string"}},
            "atomic_steps": {"type": "array", "items": {"type": "string"}},
            "acceptance_criteria": {"type": "array", "items": {"type": "string"}},
            "risk_notes": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["atomic_steps", "acceptance_criteria", "risk_notes"],
    },
)
log("Plan steps:", len(plan.get("atomic_steps", [])))

phase(f"2. Execute Work ({worker_name})")
worker = agent(
    prompt=(
        f"Bạn là thành viên `{worker_name}` thuộc {tinfo['title']}. "
        f"Luôn tuân thủ quy chuẩn môi trường INFOASIA (Python313: {PY}) và đọc tài liệu ghim cứng khi cần."
    ),
    type_name=worker_name,
    role=f"Worker ({worker_name})",
)
work_report = await worker(
    f"Thực thi mục tiêu: {goal}\n"
    f"Kế hoạch đã khóa:\n{json.dumps(plan, ensure_ascii=False)}\n"
    f"Tài liệu Javis ghim cứng: {pinned_docs}\n"
    f"Trả về tóm tắt thay đổi, đường dẫn file/URL tạo hoặc sửa, và bằng chứng tự kiểm tra sơ bộ.",
    schema={"type": "string"},
)
log("Initial work completed by:", worker_name)


async def run_verify_gate(round_idx: int, latest_work: str):
    phase(f"3.{round_idx} Verify Gate (QA Code + Visual Human + Domain Auditor)")
    qa_schema = {
        "type": "object",
        "properties": {
            "passed": {"type": "boolean"},
            "evidence": {"type": "string"},
            "bugs": {"type": "array", "items": {"type": "string"}},
            "new_lesson": {"type": "string"},
        },
        "required": ["passed", "evidence", "bugs"],
    }
    checks = [
        {
            "key": "qa_code",
            "type_name": "qa-code-tester",
            "role": f"QA Code Tester R{round_idx}",
            "prompt": (
                f"Kiểm thử kỹ thuật ĐỘC LẬP (KHÔNG sửa code) cho mục tiêu '{goal}' ({team}).\n"
                f"Tiêu chí: {plan['acceptance_criteria']}\nBáo cáo Worker: {latest_work}\n"
                f"Chạy lệnh kiểm chứng thật thu Exit code 0 + output thực tế."
            ),
        }
    ]
    if test_url:
        checks.append(
            {
                "key": "qa_visual",
                "type_name": "qa-visual-human-tester",
                "role": f"QA Visual Human R{round_idx}",
                "prompt": (
                    f"Dùng thử giao diện NHƯ NGƯỜI THẬT tại URL: {test_url}\n"
                    f"Mục tiêu: {goal}\nTiêu chí: {plan['acceptance_criteria']}\n"
                    f"Tương tác thật, CHỤP ẢNH và DÙNG read_file ĐỌC LẠI CHÍNH ẢNH VỪA CHỤP để soi lỗi."
                ),
            }
        )
    if domain_auditor and domain_auditor != worker_name:
        checks.append(
            {
                "key": "domain_audit",
                "type_name": domain_auditor,
                "role": f"{domain_auditor} R{round_idx}",
                "prompt": (
                    f"Kiểm toán chuyên ngành ĐỘC LẬP cho {team} (KHÔNG sửa file).\n"
                    f"Mục tiêu: {goal}\nBáo cáo Worker: {latest_work}\n"
                    f"Kiểm tra đúng chuẩn chuyên môn của {team} và trả về kết quả thực tế."
                ),
            }
        )

    res = await parallel(
        checks,
        lambda c: agent(c["prompt"], schema=qa_schema, role=c["role"], type_name=c["type_name"]),
    )
    return {checks[i]["key"]: res[i] for i in range(len(checks))}


qa_out = await run_verify_gate(1, work_report)
if not all(v.get("passed") for v in qa_out.values()):
    phase(f"3.5 Auto-Retry Remediation ({worker_name})")
    work_report = await worker(
        f"Cổng QA vòng 1 báo lỗi:\n{json.dumps(qa_out, ensure_ascii=False)}\n"
        f"Hãy sửa dứt điểm nguyên nhân gốc toàn bộ lỗi trên rồi báo lại thay đổi.",
        schema={"type": "string"},
    )
    qa_out = await run_verify_gate(2, work_report)

del worker

phase("4. Synthesize, iFixAi Scorecard & Save Long Memory")
final_audit = await agent(
    prompt=(
        f"Kiểm toán tổng kết iFixAi 5 trụ cột cho {team} — mục tiêu: {goal}\n"
        f"- Kế hoạch: {plan}\n"
        f"- Kết quả thực thi: {work_report}\n"
        f"- Kết quả QA Gate: {qa_out}\n\n"
        f"Sau khi chấm Scorecard, hãy chạy lệnh ghi nhật ký vào bộ nhớ dài hạn nhóm:\n"
        f"`& \"{PY}\" \"{MEM_CLI}\" --log-run {team} --agent {worker_name} --task \"<ten ngan>\" --status <PASS|FAIL> --summary \"<tom tat>\" --evidence \"<bang chung>\"`\n"
        f"Nếu có bài học mới đáng nhớ, chạy thêm `--learn {team} --lesson \"<bai hoc>\"`."
    ),
    type_name="qa-ifixai-auditor",
    role=f"iFixAi Auditor & Memory Saver ({team})",
    schema={
        "type": "object",
        "properties": {
            "approved": {"type": "boolean"},
            "grade": {"type": "string"},
            "score": {"type": "integer"},
            "scorecard": {"type": "string"},
            "memory_logged": {"type": "boolean"},
        },
        "required": ["approved", "grade", "score", "scorecard", "memory_logged"],
    },
)
log("Final Audit:", final_audit.get("grade"), final_audit.get("score"))

{"team": team, "worker": worker_name, "plan": plan, "qa": qa_out, "audit": final_audit}
