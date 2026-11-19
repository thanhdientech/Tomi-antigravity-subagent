# Luật Vận Hành Team 14 — Nhà Máy Video Ngắn 9:16 & Tiếp Thị Liên Kết Shopee (`team-short-video-affiliate`)

Toàn bộ 4 thành viên (`short-channel-product-scout`, `short-script-storyboarder`, `short-kol-studio-producer`, `short-video-qa-auditor`) bắt buộc tuân thủ 6 thiết luật sau khi vận hành tại `E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\`:

1. **Bắt Buộc Đối Chiếu Kho 13 Kênh Mẫu (`Mandatory Sample-Matching Rule`):**
   - Trước khi thiết kế bất kỳ video ngắn `9:16` nào, bắt buộc đọc `Nghien_Cuu_Kenh_Moi_Huong_Dan\00_MASTER_SOP_TOAN_BO_CAC_KENH_CHO_AGENT.md` và mở đối chiếu đúng thư mục mẫu khớp nhất (`01`..`13`: `SOP_*.md`, `videos_mau\*.mp4`, `PREVIEW_*.jpg`, `scripts_python\*.py`, `BANG_TRA_CUU_GIONG_DOC_AI33_VI_EN.md`). Tuyệt đối không thiết kế mò từ đầu.
2. **3 Định Luật Kim Chỉ Nam Chống Lỗi Vật Lý (`Zero Step-Jumping`, `Tool-Tip Lock`, `3.4s Golden Window`):**
   - **Kim Chỉ Nam 1:** Bước `k` bắt buộc truyền trực tiếp ảnh Bước `k-1` làm tham chiếu Image-to-Image và chỉ thêm ĐÚNG 1 thao tác vật lý mới (cấm nhảy cóc bước).
   - **Kim Chỉ Nam 2:** Đầu dụng cụ trên tay (bút, tua-vít, con lăn keo, khăn lau...) phải chạm đúng vị trí chi tiết vừa thêm ở bước đó; với kênh DIY (`09`) loại sạch 100% chữ Hán trên đạo cụ; với `Dual-PiP` (`08`) khóa trục 180° sau đuôi xe.
   - **Kim Chỉ Nam 3:** Cắt Khung Vàng `0.0s -> 3.4s` từ clip Veo 8s (`trim=start=0:end=3.4,setpts=(dur/3.4)*PTS,fps=30`) để triệt tiêu biến hình cuối clip (`Late-Clip Morphing`).
3. **Cấm Dùng Ảnh Tĩnh `zoompan` & Khóa `Stage B5 First Frame Only`:**
   - 100% phân cảnh video (`1080x1920`, `30fps`) phải là cảnh quay chuyển động thật sinh từ `OmniEngine` (`Veo 3.1 :8100` / `Muse :8010`) hoặc `Three.js WebGL` (Kênh `11` Cờ vua / Kênh `13` Cờ tướng).
   - Khi diễn hoạt video B5 từ ảnh cảnh `SCENE_XX.png`, chỉ đính kèm duy nhất ảnh cảnh đó làm First Frame (không đính lại chip `UID01/UID02` rời).
4. **Đúng Môi Trường `.venv` & Cô Lập Cổng `:8600`:**
   - Chạy Shopee KOL Studio bằng `E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Shopee_KOL_Studio_Tool\.venv\Scripts\python.exe` (5 dịch vụ `:8600 / :8650 / :8100 / :8010 / :8766`, tách hẳn `:8500` của YouTube dài).
   - Script kiểm định nhẹ / `ffprobe` / `team_memory_cli.py`: dùng Python313 (`python`).
5. **Chống Bịa Thông Số NSX & Phụ Đề Safe-Zone Meta Reels:**
   - Mọi thông số kỹ thuật sản phẩm Shopee phải trích 100% từ dữ liệu thật của Shop; bỏ chữ `"Shopee"` khi làm cho TikTok Shop / Web riêng; lời thoại KOL đời thường tự nhiên 100% sạch URL/Markdown.
   - Phụ đề chạy theo nhịp giọng đọc (`1–2 dòng`) neo trọn trong Safe-Zone Facebook Reels/TikTok (`y_top >= 148px`, `y_bottom <= 1244px`, `x = 64..896px`).
6. **Tách Vai Sản Xuất & Kiểm Toán Mắt Thật Độc Lập (`No Self-Grading`):**
   - `short-video-qa-auditor` chỉ đọc & chạy kiểm định (**CẤM** `edit_file`/`write_file`), bắt buộc gọi `read_file` mở soi trực tiếp ảnh `Step_01..08` (Cổng 1) và ảnh cuối cảnh `qa_end_step_*.jpg` + `ffprobe` (Cổng 2) trước khi bàn giao.
