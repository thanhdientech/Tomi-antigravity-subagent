---
name: sap-b1-sql-sop
description: "SOP Team 8 (SAP B1 & SQL): Điều phối 3 subagent cho Kiến trúc SAP B1/Beas, Viết/Test SQL Read-Only và Kiểm toán Kế toán."
---

# SOP Team 8 — ERP SAP B1, Beas & Kế Toán SQL (`team-sap-b1-sql`)

## 1. Nhân Sự Cố Định Trong Team 8
- **`sap-b1-architect`**: Kiến trúc SAP Business One 9.3/10.0, Boyum Beas Manufacturing, giá thành WIP 154, Thông tư 99/2025/TT-BTC, SDK/DI API/Service Layer & DTW (`sap-b1-beas`).
- **`sap-sql-developer`**: Tra cứu schema thật & viết/test T-SQL / HANA SQLScript, FMS, `SBO_SP_TransactionNotification`, 323 mẫu query thực chiến qua `sql_runner.py` (`sql-sap-b1`, `viet-sql-sap-b1`).
- **`sap-accounting-auditor`**: Kiểm toán độc lập số liệu đối chiếu `∑Nợ = ∑Có`, kiểm tra bảng/cột tồn tại thật trong DB và rà luật bảo hành SAP B1 (chỉ đọc & kiểm chứng — không sửa file).

## 2. Sổ Tay Kinh Nghiệm
Đọc [learned_patterns.md](./references/learned_patterns.md) trước khi chạy query trên 4 Server SAP B1.

## 🧠 Bộ Nhớ Dài Hạn & Kho Tri Thức Ghim Cứng (Javis Bridge)
- **Trưởng nhóm (Leader):** `sap-b1-architect` | **Bộ nhớ riêng:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-sap-b1-sql\MEMORY.md`
- **Đầu ca đọc bộ nhớ & nhật ký chạy:**
  ```powershell
  & "python" "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py" --read team-sap-b1-sql
  ```
- **Cuối ca ghi nhận kết quả & bài học:** dùng `--log-run team-sap-b1-sql ...` và `--learn team-sap-b1-sql --lesson "..."`.
- **Tra cứu Javis Wiki/Sources:** `--search-wiki "<từ_khóa>"` hoặc đọc trực tiếp tài liệu ghim cứng:
- `%JAVIS_BRAIN_DIR%\brains_team\Brain Default\wiki\index.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\sap-b1-beas-manufacturing-master.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\so-tay-sap-b1-sql-va-server-vps.md`
- `%JAVIS_BRAIN_DIR%\brains_team\Brain Default\wiki\cam-nang-ke-toan-gia-thanh-thue-va-luong-nghiep-vu-erp.md`
- `%JAVIS_BRAIN_DIR%\brains_team\Brain Default\wiki\cam-nang-sap-b1-93-10-sql-va-beas-manufacturing.md`
- *(+3 tài liệu khác trong `team_memory/WIKI_BRIDGE.md`)*
- **Chạy dây chuyền 4 pha chuẩn Javis (`plan → work → verify+retry → memory`):** gọi `run_workflow` với `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py` (`Args: {"team": "team-sap-b1-sql", "goal": "..."}`).
