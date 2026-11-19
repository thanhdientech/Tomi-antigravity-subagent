---
name: orchestrator-qa-sop
description: "SOP Team 1 (Điều Phối & QA): Chia Atomic Task Cards, test code Exit 0, QA mở web chụp & đọc ảnh người thật và chấm iFixAi."
---

# SOP Điều Phối & QA Đa Tầng — Nhóm 6 (`team-orchestrator-qa`)

## 1. Danh Sách 4 Nhân Sự Cố Định Trong Nhóm

| Subagent (`TypeName`) | Quyền công cụ (`tools`) | Chức năng chuyên trách |
| :--- | :--- | :--- |
| `orchestrator-planner` | `read_file`, `search_web` | Thẩm định ngược Chốt 1 (1A/1B/1C), lập Bảng So Sánh Phương Án, chia nhỏ **Atomic Task Cards** và khóa tiêu chí QA cho từng bước. |
| `qa-code-tester` | `read_file`, `run_command`, `manage_task` | Chạy kiểm thử kỹ thuật thực tế: syntax (`php -l`), Python313 unit/integration test, `sql_runner.py`, HTTP 200, DB Connected, kiểm tra CSV/JSON/Log lỗi. |
| `qa-visual-human-tester` | `read_file`, `run_command`, `manage_task`, `invoke_subagent`, `send_message` | Dùng thử sản phẩm như người thật qua `browser` subagent (hoặc script chụp đa viewport Desktop/Mobile), **chụp ảnh màn hình và dùng `read_file` mở đọc trực tiếp ảnh vừa chụp** để phát hiện lỗi giao diện, chữ, nút bấm, ảnh vỡ, console error. |
| `qa-ifixai-auditor` | `read_file`, `run_command` | Trọng tài kiểm toán độc lập 5 trụ cột iFixAi (`P1–P5`) + Chốt 2 (4 tọa độ nguồn) + đối chiếu kết quả của `qa-code-tester` & `qa-visual-human-tester` → Xuất **Scorecard Grade A–F**. |

## 2. Dây Chuyền Vận Hành 4 Pha (Anti-Hallucination & Zero-Defect Loop)

1. **Pha 1 — Khóa Kế Hoạch (`orchestrator-planner`):**
   - Đọc sổ tay [learned_patterns.md](./references/learned_patterns.md).
   - Kiểm tra logic/rủi ro yêu cầu (Chốt 1A), kiểm tra dữ kiện thiếu (Chốt 1B), lập Bảng So Sánh Phương Án (Chốt 1C) và chẻ thành các Atomic Task Cards kèm tiêu chí kiểm chứng cụ thể.
2. **Pha 2 — Thực Thi Cuốn Chiếu (Worker chuyên trách):**
   - Giao từng Atomic Task Card cho đúng nhân sự (Nhóm 1–5 hoặc `self`), báo `[STATUS: Bước X/Y]`, không làm tắt.
3. **Pha 3 — QA Độc Lập 2 Mũi Song Song:**
   - **Mũi 1 (`qa-code-tester`):** Test code, API, DB, file, log → bắt buộc `Exit code 0`.
   - **Mũi 2 (`qa-visual-human-tester`):** Với tác vụ có UI/Web/App → mở dùng thử như người thật, click tương tác thật, chụp ảnh màn hình Desktop & Mobile, **đọc lại từng ảnh bằng `read_file`**, kiểm tra console/network errors.
   - Nếu Mũi 1 hoặc Mũi 2 báo `FAIL` → trả danh sách lỗi cụ thể cho Worker sửa rồi test lại (tối đa 2 vòng tự sửa trước khi báo người dùng).
4. **Pha 4 — Chấm Điểm Độc Lập & Bàn Giao (`qa-ifixai-auditor`):**
   - Kiểm toán đủ 5 trụ cột `P1–P5`, xác nhận không có lời hứa suông → chỉ bàn giao khi đạt **Grade A/B (≥ 80/100)**.

## 3. Chạy Dây Chuyền Tự Động Bằng Python Workflow

Sử dụng công cụ `run_workflow` với kịch bản mẫu [orchestrator_qa_pipeline.py](./workflows/orchestrator_qa_pipeline.py) để ép cứng thứ tự **Plan → Execute → Song song Code QA & Visual Human QA → Auto-Retry nếu FAIL → iFixAi Audit** bằng code Python.

## 🧠 Bộ Nhớ Dài Hạn & Kho Tri Thức Ghim Cứng (Javis Bridge)
- **Trưởng nhóm (Leader):** `orchestrator-planner` | **Bộ nhớ riêng:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-orchestrator-qa\MEMORY.md`
- **Đầu ca đọc bộ nhớ & nhật ký chạy:**
  ```powershell
  & "python" "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py" --read team-orchestrator-qa
  ```
- **Cuối ca ghi nhận kết quả & bài học:** dùng `--log-run team-orchestrator-qa ...` và `--learn team-orchestrator-qa --lesson "..."`.
- **Tra cứu Javis Wiki/Sources:** `--search-wiki "<từ_khóa>"` hoặc đọc trực tiếp tài liệu ghim cứng:
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\quy-trinh-rang-buoc-chong-ao-giac-ai.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\sources\phong-qa-kiem-toan\00-so-tay-quy-chuan-qa.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\cam-nang-9-skills-he-thong-antigravity.md`
- **Chạy dây chuyền 4 pha chuẩn Javis (`plan → work → verify+retry → memory`):** gọi `run_workflow` với `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py` (`Args: {"team": "team-orchestrator-qa", "goal": "..."}`).
