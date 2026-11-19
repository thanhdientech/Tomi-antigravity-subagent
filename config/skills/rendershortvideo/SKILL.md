---
name: rendershortvideo
description: "Điều khiển Shopee KOL Studio (:8600) & 11 mẫu video ngắn 9:16: đối chiếu video mẫu, học kênh, khóa nhân vật & chống nhảy bước."
group: "Làm Phim & Video AI"
---

# 📱 RENDER SHORT VIDEO, SHOPEE KOL STUDIO & KHO 11 VIDEO MẪU NGHIÊN CỨU (`rendershortvideo` — `:8600`)

<!-- JAVIS_TRIGGER_ARCHIVE_START -->
## Khi nào dùng (Triggers & Ngữ cảnh kích hoạt đầy đủ)

> Điều khiển trực tiếp hệ thống **Shopee & Multi-Source KOL Video Studio (`v4.3.3` — Cổng `:8600` / Timeline `:8650`)** và **Kho 11 Dạng Video Mẫu Nghiên Cứu & SOP Kênh Triệu View** nằm cố định tại `E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video` để sản xuất **Video Ngắn Dọc (`9:16`, `1080x1920`, `30fps`)** cho Shopee Affiliate, TikTok Shop, Facebook Reels và YouTube Shorts. **Quy tắc cốt lõi: Khi yêu cầu của người dùng giống hoặc gần giống bất kỳ dạng nào trong 11 dạng video nghiên cứu (Ô tô tư vấn cabin, Thời trang Dance, Thời trang KOL Color Palette, Mẹo vặt khoa học, Decor chữa lành, Thể thao Calisthenics, KOC lắp phụ kiện ô tô 7 góc, Mẹo lái xe Dual-PiP, DIY thủ công 8 bước, Học tiếng Anh gia đình 3D Flashcard kiểu Kyna, Cờ vua 3D kịch tính kiểu Forgiro), AI Agent BẮT BUỘC mở đối chiếu trực tiếp Video Mẫu (`videos_mau/*.mp4`), ảnh Preview/Gốc nhân vật, file SOP `.md` và Script Python mẫu trong `Nghien_Cuu_Kenh_Moi_Huong_Dan` trước khi thực thi.** Bao phủ trọn gói: Học kênh mẫu (`reference-learner`), Khóa nhân vật 6 góc `[uid01]` + Phòng trống `[LOC]` + Giọng đọc (`ai33.pro` / `Edge-TTS`), Lộ trình 50 video xây kênh, Quét SP chống sale ảo, 3 Định luật Kim Chỉ Nam (`Zero Step-Jumping`, `Tool-Tip Contact Lock`, `Golden-Window 0.0s->3.4s`), Render đa luồng Veo 3.1 (`:8100`) / Muse (`:8010`) / `Three.js WebGL`, phụ đề Safe-Zone và xuất kép `.MP4`.
> TRIGGERS: "rendershortvideo", "render short video", "làm video ngắn", "lam video ngan", "render video ngắn", "video shopee", "làm video shopee", "shopee kol studio", "cổng 8600", "cong 8600", "cổng 8650", "video mẫu nghiên cứu", "tham chiếu video mẫu", "học kênh mẫu", "50 video xây kênh", "tiktok shop video", "reels 9:16", "youtube shorts", "chống nhảy bước", "zero step jumping", "golden window 3.4s", "dual pip lái xe", "kênh diy 8 bước", "kênh mẹo vặt", "kênh thời trang dance", "color palette", "koc ô tô", "decor chữa lành", "calisthenics", "flashcard tiếng anh", "kyna english", "cờ vua 3d", "forgiro".
<!-- JAVIS_TRIGGER_ARCHIVE_END -->

