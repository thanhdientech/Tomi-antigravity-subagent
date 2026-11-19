# Luật Vận Hành Team 5 — Edit Video, Motion & Hậu Kỳ MP4

1. **Không Bàn Giao Video Chưa Kiểm Định Thực Tế:** Mọi file `.mp4` xuất ra bắt buộc qua `video-qa-verifier` chạy `ffprobe` (kiểm tra đủ thời lượng, có luồng video + audio, FPS & độ phân giải chuẩn) và trích xuất tối thiểu 2–3 frame ảnh PNG rồi **mở đọc ảnh bằng `read_file`** để bắt lỗi tràn chữ, sai font tiếng Việt, màn hình đen hoặc lệch phụ đề.
2. **Đúng Engine Cho Đúng Việc:** Edit nhanh HTML→MP4/hàng loạt dùng `ai-video-studio` `:5186` hoặc `Auto-Editor`/`Editly`/`FFmpeg`; Motion đồ họa/React dùng `Remotion` / `Motion Canvas`; Toán-Khoa học dùng `Manim`; Reels khớp nhịp dùng `kinetic-reel`; Màu nước dùng `painted-animation`; Tutorial màn hình dùng `recordly-tutorial-ai`.
3. **Chuẩn Môi Trường INFOASIA:** Chạy toàn bộ script dựng/hậu kỳ Python bằng `python`; giữ file nguồn gốc nguyên vẹn (không ghi đè đứt file input).
