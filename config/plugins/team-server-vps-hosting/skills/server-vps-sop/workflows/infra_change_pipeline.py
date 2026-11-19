"""
Workflow mẫu Nhóm 4: Thực thi hạ tầng -> Kiểm chứng QA/Bảo mật độc lập.
Chạy qua công cụ `run_workflow` với Args:
  {
    "worker_type": "infra-linux-vps" | "infra-windows-server" | "infra-directadmin-hosting",
    "task": "Mô tả tác vụ hạ tầng cần thực hiện",
    "verify_target": "URL, dịch vụ, port hoặc đường dẫn cần QA kiểm chứng sau khi làm"
  }
"""

worker_type = args.get("worker_type", "infra-linux-vps")
task = args.get("task", "")
verify_target = args.get("verify_target", "")

if not task:
    raise ValueError("Thiếu tham số bắt buộc: args['task']")

phase("1. Execute Infrastructure Task")
exec_result = await agent(
    prompt=(
        f"Thực hiện tác vụ hạ tầng sau đúng SOP (Inspect -> Backup -> Apply):\n"
        f"{task}\n\n"
        f"Trả về kết quả JSON theo schema gồm các bước đã làm, file backup đã tạo và lệnh cần kiểm chứng."
    ),
    type_name=worker_type,
    role=f"Infra Executor ({worker_type})",
    schema={
        "type": "object",
        "properties": {
            "status": {"type": "string"},
            "backups_created": {"type": "array", "items": {"type": "string"}},
            "changes_summary": {"type": "string"},
            "verification_hints": {"type": "string"},
        },
        "required": ["status", "backups_created", "changes_summary"],
    },
)
log("Executor result:", exec_result)

phase("2. Independent QA & Security Verification")
qa_result = await agent(
    prompt=(
        f"Kiểm chứng ĐỘC LẬP kết quả thực thi hạ tầng.\n"
        f"- Tác vụ gốc: {task}\n"
        f"- Mục tiêu kiểm chứng: {verify_target}\n"
        f"- Báo cáo từ Executor: {exec_result}\n\n"
        f"Chạy lệnh kiểm chứng thực tế (HTTP 200 / DB Connected / Service status / Backup tồn tại / không lộ secret). "
        f"Chấm Scorecard iFixAi (Grade A/B mới đặt passed=true)."
    ),
    type_name="infra-qa-security-verifier",
    role="Independent Infra QA Verifier",
    schema={
        "type": "object",
        "properties": {
            "passed": {"type": "boolean"},
            "grade": {"type": "string"},
            "evidence": {"type": "string"},
            "issues_found": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["passed", "grade", "evidence", "issues_found"],
    },
)
log("QA Verifier result:", qa_result)

{"execution": exec_result, "qa": qa_result}
