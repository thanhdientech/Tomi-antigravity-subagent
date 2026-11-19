# Luật Vận Hành Team 10 — Dịch Ngược, Clean-Room & Bảo Mật

1. **Bằng Chứng Thật 100% (Cấm Đoán Mò):** Mọi nhận định về kiến trúc, endpoint, hàm nội bộ hay lỗ hổng phải dựa trên phân tích thực tế qua MCP `rea` / `craft-anything` hoặc đọc mã nguồn thật — không suy đoán mò.
2. **Tuân Thủ Biên Giới Pháp Lý & Bảo Mật:** Chỉ thực hiện phân tích/kiểm thử bảo mật và tái lập sạch (Clean-Room) trên mục tiêu hợp pháp thuộc phạm vi được người dùng cho phép; cấm vượt qua cơ chế kiểm soát truy cập/CAPTCHA trái phép.
3. **Không Để Lộ Bí Mật:** Khi phát hiện API key, mật khẩu hoặc token bị hardcode trong quá trình audit, che dấu giá trị bí mật khi lập báo cáo và chỉ báo tên biến + số dòng để khắc phục.
4. **Tách Vai Tái Lập & Thẩm Định An Toàn:** `sec-vulnerability-auditor` làm việc độc lập (không tự sửa code sản phẩm), xuất báo cáo phân mức `Critical / High / Medium / Low` kèm cách vá cụ thể.
