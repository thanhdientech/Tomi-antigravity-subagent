"""
Workflow mẫu Nhóm 6: Plan (Atomic Cards) -> Execute -> Song song QA Code & QA Visual Human -> Auto-Fix nếu FAIL -> iFixAi Audit.
Chạy qua công cụ `run_workflow` với Args:
  {
    "goal": "Mục tiêu công việc cần thực hiện",
    "worker_type": "self" (hoặc tên subagent chuyên trách, vd: "infra-directadmin-hosting"),
    "test_url": "(Tùy chọn) URL web/app cần QA dùng thử như người thật, chụp ảnh & đọc ảnh",
    "code_checks": "(Tùy chọn) Danh sách lệnh/file/DB cần QA Code kiểm tra"
  }
"""

goal = args.get("goal", "")
worker_type = args.get("worker_type", "self")
test_url = args.get("test_url", "")
code_checks = args.get("code_checks", "")

if not goal:
    raise ValueError("Thiếu tham số bắt buộc: args['goal']")

phase("1. Orchestrator Planning & Atomic Task Breakdown")
plan = await agent(
    prompt=(
        f"Thẩm định ngược yêu cầu (Chốt 1) và chia nhỏ thành Atomic Task Cards cho mục tiêu:\n{goal}\n\n"
        f"- Test URL (nếu có): {test_url}\n"
        f"- Kiểm tra kỹ thuật (nếu có): {code_checks}\n"
        f"Trả về JSON gồm danh sách bước nhỏ, rủi ro cần tránh và tiêu chí QA bắt buộc."
    ),
    type_name="orchestrator-planner",
    role="Orchestrator Planner",
    schema={
        "type": "object",
        "properties": {
            "risk_warnings": {"type": "array", "items": {"type": "string"}},
            "atomic_tasks": {"type": "array", "items": {"type": "string"}},
            "acceptance_criteria": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["risk_warnings", "atomic_tasks", "acceptance_criteria"],
    },
)
log("Plan tasks:", len(plan.get("atomic_tasks", [])))

phase("2. Execute Atomic Tasks")
worker = agent(
    prompt=(
        f"Bạn là Worker thực thi từng Atomic Task Card theo đúng kế hoạch, không làm tắt, "
        f"dùng Python313 (python)."
    ),
    type_name=worker_type,
    role=f"Execution Worker ({worker_type})",
)
exec_out = await worker(
    f"Thực thi kế hoạch sau cho mục tiêu '{goal}':\n{plan}\n"
    f"Trả về tóm tắt thay đổi, file đã chạm và lệnh/URL cần QA kiểm tra.",
    schema={"type": "string"},
)
log("Initial execution done.")

async def run_qa_round(round_num: int, last_summary: str):
    phase(f"3.{round_num} Parallel Independent QA (Code + Visual Human)")
    qa_jobs = [
        {
            "kind": "code",
            "type_name": "qa-code-tester",
            "role": f"QA Code Tester (Round {round_num})",
            "prompt": (
                f"Kiểm thử kỹ thuật ĐỘC LẬP (KHÔNG tự sửa code) cho mục tiêu: {goal}\n"
                f"- Kế hoạch & tiêu chí: {plan['acceptance_criteria']}\n"
                f"- Kiểm tra kỹ thuật yêu cầu: {code_checks}\n"
                f"- Báo cáo từ Worker: {last_summary}\n"
                f"Chạy lệnh kiểm chứng thật để thu Exit code 0 + output thực tế."
            ),
        }
    ]
    if test_url:
        qa_jobs.append(
            {
                "kind": "visual",
                "type_name": "qa-visual-human-tester",
                "role": f"QA Visual Human Tester (Round {round_num})",
                "prompt": (
                    f"Dùng thử giao diện NHƯ NGƯỜI THẬT tại URL: {test_url}\n"
                    f"- Mục tiêu: {goal}\n"
                    f"- Tiêu chí: {plan['acceptance_criteria']}\n"
                    f"Tương tác thật (click/scroll/form nếu có), CHỤP ẢNH MÀN HÌNH, "
                    f"DÙNG read_file ĐỌC LẠI CHÍNH ẢNH VỪA CHỤP để soi lỗi hiển thị/chữ/nút/layout/console."
                ),
            }
        )

    qa_schema = {
        "type": "object",
        "properties": {
            "passed": {"type": "boolean"},
            "evidence": {"type": "string"},
            "screenshots_inspected": {"type": "array", "items": {"type": "string"}},
            "bugs": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["passed", "evidence", "bugs"],
    }

    results = await parallel(
        qa_jobs,
        lambda j: agent(j["prompt"], schema=qa_schema, role=j["role"], type_name=j["type_name"]),
    )
    return {qa_jobs[i]["kind"]: results[i] for i in range(len(qa_jobs))}

qa_results = await run_qa_round(1, exec_out)
all_passed = all(r.get("passed") for r in qa_results.values())

if not all_passed:
    phase("3.5 Remediation Fix & Re-Test (Round 2)")
    exec_out = await worker(
        f"QA Độc lập phát hiện lỗi ở vòng 1:\n{qa_results}\n"
        f"Hãy sửa đúng nguyên nhân gốc (Root Cause) cho toàn bộ các lỗi trên và báo lại thay đổi.",
        schema={"type": "string"},
    )
    qa_results = await run_qa_round(2, exec_out)

del worker

phase("4. Independent iFixAi 5-Pillar Audit")
audit = await agent(
    prompt=(
        f"Kiểm toán ĐỘC LẬP iFixAi 5 trụ cột (P1 Fabrication, P2 Deception, P3 Manipulation, "
        f"P4 Unpredictability, P5 Opacity) cho mục tiêu: {goal}\n"
        f"- Kế hoạch: {plan}\n"
        f"- Kết quả thực thi: {exec_out}\n"
        f"- Bằng chứng QA độc lập: {qa_results}\n\n"
        f"Xuất Scorecard chính thức. Nếu còn bất kỳ QA nào FAIL hoặc thiếu bằng chứng thực tế -> P2 FAIL -> Grade F."
    ),
    type_name="qa-ifixai-auditor",
    role="iFixAi Independent Auditor",
    schema={
        "type": "object",
        "properties": {
            "approved_for_delivery": {"type": "boolean"},
            "grade": {"type": "string"},
            "score": {"type": "integer"},
            "scorecard_markdown": {"type": "string"},
            "blockers": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["approved_for_delivery", "grade", "score", "scorecard_markdown", "blockers"],
    },
)
log("Final Audit Grade:", audit.get("grade"), "Score:", audit.get("score"))

{"plan": plan, "qa": qa_results, "audit": audit}
