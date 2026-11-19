"""
Workflow mẫu Team 0: Interview (Grill-Me) -> Architecture & Options -> Spec Validation (Exit 0).
Args:
  {
    "idea": "Ý tưởng dự án hoặc chức năng mới",
    "workspace_hint": "(Tùy chọn) Thư mục dự án hiện có để khảo sát trước",
    "blueprint_path": "(Tùy chọn) Đường dẫn lưu file BLUEPRINT_<TEN>.md"
  }
"""

idea = args.get("idea", "")
workspace_hint = args.get("workspace_hint", "")
blueprint_path = args.get("blueprint_path", "")

if not idea:
    raise ValueError("Thiếu tham số bắt buộc: args['idea']")

phase("1. Context Survey & Grill-Me Discovery")
discovery = await agent(
    prompt=(
        f"Khảo sát ngữ cảnh (workspace: {workspace_hint}) và phân tích điểm mù theo Chốt 1A/1B cho yêu cầu:\n{idea}\n"
        f"Trả về JSON gồm rủi ro logic, dữ kiện thiếu bắt buộc và tối đa 5-7 câu hỏi Grill-Me kèm đề xuất Khuyên dùng."
    ),
    type_name="blueprint-interviewer",
    role="Blueprint Interviewer (Grill-Me)",
    schema={
        "type": "object",
        "properties": {
            "existing_context": {"type": "string"},
            "risk_warnings": {"type": "array", "items": {"type": "string"}},
            "missing_hard_facts": {"type": "array", "items": {"type": "string"}},
            "decision_questions": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["existing_context", "risk_warnings", "missing_hard_facts", "decision_questions"],
    },
)

phase("2. Solution Architecture & Options Table")
arch = await agent(
    prompt=(
        f"Thiết kế kiến trúc, khóa In-Scope/Out-of-Scope, lập Bảng So Sánh Phương Án [1] Recommended / [2] / [3] "
        f"và ánh xạ đúng các Team (0..10) & Skills thực tế cho:\n{idea}\n"
        f"Kết quả khảo sát:\n{discovery}"
    ),
    type_name="solution-architect",
    role="Solution Architect",
    schema={
        "type": "object",
        "properties": {
            "in_scope": {"type": "array", "items": {"type": "string"}},
            "out_of_scope": {"type": "array", "items": {"type": "string"}},
            "options_table_md": {"type": "string"},
            "mapped_teams_and_skills": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["in_scope", "out_of_scope", "options_table_md", "mapped_teams_and_skills"],
    },
)

phase("3. Draft & Validate Master Blueprint")
spec = await agent(
    prompt=(
        f"Tổng hợp Master Blueprint (lưu tại '{blueprint_path}' nếu có) không chứa TBD/TODO và chạy kiểm định "
        f"validate_blueprint.py bằng Python313.\n- Ý tưởng: {idea}\n- Khảo sát: {discovery}\n- Kiến trúc: {arch}"
    ),
    type_name="blueprint-spec-validator",
    role="Blueprint Spec Validator",
    schema={
        "type": "object",
        "properties": {
            "blueprint_file": {"type": "string"},
            "validation_passed": {"type": "boolean"},
            "ready_for_user_approval": {"type": "boolean"},
            "summary": {"type": "string"},
        },
        "required": ["validation_passed", "ready_for_user_approval", "summary"],
    },
)

{"discovery": discovery, "architecture": arch, "spec": spec}