- **Thư mục công cụ & kho video mẫu thực thi gốc (Giữ nguyên tại ổ E — Gọi & tham chiếu trực tiếp, KHÔNG sao chép sang nơi khác):**
  - 🛠️ **Bộ máy Shopee KOL Studio (`:8600`):** `E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Shopee_KOL_Studio_Tool`
    - Khởi động 1 chạm 5 dịch vụ: `"E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Shopee_KOL_Studio_Tool\START_SHOPEE_STUDIO.bat"` $\rightarrow$ Mở `http://127.0.0.1:8600`
    - Dừng / Khởi động lại sạch: `STOP_ALL_SERVICES.bat` / `RESTART_ALL_SERVICES.bat`
    - Python `.venv` chuẩn của Tool: `"E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Shopee_KOL_Studio_Tool\.venv\Scripts\python.exe"`
  - 🎬 **Kho 11 Dạng Video Mẫu Nghiên Cứu, SOP & Script Python (`01..11`):**
    `E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Nghien_Cuu_Kenh_Moi_Huong_Dan`
    - Sổ tay điều hướng tổng: `E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Nghien_Cuu_Kenh_Moi_Huong_Dan\00_MASTER_SOP_TOAN_BO_CAC_KENH_CHO_AGENT.md`
  - 🌐 **Kho Git Upstream của Tool:** [thanhdientech/Shopee_KOL_Studio_Tool](https://github.com/thanhdientech/Shopee_KOL_Studio_Tool)

---

## 🚨 1. QUY TẮC BẮT BUỘC: THAM CHIẾU VIDEO MẪU KHI YÊU CẦU GIỐNG 11 DẠNG NGHIÊN CỨU (`MANDATORY SAMPLE-MATCHING RULE`)

Khi người dùng yêu cầu làm một video ngắn có chủ đề, bố cục hoặc phong cách **giống hoặc tương tự bất kỳ dạng nào trong 11 dạng video đã nghiên cứu** dưới đây, AI Agent **TUYỆT ĐỐI KHÔNG tự thiết kế mò từ đầu** mà **BẮT BUỘC vào đúng thư mục mẫu tại `E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Nghien_Cuu_Kenh_Moi_Huong_Dan\` để tham chiếu trước**:

1. **`01` — Ô tô KOC Cabin:** Nữ KOC ngồi ghế lái so sánh Xe Điện vs Xe Xăng, chi phí nuôi xe & phụ kiện nội thất (`videos_mau/VIDEO_01..03_*.mp4`).
2. **`02` — Thời trang AI Hotgirl Dance:** Nhảy Dance Pop 124–128 BPM khoe form đồ ngủ lụa, sườn xám, sơ mi chân váy góc `Knee-up 9:16` (`videos_mau/MAU_REEL_01..02_*.mp4`).
3. **`03` — Thời trang KOL Review + Color Palette:** Voiceover review chất vải + thẻ bảng màu 3 mã HEX + khung ngắm `[● REC 4K]` (`videos_mau/VIDEO_SHOPEE_916_SET_DA_TWEED_*.mp4`).
4. **`04` — Mẹo vặt khoa học đời sống 60s:** Host nam đeo mic thực nghiệm 5 pha Toàn – Trung – Cận trên đảo bếp (`HUONG_DAN_SOP_CHI_TIET_MEO_VAT_60S.md`).
5. **`05` — Decor & Dọn dẹp chữa lành:** Cải tạo bàn làm việc, ban công, góc phòng `Before -> Process -> After` (`videos_mau/VIDEO_MAU_DECOR_GOC_BAN_LAM_VIEC_CHUA_LANH_916.mp4`).
6. **`06` — Thể thao dáng đẹp Calisthenics:** Tập xà đơn chữ U công viên ban đêm bắt nhạc Gym Remix (`videos_mau/VIDEO_THE_THAO_CO_GAI_TAP_XA_BAN_DEM_KHONG_BIEN_HINH_916.mp4`).
7. **`07` — KOC Lắp đặt phụ kiện ô tô 7 góc quay:** Ra phố kiểm tra thực tế, bóp dẻo, bắt vít lỗ zin & test cản nước mưa kiểu *Long Gara* (`videos_mau/VIDEO_05_REVIEW_CHAN_BUN_O_TO_7_GOC_QUAY_THAT_100.mp4`).
8. **`08` — Mẹo lái xe `Dual-View PiP`:** Góc cao sau đuôi xe nhìn quỹ đạo + khung tròn xoay vô-lăng đồng bộ + gương cầu lồi 360° (`videos_mau/VIDEO_01_MEO_LUI_XE_NGO_HEP_DUAL_PIP_7_GOC_LOGIC_100.mp4`).
9. **`09` — DIY Nghệ thuật & Họa cụ Mẹ & Bé:** Làm tranh lá cây/vỏ cây/đất sét 7–8 bước kế thừa không nhảy cóc, xuất kép Giọng hướng dẫn + ASMR (`videos_mau/VIDEO_01..05B_*.mp4`).
10. **`10` — Học Tiếng Anh gia đình 3D Flashcard + Suno Song:** Gia đình 3D Pixar hỏi đáp từ vựng + câu Q&A `en-US` + HUD IPA + MV bài hát ôn tập `suno.com/create` kiểu *Bé Nói English / Kyna* (`videos_mau/VIDEO_01_V3_STORY_KEM_BAI_HAT_SUNO_AI.mp4`).
11. **`11` — Cờ vua 3D kịch tính giải mã thế cờ:** Hook cận cảnh nước thí Hậu + bàn cờ gỗ 3D `Three.js` nghiêng `42°` + giọng Epic Tùng Đặng kiểu *Forgiro* (`videos_mau/VIDEO_01_CO_VUA_3D_OPERA_1858_*.mp4`, `VIDEO_02_CO_VUA_3D_LASKER_1912_*.mp4`).

**Quy trình 3 bước đối chiếu mẫu bắt buộc:** (1) Đọc file SOP `.md` của thư mục khớp nhất $\rightarrow$ (2) Dùng `read_file` / `ffprobe` xem ảnh `PREVIEW_*.jpg`, ảnh gốc `stages/` và thông số file `videos_mau/*.mp4` để bám sát 100% bố cục, nhịp cắt, HUD và âm lượng $\rightarrow$ (3) Kế thừa trực tiếp Script Python trong `scripts_python/` & mã `Voice ID` chuẩn của mẫu đó.

---

## 📌 2. BẢNG ĐIỀU PHỐI TÀI LIỆU CHUYÊN SÂU (`references/`)

| Tình Huống / Bước Thực Thi | Tệp Tham Chiếu Cần Đọc | Nội Dung Cốt Lõi |
| :--- | :--- | :--- |
| **Kiến trúc 5 Cổng (`:8600/:8650/:8100/:8010/:8766`), 7 Bước Xây Kênh & REST API** | [`references/01-kien-truc-5-dich-vu-7-buoc-xay-kenh-va-api-8600.md`](./references/01-kien-truc-5-dich-vu-7-buoc-xay-kenh-va-api-8600.md) | Sơ đồ 5 Microservices cách ly cổng (không đụng `:8500` của YouTube dài), lưu trữ 8 ngăn & trọn bộ API `:8600`. |
| **3 Định Luật Kim Chỉ Nam & Kỹ Thuật Đặc Thù (Chống Nhảy Bước, `3.4s`, 3D Pixar, `Three.js` Cờ Vua)** | [`references/02-kim-chi-nam-tam-dong-nhat-va-chong-nhay-buoc-bien-hinh.md`](./references/02-kim-chi-nam-tam-dong-nhat-va-chong-nhay-buoc-bien-hinh.md) | Kế thừa `Step_{k-1}`, `Tool-Tip Contact Lock`, `trim=0:3.4`, trục 180° `Dual-PiP`, giọng gốc Veo 3.1 Lite & `Three.js 8x8` Zero-Flicker. |
| **Bản Đồ 11 Dạng Video Mẫu (`videos_mau/*.mp4`), SOP Riêng, Chọn SP & Mã Giọng Đọc** | [`references/03-ban-do-11-mau-kenh-video-mau-sop-va-giong-doc.md`](./references/03-ban-do-11-mau-kenh-video-mau-sop-va-giong-doc.md) | Danh mục chi tiết từng file `.mp4` mẫu, file SOP `.md`, script `.py`, chiến lược sản phẩm theo tệp người xem & mã `Voice ID`. |

---

## 📌 3. LỆNH GỌI NHANH TỪ AI AGENT TỚI TOOL & KHO MẪU TẠI Ổ E

1. **Kiểm tra trạng thái 5 cổng dịch vụ (`:8600, :8650, :8100, :8010, :8766`) hoặc khởi động:**
   ```powershell
   Invoke-RestMethod -Uri "http://127.0.0.1:8600/api/health" -ErrorAction SilentlyContinue
   $ToolDir = "E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Shopee_KOL_Studio_Tool"
   Start-Process -WorkingDirectory $ToolDir -FilePath "cmd.exe" -ArgumentList "/c START_SHOPEE_STUDIO.bat"
   ```
2. **Tra cứu nhanh danh sách Video Mẫu & SOP của một chủ đề trong `Nghien_Cuu_Kenh_Moi_Huong_Dan`:**
   ```powershell
   $SampleRoot = "E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Nghien_Cuu_Kenh_Moi_Huong_Dan"
   Get-ChildItem -LiteralPath $SampleRoot -Recurse -Include *.md, *.mp4, PREVIEW_*.jpg, *.py | Select-Object FullName
   ```
3. **Kết nối MCP Server của Shopee Studio (khi cần gọi qua giao thức MCP):**
   - Tệp thực thi: `"E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Shopee_KOL_Studio_Tool\shopee_video_studio\mcp_shopee_studio.py"`.

---

## 📌 4. 5 QUY TẮC VÀNG BẮT BUỘC KHI LÀM VIDEO NGẮN (`NON-NEGOTIABLE GATES`)

1. **Chỉ Gọi Tool & Tham Chiếu Video Mẫu Tại Chỗ (`In-Place Execution & Sample Reference`):** Giữ nguyên toàn bộ source, `.venv`, DB `channels_studio.sqlite` và 11 thư mục video mẫu tại `E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video`; luôn đối chiếu mẫu trước khi làm nếu trùng dạng video.
2. **Cấm Dùng Ảnh Tĩnh Chạy Hiệu Ứng Zoom (`No Static Zoompan`):** 100% phân cảnh video xuất bản phải là cảnh quay chuyển động thật (`1080x1920`, `30fps`) sinh từ `OmniEngine` (`Veo 3.1 :8100` / `Muse.ai :8010`) hoặc Engine 3D `Three.js WebGL` (với Cờ vua 3D).
3. **3 Định Luật Kim Chỉ Nam Chống Lỗi Vật Lý:** Kế thừa ảnh `Step_{k-1}` chống nhảy bước, khóa điểm chạm đầu dụng cụ (`read_file` soi từng ảnh trước khi render) và cắt Khung Vàng `0.0s -> 3.4s` chống biến hình cuối clip.
4. **Khóa Tệp Khán Giả Thật & Thông Số NSX Thật (`Zero Hallucination`):** Chọn sản phẩm đúng nhân khẩu học người xem thật; không bịa thông số kỹ thuật; định hướng CTA cho phụ huynh ở bình luận ghim đối với nội dung có trẻ em (Kênh 10); tự loại chữ `"Shopee"` khi làm cho TikTok Shop/Web riêng.
5. **Vùng An Toàn Phụ Đề (`Safe-Zone 9:16`) & Xuất Kép:** Đặt phụ đề gọn trong Safe-Zone Reels/TikTok/Shorts (`y_top >= 148px`, `y_bottom <= 1244px`, `x = 64..896px`); với kênh hướng dẫn/DIY xuất đủ 2 bản (Có Giọng Hướng Dẫn & Nhạc + ASMR sạch).
