# Sổ Tay Kinh Nghiệm Hạ Tầng (Learned Patterns — Nhóm 4)

> Mọi subagent thuộc Nhóm 4 bắt buộc đọc nhanh file này trước khi xử lý sự cố để tránh thử-sai lặp lại.

## 1. PowerShell & Import SQL trên Windows / XAMPP
- **Triệu chứng:** Lệnh `& mysql.exe -u root db < file.sql` báo lỗi cú pháp trên PowerShell.
- **Nguyên nhân:** PowerShell không hỗ trợ toán tử chuyển hướng đầu vào `<` như `cmd.exe`.
- **Cách xử lý chuẩn:** Dùng `cmd /c "D:\xampp\mysql\bin\mysql.exe -u root db < file.sql"` hoặc chạy script Python313.

## 2. WordPress Local XAMPP — Lỗi `Error establishing a database connection` dù MySQL đang chạy
- **Triệu chứng:** Test PHP `mysqli` kết nối DB thành công nhưng mở trình duyệt vẫn báo lỗi DB hoặc redirect về domain cũ.
- **Nguyên nhân:** File `wp-config.php` bị khai báo `define('WP_HOME', ...)` / `define('WP_SITEURL', ...)` 2 lần hoặc `WP_CACHE = true` giữ cache môi trường cũ.
- **Cách xử lý chuẩn:** Backup `wp-config.php`, comment dòng override domain cũ ở cuối file, tạm đặt `WP_CACHE` về `false`, chạy `php -l wp-config.php` và kiểm tra HTTP 200 bằng Python313.

## 3. SSH/SCP Không Tương Tác Từ Máy Windows INFOASIA
- **Cách xử lý chuẩn:** Đặt mật khẩu vào biến môi trường `$env:SSHPASS` và chạy `sshpass -e -k ssh -o StrictHostKeyChecking=no user@host "lệnh"` (không ghi mật khẩu trần trực tiếp trên tham số `-p` để tránh lộ lịch sử lệnh).

## 4. Python Sandbox Trên Máy INFOASIA
- **Nguyên nhân:** Gọi `python` trần có thể trỏ vào môi trường bị sandbox chặn thư viện (`pyodbc`, `requests`).
- **Cách xử lý chuẩn:** Luôn gọi tường minh `python`.
