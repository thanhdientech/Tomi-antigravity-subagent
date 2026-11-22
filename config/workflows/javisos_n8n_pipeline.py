"""
Workflow 4 Pha — Build, Training Chống Bịa Đặt, Workflow n8n & Deploy Dual-JavisOS (`team-javisos-n8n`).
Vòng đời khép kín có QA 4 tầng & Auto-Retry 1 vòng:
  Phase 1 (plan)   : javis-architect-builder khóa rõ mục tiêu (Tomi :7777 | InfoAsia :7778 | Javis mới | n8n :5678/:5679)
  Phase 2 (build)  : Giao đúng chuyên gia (javis-architect-builder / javis-anti-hallucination-trainer / n8n-workflow-engineer)
  Phase 3 (qa_4t)  : javis-n8n-qa-auditor kiểm toán Độc Lập 4 Tầng (HTTP 200/Docker + Logo/Name/Brain + 5 câu test chống bịa + n8n/UI ảnh)
  Phase 4 (retry)  : Nếu FAIL -> Tự trả lỗi về Worker sửa 1 vòng rồi tái kiểm toán; PASS -> xuất Scorecard A-F

Chạy bằng `run_workflow` với Args:
  {
    "target_instance": "infoasia" | "tomi" | "both" | "new_javis" | "n8n_5678" | "n8n_5679",
    "mode": "build_or_edit_javis" | "train_anti_hallucination" | "n8n_workflow" | "deploy_server29",
    "task": "Mô tả chi tiết yêu cầu chỉnh sửa, đào tạo, tạo workflow n8n hoặc deploy"
  }
"""

target_instance = args.get("target_instance", "")
mode = args.get("mode", "build_or_edit_javis")
task = args.get("task", "")

if not target_instance or not task:
    raise ValueError("Bắt buộc truyền args['target_instance'] (infoasia|tomi|both|new_javis|n8n_5678|n8n_5679) và args['task'].")

phase(f"1. Khóa Phạm Vi & Cách Ly Instance ({target_instance} / {mode})")
plan = await agent(
    type="javis-architect-builder",
    role="JavisOS & n8n Architect (Team 15 LEADER)",
    prompt=(
        f"Mục tiêu: {task}\nInstance: {target_instance}\nChế độ: {mode}\n"
        "Đọc instances_dual_javis_n8n.md và hồ sơ liên quan trong %JAVIS_BRAIN_DIR%. "
        "Khóa rõ đường dẫn file/brain/port/branding được phép đụng (TUYỆT ĐỐI cách ly Tomi :7777 với InfoAsia :7778) "
        "và chốt danh sách tiêu chí QA 4 tầng."
    ),
)

if mode == "train_anti_hallucination":
    phase("2. Đào Tạo AI Agent & Khóa Chống Bịa Đặt (javis-anti-hallucination-trainer)")
    work_out = await agent(
        type="javis-anti-hallucination-trainer",
        role="Anti-Hallucination Trainer (Team 15)",
        prompt=(
            f"Instance: {target_instance}\nKế hoạch từ LEADER:\n{plan}\n\n"
            "Thực hiện đào tạo / nạp tri thức đúng Brain (brains_infoasia cho InfoAsia, brains cho Tomi), "
            "nhồi đủ 5 Chốt Chặn chống bịa đặt, cập nhật index.md/log.md/security_guard nếu cần, "
            "và BẮT BUỘC xuất kèm Bộ 5 Câu Hỏi Test Chống Bịa (3 câu thật + 2 câu bẫy)."
        ),
    )
    fixer = "javis-anti-hallucination-trainer"
elif mode == "n8n_workflow":
    phase("2. Thiết Kế & Triển Khai Workflow n8n (n8n-workflow-engineer)")
    work_out = await agent(
        type="n8n-workflow-engineer",
        role="n8n Workflow Engineer (Team 15)",
        prompt=(
            f"Cụm n8n đích: {target_instance}\nKế hoạch từ LEADER:\n{plan}\n\n"
            "Thiết kế / sửa / export Workflow n8n JSON hợp lệ (0 hardcode API key/password, có Error Handler & Retry), "
            "nối đúng endpoint JavisOS/SAP/ERPNext nếu cần và chuẩn bị payload test webhook."
        ),
    )
    fixer = "n8n-workflow-engineer"
else:
    phase(f"2. Chỉnh Sửa / Build / Deploy JavisOS ({mode})")
    work_out = await agent(
        type="javis-architect-builder",
        role="JavisOS Builder & Deployer (Team 15)",
        prompt=(
            f"Instance: {target_instance} | Mode: {mode}\nKế hoạch:\n{plan}\n\n"
            "Backup trước khi sửa, thực thi thay đổi tại %JAVIS_BRAIN_DIR% (giữ nguyên Logo/Name Tomi vs InfoAsia), "
            "kiểm tra cú pháp local Exit 0; nếu mode=deploy_server29 thì deploy an toàn qua update-javis-safe.sh / restart-both-javis.sh."
        ),
    )
    fixer = "javis-architect-builder"

phase("3. Kiểm Toán QA Độc Lập 4 Tầng (javis-n8n-qa-auditor)")
qa_out = await agent(
    type="javis-n8n-qa-auditor",
    role="JavisOS & n8n QA Auditor (Team 15 AUDITOR)",
    prompt=(
        f"Kiểm toán Độc Lập 4 Tầng cho {target_instance} ({mode}):\n{work_out}\n\n"
        "1) Kiểm tra HTTP 200 / Docker / cú pháp code/JSON.\n"
        "2) Kiểm tra đúng Logo + Name (Tomi :7777 vs InfoAsia :7778) & 0 rò dữ liệu Brain (chụp & đọc ảnh UI bằng read_file nếu đụng UI/deploy).\n"
        "3) Chạy Bộ 5 Câu Test Chống Bịa Đặt (nếu mode=train_anti_hallucination hoặc sửa prompt Agent).\n"
        "4) Kiểm tra n8n execution & 0 hardcode secret (nếu đụng n8n).\n"
        "Trả [STATUS: PASS] hoặc [STATUS: FAIL] kèm Scorecard iFixAi A-F."
    ),
)

if "STATUS: FAIL" in str(qa_out).upper():
    phase("4. Auto-Retry 1 Vòng Sửa Lỗi & Tái Kiểm Toán")
    fix_out = await agent(
        type=fixer,
        role=f"Team 15 Auto-Fixer ({fixer})",
        prompt=f"Sửa triệt để các lỗi QA 4 tầng vừa phát hiện:\n{qa_out}",
    )
    qa_out = await agent(
        type="javis-n8n-qa-auditor",
        role="JavisOS & n8n Re-QA Auditor (Team 15 AUDITOR)",
        prompt=f"Tái kiểm toán 4 tầng sau khi sửa:\n{fix_out}\nChỉ PASS khi đạt sạch 100% và ký Scorecard A/B.",
    )

result({"plan": plan, "work": work_out, "qa": qa_out})
