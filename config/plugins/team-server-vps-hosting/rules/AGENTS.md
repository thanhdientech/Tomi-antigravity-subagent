# Luật Vận Hành Nhóm 4 — Server, VPS, Hosting & DirectAdmin

Khi xử lý bất kỳ tác vụ hạ tầng nào (Windows Server, Linux VPS, Hosting, DirectAdmin), toàn bộ thành viên trong nhóm bắt buộc tuân thủ:

1. **Nguyên tắc Backup Trước Khi Đụng Production:** Trước mọi thao tác sửa cấu hình (`nginx.conf`, `httpd.conf`, `wp-config.php`, firewall, DNS, nâng cấp PHP/DB), bắt buộc tạo bản sao lưu có timestamp (`.bak_YYYYMMDD_HHMMSS`) và xác minh bản sao lưu tồn tại.
2. **Hard Stop Với Lệnh Phá Hủy:** Tuyệt đối dừng lại xin người dùng xác nhận rõ ràng trước khi chạy `rm -rf`, `DROP DATABASE`, xóa account DirectAdmin, mở/đóng port firewall production hoặc khởi động lại server đang có khách truy cập.
3. **Bảo Mật Tuyệt Đối:** Không bao giờ ghi mật khẩu thật, SSH private key hoặc API token vào file cấu hình plugin, mã nguồn hoặc in trần ra log. Dùng `$env:SSHPASS` với `sshpass -e` trên Windows khi cần SSH/SCP không tương tác.
4. **Môi Trường Máy INFOASIA:** Luôn dùng Python313 (`python`), không dùng `python` trần. Với PowerShell, không dùng toán tử `<` để import SQL (dùng `cmd /c` hoặc `Get-Content ... | mysql.exe`).
5. **Tách Vai Làm & Vai Kiểm:** Nhân sự thực thi (`infra-linux-vps`, `infra-windows-server`, `infra-directadmin-hosting`) không tự chốt hoàn thành — phải gọi `infra-qa-security-verifier` kiểm chứng thực tế (`Exit code 0`, HTTP 200, DB Connected, port sống) và xuất Scorecard iFixAi trước khi bàn giao.
