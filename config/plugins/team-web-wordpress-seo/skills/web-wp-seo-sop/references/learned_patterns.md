# Sổ Tay Kinh Nghiệm Web & WordPress (Learned Patterns — Team 2)

1. **Lỗi trắng trang / `Error establishing a database connection` trên XAMPP local:** Kiểm tra `wp-config.php` tránh define `WP_HOME` / `WP_SITEURL` 2 lần; tắt `WP_CACHE` khi dev local; chạy `php -l` trước khi test HTTP.
2. **Lỗi `Index of /` sau khi restore:** Đảm bảo `index.php`, `wp-config.php`, `wp-admin`, `wp-content` nằm trực tiếp ở thư mục gốc web thay vì nằm lồng trong thư mục con backup.
3. **Icon & Ảnh Landing Page:** Dùng bộ 138 icon SVG chuẩn trong `design-landingpage-vip-v2/assets/icons/`, tuyệt đối không dùng emoji thay icon UI; luôn kiểm tra đường dẫn ảnh không bị 404.
4. **Quy Chuẩn Flatsome `V4.2` (Bắt Buộc Mọi Dự Án Team 2):**
   - **100% Quản trị động — Cấm code cứng:** Mọi thành phần Frontend đều chỉnh được trong `WP-Admin / UX Builder / Customizer` (CRUD, kéo thả vị trí, màu sắc, chia cột, layout riêng Máy tính/Tablet/Điện thoại); ngoại lệ bắt buộc dùng code phải tách tham số ra Admin + giải trình bằng **Bảng Ngoại Lệ 5 Cột** + hướng dẫn.
   - **Ngôn ngữ hiển thị:** Mặc định **1 ngôn ngữ** tùy theo dự án — luôn hỏi người dùng ở Bước 1, KHÔNG tự ý bắt buộc làm đa ngôn ngữ; chỉ bật kiến trúc Native WP Multilang (InfoAsia V3.5 — 0 plugin nặng, decode `&#038;` priority `99`) khi khách yêu cầu `>= 2` ngôn ngữ.
   - **UX & Chuyển đổi chuẩn `V4.2`:** View nhìn rộng thoáng không quá gần (`1220–1280px`), Khung Bộ lọc (`Smart Filter`) có thể thu gọn, Mega Menu có Ảnh/Icon SVG đẹp, **100% danh sách liệt kê có Icon SVG inline đẹp**, tích hợp Chatbot AI / Zalo / Form CRM / (Mua hàng, Thanh toán COD-VietQR & Ship GHN nếu có), đạt chuẩn SEO 2026 & **PageSpeed 100/100 Desktop & Mobile** (`CLS = 0`, `0KB` admin leak).
