# Sổ Tay Kinh Nghiệm Tra Cứu Web (Learned Patterns — Nhóm 5)

> Mọi subagent thuộc Nhóm 5 đọc nhanh file này trước khi bắt đầu phiên tra cứu.

## 1. Bẫy Tin Cũ & Văn Bản Hết Hiệu Lực
- **Bài học:** Nhiều bài blog SEO top Google vẫn trích quy định cũ (ví dụ Thông tư kế toán cũ thay vì Thông tư 99/2025/TT-BTC, hoặc chính sách Meta/Google Ads năm cũ).
- **Cách xử lý:** Luôn thêm năm hiện hành vào truy vấn tìm kiếm, ưu tiên trang chủ cơ quan ban hành / Official Docs và ghi rõ **Ngày ban hành & Tình trạng hiệu lực**.

## 2. Bẫy Link Ảo / Redirect / Paywall
- **Bài học:** URL cắt từ snippet tìm kiếm có thể trả `HTTP 404` hoặc chuyển hướng về trang chủ không còn chứa dữ kiện.
- **Cách xử lý:** Luôn kiểm tra link bằng Python313 (`requests` / `urllib`) hoặc `%USERPROFILE%\.gemini\config\skills\verified-source-researcher\cli.py` để xác nhận `HTTP 200` trước khi đưa vào báo cáo.

## 3. Quy Tắc Tách Sạch Nội Dung 3 Tầng
- **Bài học:** Chèn tọa độ kỹ thuật, nhãn `🟢/🟡/🔴` hoặc từ khóa nội bộ (`Chốt chặn`, `RULE[user_global]`) vào bài viết công khai sẽ làm hỏng văn phong xuất bản.
- **Cách xử lý:** Nội dung đọc (Tầng 1) luôn sạch 100%; tài liệu tham khảo (Tầng 2) ngắn gọn cuối bài; toàn bộ bảng 6 cột & nhãn kiểm chứng (Tầng 3) trả riêng trên khung chat hoặc file `_THAM_CHIEU_NGUON.md`.
