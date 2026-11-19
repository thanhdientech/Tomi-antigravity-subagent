---
name: planning-blueprint-sop
description: "SOP Team 0 (Blueprint): Phỏng vấn Grill-Me, lập Bảng Phương Án, viết Master Blueprint 0 TBD và kiểm định validate_blueprint.py."
---

# SOP Team 0 — Cổng Lên Kế Hoạch & Chốt Đặc Tả (`team-planning-blueprint`)

## 1. Nhân Sự Cố Định Trong Team 0

| Subagent (`TypeName`) | Nhiệm vụ cốt lõi |
| :--- | :--- |
| `blueprint-interviewer` | Khảo sát ngữ cảnh workspace có sẵn, thẩm định ngược Chốt 1A/1B, phỏng vấn `Grill-Me` (gom 5–7 câu hỏi cốt lõi kèm `[⭐ Khuyên dùng]`). |
| `solution-architect` | Chốt Tech Stack, khóa `In-Scope / Out-of-Scope`, lập Bảng So Sánh Phương Án `[1]⭐/[2]/[3]`, ánh xạ đúng các Phòng Ban (Team 1–10) & Skills thực tế trên máy. |
| `blueprint-spec-validator` | Biên soạn & kiểm định 1 file `BLUEPRINT_<TEN_DU_AN>.md` duy nhất, chạy `validate_blueprint.py` / `converge_blueprint.py` bằng Python313 đạt `Exit code 0`, trình người dùng ký chốt. |

## 2. Dây Chuyền 3 Bước
1. Đọc skill gốc `%USERPROFILE%\.gemini\config\skills\project-blueprint-architect\SKILL.md` và sổ tay [learned_patterns.md](./references/learned_patterns.md).
2. Chạy tuần tự `blueprint-interviewer` → `solution-architect` → `blueprint-spec-validator` (hoặc qua workflow [blueprint_lock_pipeline.py](./workflows/blueprint_lock_pipeline.py)).
3. **Chỉ bàn giao sang Team 1 (`team-orchestrator-qa`) sau khi người dùng xác nhận "Chốt / Đồng ý"**.

## 🧠 Bộ Nhớ Dài Hạn & Kho Tri Thức Ghim Cứng (Javis Bridge)
- **Trưởng nhóm (Leader):** `solution-architect` | **Bộ nhớ riêng:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-planning-blueprint\MEMORY.md`
- **Đầu ca đọc bộ nhớ & nhật ký chạy:**
  ```powershell
  & "python" "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py" --read team-planning-blueprint
  ```
- **Cuối ca ghi nhận kết quả & bài học:** dùng `--log-run team-planning-blueprint ...` và `--learn team-planning-blueprint --lesson "..."`.
- **Tra cứu Javis Wiki/Sources:** `--search-wiki "<từ_khóa>"` hoặc đọc trực tiếp tài liệu ghim cứng:
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\index.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\so-do-5-phong-ban-va-15-du-an.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\quy-trinh-rang-buoc-chong-ao-giac-ai.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\sources\ban-giam-doc\00-so-tay-quy-chuan-exec.md`
- **Chạy dây chuyền 4 pha chuẩn Javis (`plan → work → verify+retry → memory`):** gọi `run_workflow` với `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py` (`Args: {"team": "team-planning-blueprint", "goal": "..."}`).
