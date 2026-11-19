---
name: server-vps-sop
description: "Quy trình chuẩn (SOP) quản trị Windows Server, Linux VPS, Hosting & DirectAdmin, điều phối 4 subagent cố định và tích lũy sổ tay lỗi hạ tầng."
---

# SOP Điều Phối Nhóm 4 — Server, VPS, Hosting & DirectAdmin

## 1. Danh Sách 4 Nhân Sự Cố Định Trong Nhóm

| Subagent (`TypeName`) | Phạm vi phụ trách | Quyền thao tác |
| :--- | :--- | :--- |
| `infra-linux-vps` | Linux VPS (Ubuntu/AlmaLinux/CentOS), SSH/SCP, Nginx/Apache/OpenLiteSpeed, systemd, SSL, UFW/CSF | Đọc + Sửa + Chạy lệnh |
| `infra-windows-server` | Windows Server, IIS, XAMPP, SQL Server/MySQL service, PowerShell, Task Scheduler, Windows Firewall | Đọc + Sửa + Chạy lệnh |
| `infra-directadmin-hosting` | DirectAdmin & Hosting: Backup/Restore account + DB, phân quyền, PHP version, DNS/SSL, di chuyển website | Đọc + Sửa + Chạy lệnh + Tra cứu |
| `infra-qa-security-verifier` | Kiểm chứng độc lập sau thực thi: test port/HTTP/SSL/DB, kiểm tra dung lượng backup, rà bảo mật, chấm Scorecard | **Chỉ đọc & chạy test (Cấm sửa file)** |

## 2. Quy Trình 4 Bước Bắt Buộc

1. **Đọc sổ tay kinh nghiệm trước khi làm:** Mở [learned_patterns.md](./references/learned_patterns.md) để tránh lặp lại lỗi đã từng gặp.
2. **Phân vai thực thi (Inspect → Backup → Apply):**
   - Tác vụ Linux VPS → gọi `infra-linux-vps`.
   - Tác vụ Windows Server / XAMPP / IIS → gọi `infra-windows-server`.
   - Tác vụ DirectAdmin / Hosting / Migration → gọi `infra-directadmin-hosting`.
3. **Kiểm chứng độc lập (QA Gate):** Gọi `infra-qa-security-verifier` chạy kiểm tra thực tế (HTTP 200, DB Connected, service active, không lộ secret) và xuất Scorecard.
4. **Cập nhật sổ tay sau ca khó:** Nếu phát hiện nguyên nhân lỗi mới, ghi ngắn gọn 3–5 dòng vào [learned_patterns.md](./references/learned_patterns.md).

## 3. Chạy Dây Chuyền Tự Động Bằng Python Workflow

Khi cần thực thi trọn quy trình **Thay đổi hạ tầng → QA kiểm chứng độc lập** mà không phụ thuộc trí nhớ khung chat, chạy workflow mẫu tại [infra_change_pipeline.py](./workflows/infra_change_pipeline.py) bằng công cụ `run_workflow`.

## 🧠 Bộ Nhớ Dài Hạn & Kho Tri Thức Ghim Cứng (Javis Bridge)
- **Trưởng nhóm (Leader):** `infra-linux-vps` | **Bộ nhớ riêng:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-server-vps-hosting\MEMORY.md`
- **Đầu ca đọc bộ nhớ & nhật ký chạy:**
  ```powershell
  & "python" "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py" --read team-server-vps-hosting
  ```
- **Cuối ca ghi nhận kết quả & bài học:** dùng `--log-run team-server-vps-hosting ...` và `--learn team-server-vps-hosting --lesson "..."`.
- **Tra cứu Javis Wiki/Sources:** `--search-wiki "<từ_khóa>"` hoặc đọc trực tiếp tài liệu ghim cứng:
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\danh-sach-dich-vu-va-port-vps-29.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\so-tay-sap-b1-sql-va-server-vps.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\sources\phong-1-erp-server\it-server-manager-readme.md`
- **Chạy dây chuyền 4 pha chuẩn Javis (`plan → work → verify+retry → memory`):** gọi `run_workflow` với `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py` (`Args: {"team": "team-server-vps-hosting", "goal": "..."}`).
