# Luật Vận Hành Team 2 — Web, WordPress, Landing Page & SEO/GEO

1. **Chuẩn Flatsome & WordPress:** Không chế shortcode không có thật trong UX Builder; luôn backup `wp-config.php`, `functions.php`, `.htaccess` trước khi sửa; kiểm tra `php -l` đạt `Exit code 0`.
2. **Bảo Mật Tracking CAPI & Thanh Toán:** Tuyệt đối KHÔNG gắn Meta Access Token / TikTok CAPI token trực tiếp ở mã nguồn frontend HTML/JS — bắt buộc gửi qua backend webhook.
3. **Không Bịa Chỉ Số SEO/Tốc Độ:** Không tự bịa điểm Core Web Vitals, lượng tìm kiếm từ khóa hay thứ hạng Google khi chưa đo thực tế.
4. **Verify-Loop Bắt Buộc:** Mọi trang web/Landing Page làm xong phải kiểm tra HTTP 200, DB Connected (nếu WordPress), và phối hợp `qa-visual-human-tester` mở trình duyệt chụp & đọc ảnh Desktop + Mobile trước khi bàn giao.
