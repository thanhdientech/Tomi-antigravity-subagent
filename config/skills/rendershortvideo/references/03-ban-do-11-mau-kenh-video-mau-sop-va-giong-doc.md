# 03. Bản Đồ 11 Dạng Video Mẫu Nghiên Cứu (`01..11`), Quy Tắc Đối Chiếu Mẫu, Chiến Lược Chọn SP & Mã Giọng Đọc (`rendershortvideo`)

Tài liệu điều hướng trực tiếp tới **Kho Video Mẫu Nghiên Cứu & SOP 11 Chủ Đề Kênh Triệu View** đặt cố định tại:
`E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Nghien_Cuu_Kenh_Moi_Huong_Dan`

---

## 1. Quy Tắc Bắt Buộc Đối Chiếu Video Mẫu Trước Khi Sản Xuất (`Mandatory Sample-Matching Protocol`)

> **NGUYÊN TẮC CỐT LÕI:** Bất cứ khi nào yêu cầu của người dùng giống hoặc gần giống **một trong 11 dạng video dưới đây**, AI Agent **TUYỆT ĐỐI KHÔNG tự suy diễn bố cục từ con số 0**, mà **BẮT BUỘC tham chiếu trực tiếp bộ mẫu đã nghiên cứu** theo 4 bước chuẩn:

1. **Bước 1 — Đọc Tổng quan & SOP riêng của mẫu khớp nhất:**
   - Đọc `00_MASTER_SOP_TOAN_BO_CAC_KENH_CHO_AGENT.md` và file SOP `.md` nằm ngay trong thư mục kênh khớp (`01` đến `11`) để khóa đúng: cấu trúc nhịp điệu (`Hook -> Thân -> CTA`), số cảnh/góc máy, quy tắc vật lý chống nhảy bước và phễu chuyển đổi Affiliate.
2. **Bước 2 — Đối chiếu trực tiếp Video Mẫu (`videos_mau/*.mp4`) & Ảnh Khung Hình (`PREVIEW_*.jpg` / `images_*/` / `stages/`):**
   - Dùng `read_file` mở ảnh `PREVIEW_*.jpg`, ảnh gốc nhân vật/bước (`stages/`, `images_*/`) hoặc chạy `ffprobe` / trích frame từ `videos_mau/*.mp4` để học chuẩn 100%: tỷ lệ khung hình, cỡ chữ thẻ HUD/phụ đề, bảng màu, nhịp cắt cảnh và mức âm lượng (`mean_volume`).
3. **Bước 3 — Kế thừa Script Python / Engine 3D & Mã Giọng Đọc đã kiểm chứng:**
   - Nhân bản hoặc gọi trực tiếp script mẫu trong `scripts_python/` (hoặc `assets/chess_reel_3d.html` với Kênh 11) và giữ đúng mã `Voice ID` đã khóa cho dạng kênh đó.
4. **Bước 4 — Chỉ Tham Chiếu Tại Chỗ (`In-Place Reference`):**
   - Đọc và chạy trực tiếp từ ổ `E:`, không sao chép các file `.mp4` nặng sang thư mục cấu hình Skill.

---

## 2. Bảng Ánh Xạ Đầy Đủ 11 Dạng Video Mẫu Nghiên Cứu (`01..11`) Tại Ổ `E:`

