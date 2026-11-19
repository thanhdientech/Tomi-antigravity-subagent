# Sổ Tay Kinh Nghiệm Edit Video & Motion (Learned Patterns — Team 5)

1. **Lỗi font tiếng Việt khi burn phụ đề FFmpeg/Canvas:** Luôn chỉ định tường minh font Unicode hỗ trợ dấu tiếng Việt và kiểm tra frame xuất ra bằng `read_file`.
2. **Lỗi video mất tiếng hoặc lệch độ phân giải:** Trước khi giao, luôn chạy `ffprobe -v error -show_streams` để xác nhận đủ 2 stream `video` + `audio`, đúng tỷ lệ `16:9` (1920x1080) hoặc `9:16` (1080x1920).
3. **Render hàng loạt không đè file gốc:** Luôn xuất thành phẩm vào thư mục `output/` riêng kèm timestamp hoặc tên cảnh rõ ràng.
