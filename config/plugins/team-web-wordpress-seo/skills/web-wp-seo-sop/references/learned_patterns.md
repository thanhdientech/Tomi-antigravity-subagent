# Sổ Tay Kinh Nghiệm Web & WordPress (Learned Patterns — Team 2)

1. **Lỗi trắng trang / `Error establishing a database connection` trên XAMPP local:** Kiểm tra `wp-config.php` tránh define `WP_HOME` / `WP_SITEURL` 2 lần; tắt `WP_CACHE` khi dev local; chạy `php -l` trước khi test HTTP.
2. **Lỗi `Index of /` sau khi restore:** Đảm bảo `index.php`, `wp-config.php`, `wp-admin`, `wp-content` nằm trực tiếp ở thư mục gốc web thay vì nằm lồng trong thư mục con backup.
3. **Icon & Ảnh Landing Page:** Dùng bộ 138 icon SVG chuẩn trong `design-landingpage-vip-v2/assets/icons/`, tuyệt đối không dùng emoji thay icon UI; luôn kiểm tra đường dẫn ảnh không bị 404.
