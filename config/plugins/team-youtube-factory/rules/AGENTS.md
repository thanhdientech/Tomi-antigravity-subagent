# Luật Vận Hành Team 12 — Nhà Máy Sản Xuất YouTube Đa Ngách (`team-youtube-factory`)

Toàn bộ 5 thành viên (`yt-niche-radar`, `yt-content-writer`, `yt-prompt-director`, `yt-omniflash-renderer`, `yt-production-qa`) bắt buộc tuân thủ 5 thiết luật sau khi vận hành tại `E:\DIEN APP\Xây Kênh Youtube\`:

1. **1 Nhà Máy — Đọc Cấu Hình Riêng Từng Kênh (`Data-Driven Channel Lock`):**
   - Trước khi viết nội dung, viết prompt hoặc render cho bất kỳ video nào, bắt buộc đọc đúng `channel_config.json`, `1 Viet Content\MASTER_PROMPT_*.md`, `2 Viet Prompt\HUONG_DAN_VIET_PROMPT_*.md`, `3 Render video\AGENTS.md`, `Channel_Branding\` và `flow_config.json` của **chính kênh đó**.
   - Tuyệt đối không trộn phong cách hình ảnh, Voice ID hoặc từ khóa giữa các ngách/kênh anh em (`zero_overlap_with_sibling_channels`).
2. **Đúng Môi Trường Python Cho Đúng Tool (Cấm Nhầm `.venv`):**
   - Quét ngách (`Tim Ngach\agent_cli.py`): dùng **Python313** (`python`, đã có sẵn `scrapetube`) và **LUÔN `cd` vào `E:\DIEN APP\Xây Kênh Youtube\Tim Ngach\WebApp`** rồi chạy `..\agent_cli.py` (để tìm đúng `database/config.json`).
   - Render OmniFlash (`flow_batch.py`, `flow_ui_batch`, `flow_tts.py`, `flowmusic_batch.py`, `qa_audio_sync_merge.py`, `super_merge.py`): **BẮT BUỘC** dùng `E:\DIEN APP\Xây Kênh Youtube\Tool render edit Video\.venv\Scripts\python.exe` và **LUÔN `cd` vào `E:\DIEN APP\Xây Kênh Youtube\Tool render edit Video`** trước khi chạy (KHÔNG dùng Python313 hệ thống chạy OmniFlash).
   - Script kiểm định nhẹ / `team_memory_cli.py` / `ffprobe` / `rebuild_srt`: dùng `python`.
3. **Không Bịa Đặt Số Liệu & Tuân Thủ YPP (`Zero Hallucination & YPP Lock`):**
   - Mọi đánh giá ngách (view, tỷ lệ kênh mới `30–47%`, RPM/CPM, đối thủ) bắt buộc trích từ JSON thật trong `Tim Ngach\WebApp\database\` hoặc chạy `agent_cli.py` — tuân thủ `Tim Ngach\Khongbiadat.md` và `YPP-Policy-Inauthentic-Content.md`.
   - Áp dụng đúng bản đồ 4 Cấp độ (`Cấp 0` → `Cấp 3`) và chiến lược **Phương án A (1 Ngách Mẹ → 3 Kênh Ngách Con)** từ `TAI_LIEU_TONG_HOP_XAY_KENH_YOUTUBE_NGUOI_MOI_A_Z_2026.md`.
4. **Cấm Gán Prompt Ẩu & Khóa Chuẩn `utf-8-sig` + SRT 8s/Cảnh:**
   - Mọi file `.csv`, `.srt`, `.txt` bắt buộc mã hóa `utf-8-sig` (`$env:PYTHONIOENCODING="utf-8"`).
   - Viết prompt cuốn chiếu 25–30 cảnh/lượt, khóa nhất quán `{uid01}..{uid06}`, biến thiên thời lượng tự nhiên giữa các tập (lệch `>= 25–45s`, trên 8 phút để bật Mid-roll Ads), và chặn đứng lỗi lệch timestamp SRT (`1.5s/câu` thay vì `~8s/câu`).
5. **Tách Vai Sản Xuất & Vai Kiểm Toán Độc Lập (`No Self-Grading`):**
   - `yt-production-qa` là kiểm toán viên độc lập (chỉ đọc & chạy script kiểm chứng, **CẤM** `edit_file`/`write_file` vào sản phẩm): bắt buộc chốt QA **2 lần** — (a) **Pre-Render QA** trước khi chạy Veo/TTS tốn credit, và (b) **Post-Render QA** (`ffprobe` + mở đọc trực tiếp ảnh Thumbnail & 3 frame MP4 bằng `read_file`).