Thư mục gốc của mọi đường dẫn con bên dưới:
`E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Nghien_Cuu_Kenh_Moi_Huong_Dan\`

| Mã | Dấu Hiệu Nhận Diện Yêu Cầu Người Dùng | Thư Mục Mẫu & File SOP Chuẩn | Video Mẫu & Ảnh Preview Cần Tham Chiếu (`videos_mau/`) | Script Python Mẫu & Giọng Đọc Khóa Cứng |
| :-: | :--- | :--- | :--- | :--- |
| **01** | Tư vấn mua xe lần đầu, so sánh chi phí nuôi **Xe Điện vs Xe Xăng**, KOC nữ ngồi cabin chia sẻ mẹo nội thất ô tô | `01_KENH_O_TO_KOC_MEO_XE_VA_XE_DIEN_XE_XANG/`<br>• SOP: `HUONG_DAN_SOP_CHI_TIET_KENH_O_TO.md` | • `VIDEO_01_MUA_XE_LAN_DAU_CHON_XE_DIEN_HAY_XE_XANG.mp4`<br>• `VIDEO_02_CHI_PHI_NUOI_XE_DIEN_VA_XE_XANG_1_THANG.mp4`<br>• `VIDEO_03_3_SAI_LAM_KHI_MOI_MUA_XE_DIEN_XE_XANG.mp4`<br>• `VIDEO_SHOPEE_916_AI_KOC_NU_MOI_MEO_XE_NEM_TRUNG.mp4` | • `scripts_python/generate_ev_vs_gas_voices_and_subs.py`<br>• `render_all_real_veo_videos.py`<br>• Nữ: `elevenlabs_Jmio6r8OUeqiK3cZ3N0K` (*Thu Thảo Story*) |
| **02** | **Thời trang nữ nhảy Dance Trending** khoe form OOTD, đồ ngủ lụa, sườn xám, sơ mi chân váy góc `Knee-up 9:16` | `02_KENH_THOI_TRANG_AI_HOTGIRL_DANCE_TRENDING/`<br>• SOP: `HUONG_DAN_SOP_CHI_TIET_FASHION_DANCE.md` | • `MAU_REEL_01_AI_HOTGIRL_SUON_XAM_HOA_TIET_HAC.mp4`<br>• `MAU_REEL_02_AI_HOTGIRL_SO_MI_HONG_CHAN_VAY.mp4`<br>• `VIDEO_SHOPEE_916_AI_HOTGIRL_DANCE_DO_NGU_LUA_MINT.mp4`<br>• `VIDEO_SHOPEE_916_AI_HOTGIRL_DANCE_FASHION_LOOKBOOK.mp4`<br>• `VIDEO_SHOPEE_916_DANG_FACEBOOK_CO_GAI_AO_DO.mp4` | • `scripts_python/build_complete_shopee_fashion_video.py`<br>• **Không Voiceover** (Thuần nhạc Dance Pop Remix 124–128 BPM) |
| **03** | **KOL Review thời trang có lời bình** + Thẻ bảng màu **Color Palette 3 mã HEX** + Khung ngắm máy quay **`[● REC 4K]`** | `03_KENH_THOI_TRANG_KOL_REVIEW_COLOR_PALETTE/`<br>• SOP: `HUONG_DAN_SOP_CHI_TIET_KOL_REVIEW_PALETTE.md` & `HUONG_DAN_SAN_XUAT_2_LOAI_VIDEO_THOI_TRANG_916.md` | • `VIDEO_SHOPEE_916_SET_DA_TWEED_CHUYEN_DONG_FLOWKIT_ELEVENLABS.mp4`<br>• `VIDEO_SHOPEE_916_DANG_FACEBOOK_CO_GAI_BABYDOLL.mp4` | • `scripts_python/render_flowkit_elevenlabs_video.py`<br>• `render_tweed_video.py`<br>• Nữ: `elevenlabs_CQAD6iKxS73fEAGjSwt5` (*Giang Podcast*) / `aN7cv9yXNrfIR87bDmyD` |
| **04** | **Mẹo vặt khoa học đời sống / nhà bếp 60s** (5 pha thí nghiệm Toàn – Trung – Cận trên đảo bếp cùng Host nam đeo mic) | `04_KENH_MEO_VAT_KHOA_HOC_HOST_ANH_TUAN/`<br>• SOP: `HUONG_DAN_SOP_CHI_TIET_MEO_VAT_60S.md` & `HUONG_DAN_TOAN_TRUNG_CAN_SPEED_RAMPING.md` | • `Du_An_Kenh_Meo_Vat_Workspace/src/Video/61_RND_Fashion_KOL_Blazer_ColorPalette/` (`VIDEO_FULL_FACEBOOK_REELS_SHOPEE_FASHION.mp4`, `VIDEO_HOAN_CHINH_SHOPEE_BABYDOLL_SPLIT_SCREEN.mp4`) | • `scripts_python/run_master_timeline_export_sync.py`<br>• `setup_mpemba_project.py`<br>• Nam: `elevenlabs_6adFm46eyy74snVn6YrT` (*Kiến Thức Nam*) |
| **05** | **Decor cải tạo góc làm việc, ban công, phòng ngủ tối giản & dọn dẹp chữa lành** (`Before -> Process -> After`) | `05_KENH_DECOR_KHONG_GIAN_CHUA_LANH/`<br>• SOP: `HUONG_DAN_SOP_CHI_TIET_DECOR_KHONG_GIAN.md` | • `VIDEO_MAU_DECOR_GOC_BAN_LAM_VIEC_CHUA_LANH_916.mp4` | • `scripts_python/render_decor_healing_video.py`<br>• Nữ: `elevenlabs_CQAD6iKxS73fEAGjSwt5` / Nam: `KVzG2JMdZJKi6y7cwERP` |
| **06** | **Thể thao dáng đẹp, tập Gym / xà đơn Calisthenics công viên ban đêm** bắt nhạc sôi động | `06_KENH_THE_THAO_DANG_DEP_CALISTHENICS/`<br>• SOP: `HUONG_DAN_SOP_CHI_TIET_THE_THAO_DANG_DEP.md` | • `VIDEO_THE_THAO_CO_GAI_TAP_XA_BAN_DEM_KHONG_BIEN_HINH_916.mp4` | • `scripts_python/render_night_calisthenics_sport_video.py`<br>• Nhạc Gym/Dance Remix 125 BPM (hoặc `aN7cv9yXNrfIR87bDmyD`) |
| **07** | **KOC thực chiến review & lắp đặt phụ kiện ngoại thất ô tô 7 góc quay** (test độ dẻo, bắt vít lỗ zin, test cản nước mưa kiểu *Long Gara*) | `07_KENH_O_TO_KOC_REVIEW_LAP_DAT_PHU_KIEN_NGOAI_THAT/`<br>• SOP: `HUONG_DAN_SOP_CHI_TIET_KENH_KOC_PHU_KIEN_O_TO.md` | • `VIDEO_05_REVIEW_CHAN_BUN_O_TO_7_GOC_QUAY_THAT_100.mp4`<br>• `VIDEO_05_REVIEW_CHAN_BUN_O_TO_7_GOC_QUAY_CLEAN_NO_SUB.mp4` | • `scripts_python/render_mudguard_koc_video.py`<br>• Nam: `elevenlabs_6adFm46eyy74snVn6YrT` + SFX nước bắn thật |
| **08** | **Mẹo lái xe / lùi chuồng / căn lề thực chiến `Dual-View PiP`** (Góc cao đuôi xe + Khung tròn xoay vô-lăng đồng bộ + Gương cầu lồi 360°) | `08_KENH_MEO_LAI_XE_DUAL_PIP_GOC_CAO_VO_LANG/`<br>• SOP: `HUONG_DAN_SOP_CHI_TIET_KENH_MEO_LAI_XE_DUAL_PIP.md` | • `VIDEO_01_MEO_LUI_XE_NGO_HEP_DUAL_PIP_7_GOC_LOGIC_100.mp4`<br>• `VIDEO_01_MEO_LUI_XE_NGO_HEP_DUAL_PIP_CLEAN_NO_SUB.mp4` | • `scripts_python/render_meolui_dual_pip_video.py`<br>• Nam: `elevenlabs_6adFm46eyy74snVn6YrT` (*Kiến Thức Nam*) |
| **09** | **DIY sáng tạo nghệ thuật, thủ công Mẹ & Bé và họa cụ** (làm tranh lá cây/vỏ cây/đất sét 7–8 bước kế thừa, xuất kép Giọng hướng dẫn + ASMR) | `09_KENH_DIY_NGHE_THUAT_VA_HOA_CU_SANG_TAO/`<br>• SOP: `HUONG_DAN_SOP_CHI_TIET_KENH_DIY_NGHE_THUAT.md` | • `VIDEO_01_DIY_NHIM_LA_THU_VA_BUT_MAU_ACRYLIC_7_BUOC_LOGIC_100.mp4`<br>• `VIDEO_02A/02B_TRANH_VO_CAY_MAY_BAM_HOA_LA_...mp4`<br>• `VIDEO_03A/03B_TRANH_LA_THU_EM_BE_AO_MUA_...mp4`<br>• `VIDEO_04A/04B_TRANH_HUOU_CAO_CO_VO_DAU_PHONG_...mp4`<br>• `VIDEO_05A/05B_TRANH_CAY_TUYET_3D_GIAY_AN_DAT_SET_...mp4` | • `scripts_python/render_diy_leaf_hedgehog_video.py` & `render_diy_type1..4_*.py`<br>• Bản A: `elevenlabs_CQAD6iKxS73fEAGjSwt5` / Bản B: Nhạc DIY + ASMR |
| **10** | **Học Tiếng Anh gia đình / trẻ em 3D Pixar Flashcard + Q&A + MV bài hát ôn tập Suno AI** (kiểu *Bé Nói English* / Affiliate *Kyna English*) | `10_KENH_HOC_TIENG_ANH_GIA_DINH_3D_FLASHCARD_KYNA/`<br>• SOP: `SOP_KENH_10_HOC_TIENG_ANH_GIA_DINH_3D_FLASHCARD_KYNA.md` | • `VIDEO_01_HOC_TIENG_ANH_DO_DUNG_TRONG_NHA_3D_FLASHCARD.mp4`<br>• `VIDEO_01_V2_TIENG_ANH_MY_KEM_VI_DU_QA_HANG_NGAY.mp4`<br>• `VIDEO_01_V3_STORY_KEM_BAI_HAT_SUNO_AI.mp4`<br>• `MV_BAI_HAT_ON_TAP_TU_VUNG_SUNO_AI.mp4`<br>• `PREVIEW_6_CANH_FLASHCARD_V2_QA.jpg`, `PREVIEW_V3_STORY_KEM_BAI_HAT_SUNO_AI.jpg` | • `scripts_python/render_english_household_vocab_v2.py` & `build_v3_story_plus_suno_song.py`<br>• Giữ giọng đa nhân vật gốc **Google Flow (`Veo 3.1 Lite`)** + Nhạc hát **`suno.com/create`** |
| **11** | **Cờ vua 3D kịch tính, thí Hậu săn Vua & giải mã ván cờ lịch sử** (kiểu *Forgiro Reels* + Affiliate Bộ cờ vua nam châm) | `11_KENH_CO_VUA_3D_KICH_TINH_FORGIRO/`<br>• SOP: `SOP_KENH_11_CO_VUA_3D_KICH_TINH_FORGIRO.md` & `HUONG_DAN_SAN_XUAT_KENH_CO_VUA_3D_FORGIRO.md` | • `VIDEO_01_CO_VUA_3D_OPERA_1858_THI_HAU_CHIEU_HET.mp4`<br>• `VIDEO_02_CO_VUA_3D_LASKER_1912_THI_HAU_SAN_VUA_DOC_BAN_CO.mp4`<br>• `PREVIEW_CHESS_3D_FORGIRO_OPERA_1858.jpg`, `PREVIEW_VIDEO_02_CUOC_DI_SAN_VUA_DEN_LASKER_1912.jpg` | • Engine: `assets/chess_reel_3d.html` (`Three.js WebGL 8x8`)<br>• Script: `build_and_render_video_02_lasker_1912.py`<br>• Nam Epic: `elevenlabs_3VnrjnYrskPMDsapTr8X` (*Tùng Đặng*) |

---

## 3. Ma Trận Tâm Lý Khán Giả & Chiến Lược Chọn Sản Phẩm Affiliate Chốt Đơn

| Nhóm Kênh Mẫu | Đặc Điểm Nội Dung | Nhân Khẩu Học Người Xem Thật | Nhóm Sản Phẩm Chốt Đơn Đúng Tệp |
| :--- | :--- | :--- | :--- |
| **`sport_music` (Kênh 06)** | Nữ/Nam tập xà đơn Calisthenics, chạy bộ, đạp xe, Pickleball trên nhạc sôi động. | **65% – 85% là NAM GIỚI** *(tuyệt đối không bán váy đầm nữ!)* | Kính mát phân cực UV400, tai nghe Open-Ear chống nước, vợt Pickleball Carbon T700, bình giữ nhiệt 1L, súng massage cơ mini, tất chống trượt. |
| **`dance_music` & KOL Fashion (Kênh 02, 03)** | Nữ nhảy bắt beat hoặc review chất vải kèm bảng màu HEX + `[● REC 4K]`. | **70% – 80% Nữ Gen-Z (16–26t)** | Set OOTD (đồ ngủ lụa, sườn xám, sơ mi chân váy, set dạ Tweed, babydoll, blazer), túi kẹp nách, kẹp tóc, sneaker độn đế. |
| **`viral_tips` & Decor / DIY (Kênh 04, 05, 09)** | Thí nghiệm mẹo vặt 5 pha, cải tạo góc phòng chữa lành, tranh DIY 8 bước. | **65% – 80% Nội trợ, Phụ huynh Mẹ & Bé, Dân văn phòng** | Chai xịt tẩy cặn canxi, băng keo chống thấm, đèn/kệ gỗ decor tối giản, bộ 60 bút Acrylic Marker, bộ máy bấm hoa văn giấy, bút kéo keo con lăn. |
| **KOC Ô Tô & Lái Xe (Kênh 01, 07, 08)** | Tư vấn cabin, lắp phụ kiện 7 góc quay, mẹo lùi xe `Dual-View PiP`. | **25 – 48 tuổi**, chủ xe ô tô có thu nhập | Chắn bùn dẻo lỗ zin, gương cầu lồi xóa điểm mù 360°, bơm lốp tự ngắt, camera hành trình, sáp thơm/phụ kiện cabin. |
| **Giáo Dục Gia Đình 3D (Kênh 10)** | Gia đình 3D Pixar hỏi đáp từ vựng + IPA + bài hát ôn tập Suno (`Sell to the Parent`). | **Phụ huynh có con 3 – 11 tuổi** *(định hướng CTA tới Ba/Mẹ ở bình luận ghim)* | Khóa học Tiếng Anh 1-kèm-1 chuẩn Cambridge (*Kyna English*), bộ thẻ Flashcard song ngữ, bút chấm đọc thông minh, sách tranh tiếng Anh. |
| **Cờ Vua & Trí Tuệ 3D (Kênh 11)** | Giải mã đòn thí Hậu / chiếu hết lịch sử trên bàn cờ gỗ 3D nghiêng `42°`. | **Học sinh, Sinh viên, Phụ huynh & Người yêu thích tư duy chiến thuật** | Bộ cờ vua nam châm từ tính gấp gọn (có 2 Hậu phong cấp), đồng hồ thi đấu cờ vua, sách khai cuộc & chiến thuật cờ vua. |

---

## 4. Bảng Tra Nhanh Mã Giọng Đọc Miễn Phí & Cao Cấp (`Gender Lock 100%`)

- **Miễn phí 100% không cần API Key (`Edge-TTS`):**
  - Nữ Tiếng Việt: `edge_vi-VN-HoaiMyNeural` | Nam Tiếng Việt: `edge_vi-VN-NamMinhNeural`
  - Nữ Tiếng Anh: `edge_en-US-AvaNeural`, `edge_en-US-EmmaNeural` | Nam Tiếng Anh: `edge_en-US-AndrewNeural`, `edge_en-US-BrianNeural`
- **Cao cấp qua `ai33.pro` (`OpenSpeaker v3`) & Google Flow:**
  - Nữ Tiếng Việt: `elevenlabs_CQAD6iKxS73fEAGjSwt5` (*Giang Podcast*), `elevenlabs_Jmio6r8OUeqiK3cZ3N0K` (*Thu Thảo Story*), `elevenlabs_aN7cv9yXNrfIR87bDmyD` (*Ngọc Huyền*), `vbee_category_advertise` (*Vbee Nữ Bán Hàng*).
  - Nam Tiếng Việt: `elevenlabs_6adFm46eyy74snVn6YrT` (*Kiến Thức Nam*), `elevenlabs_3VnrjnYrskPMDsapTr8X` (*Tùng Đặng — Deep, Resonant, Epic* cho Cờ vua/Lịch sử), `elevenlabs_KVzG2JMdZJKi6y7cwERP` (*Quang Nguyễn*), `elevenlabs_CxJbDdwqY48MY3gPVYwe` (*Đỗ Trịnh*).
  - Đa nhân vật Việt – Anh tự nhiên (Kênh 10): Giữ nguyên âm thanh thoại gốc đa nhân vật từ **Google Flow (`Veo 3.1 Lite`)**.
*(Bảng tra cứu đầy đủ tại: `E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Nghien_Cuu_Kenh_Moi_Huong_Dan\BANG_TRA_CUU_GIONG_DOC_AI33_VI_EN.md`).*
