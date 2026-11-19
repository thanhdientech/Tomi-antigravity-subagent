---
name: reverse-security-sop
description: "SOP Team 10 (Dịch Ngược & Bảo Mật): Điều phối 3 subagent phân tích nhị phân (REA), tái lập bản sạch (Craft Anything) & audit."
---

# SOP Team 10 — Dịch Ngược, Clean-Room & Bảo Mật (`team-reverse-security`)

## 1. Nhân Sự Cố Định Trong Team 10
- **`rev-binary-analyst`**: Phân tích & bóc tách `.exe`, Electron `.asar`, `.NET`, APK, PyInstaller, Web bundle, HAR/API qua MCP `rea` (`reverse-engineer-anything`).
- **`rev-cleanroom-builder`**: Nghiên cứu hành vi & tái lập bản sạch (Clean-Room / Deep) qua MCP `craft-anything` (`craft-anything`).
- **`sec-vulnerability-auditor`**: Kiểm toán bảo mật mã nguồn, Web/API, CLI & dịch vụ ngầm độc lập (`security-audit` — chỉ kiểm, không sửa code).

## 2. Sổ Tay Kinh Nghiệm
Đọc [learned_patterns.md](./references/learned_patterns.md) trước khi khởi chạy phiên REA hoặc Craft Anything.

## 🧠 Bộ Nhớ Dài Hạn & Kho Tri Thức Ghim Cứng (Javis Bridge)
- **Trưởng nhóm (Leader):** `rev-binary-analyst` | **Bộ nhớ riêng:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-reverse-security\MEMORY.md`
- **Đầu ca đọc bộ nhớ & nhật ký chạy:**
  ```powershell
  & "python" "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py" --read team-reverse-security
  ```
- **Cuối ca ghi nhận kết quả & bài học:** dùng `--log-run team-reverse-security ...` và `--learn team-reverse-security --lesson "..."`.
- **Tra cứu Javis Wiki/Sources:** `--search-wiki "<từ_khóa>"` hoặc đọc trực tiếp tài liệu ghim cứng:
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\giai-thich-9-skills-va-thu-vien-python.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\sources\phong-qa-kiem-toan\00-so-tay-quy-chuan-qa.md`
- **Chạy dây chuyền 4 pha chuẩn Javis (`plan → work → verify+retry → memory`):** gọi `run_workflow` với `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py` (`Args: {"team": "team-reverse-security", "goal": "..."}`).
