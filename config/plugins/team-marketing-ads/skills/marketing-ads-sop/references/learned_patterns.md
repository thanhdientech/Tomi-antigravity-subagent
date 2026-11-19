# Sổ Tay Kinh Nghiệm Marketing & Ads (Learned Patterns — Team 9)

1. **Xuất Google Ads Editor CSV:** Luôn kiểm tra độ dài ký tự Headline (≤ 30 ký tự) & Description (≤ 90 ký tự) bằng Python313 và mã hóa `utf-8-sig` trước khi bàn giao.
2. **Bảo mật Tracking CAPI:** Mọi Meta CAPI / Google Enhanced Conversions phải cấu hình qua backend webhook hoặc GTM Server-Side, không lộ token ở frontend.
3. **Phân biệt số liệu thật và dự phóng:** Mọi báo cáo gửi khách hàng/nội bộ đều ghi rõ nguồn CSV/tài khoản Ads (nếu là số thật) hoặc đánh dấu rõ là ước tính tham khảo.
