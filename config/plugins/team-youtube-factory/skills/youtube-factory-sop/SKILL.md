---
name: youtube-factory-sop
description: "SOP Team 12 (YouTube Đa Ngách): Quy trình 5 giai đoạn khép kín Tim Ngach Radar + OmniFlash 16:9 cho mọi ngách/kênh YouTube."
---

# SOP TEAM 12 — NHÀ MÁY SẢN XUẤT YOUTUBE ĐA NGÁCH (`team-youtube-factory`)

## 1. Kiến Trúc "1 Nhà Máy — N Ngách / N Kênh"
Toàn bộ các ngách tại `E:\DIEN APP\Xây Kênh Youtube\` (Ngách 01 `01_Ngach_Khao_Co_Va_Huyen_Thoai_US`, Ngách 02 `02_Ngach_KosmosGeist_Sleep_Science_US`, và mọi ngách mới sau này) dùng chung 1 dây chuyền 5 Subagent:

```text
[1. yt-niche-radar (LEADER)]  -> Quét số liệu thật (Tim Ngach) + Tư vấn Cấp 0..3 + Chốt đề tài / tạo channel_config.json
             │
             ▼
[2. yt-content-writer]        -> Đọc channel_config.json & MASTER_PROMPT -> Xuất 0 Noi dung video/ + 5 srt/ (chuẩn 8s/cảnh)
             │
             ▼
[3. yt-prompt-director]       -> Đọc HUONG_DAN_VIET_PROMPT & ảnh mẫu -> Xuất B2, B3 ({uid01}), B5, B9, B8 (utf-8-sig)
             │
             ▼
[4a. yt-production-qa]        -> PRE-RENDER QA (Độc lập): Đếm dòng CSV=SRT, check 8s/cảnh, utf-8-sig, YPP -> PASS mới Render!
             │
             ▼
[4b. yt-omniflash-renderer]   -> Render .venv 3.12 OmniFlash: B2 -> B3 -> B4-5 (Veo 8s) -> B6 (TTS) -> B9 (BGM) -> B12 (Merge)
             │
             ▼
[5. yt-production-qa]         -> POST-RENDER QA (Độc lập): ffprobe + trích 3 frame MP4 + mở đọc 6 Thumbnail bằng read_file -> PASS!
```

## 2. Đường Dẫn Công Cụ & Tài Liệu Gốc (Đã Xác Minh)
- **Thư mục gốc YouTube:** `E:\DIEN APP\Xây Kênh Youtube\`
- **Cẩm nang chiến lược A–Z 2026:** `E:\DIEN APP\Xây Kênh Youtube\TAI_LIEU_TONG_HOP_XAY_KENH_YOUTUBE_NGUOI_MOI_A_Z_2026.md`
- **Kế hoạch triển khai mẫu OmniFlash:** `E:\DIEN APP\Xây Kênh Youtube\ke hoach triển khai mau de hoc\KE_HOACH_TRIEN_KHAI_SAN_XUAT_VIDEO_YOUTUBE.md`
- **Tool Tìm Ngách (`YouTube Niche Radar V2.2`):**
  - Thư mục chạy (PHẢI `cd` vào đây trước khi chạy `..\agent_cli.py`): `E:\DIEN APP\Xây Kênh Youtube\Tim Ngach\WebApp`
  - Python (đã có `scrapetube`): `python`
  - CLI chính: `..\agent_cli.py` (`--action list_config | summary | video`)
  - Dữ liệu JSON đã quét: `WebApp\database\config.json`, `summary_*.json`, `videos_*.json`, `Ket qua kiem chung\`
- **Tool Render OmniFlash (Python 3.12 `.venv`):**
  - Thư mục gốc (PHẢI `cd` vào đây trước khi chạy): `E:\DIEN APP\Xây Kênh Youtube\Tool render edit Video`
  - Python venv: `E:\DIEN APP\Xây Kênh Youtube\Tool render edit Video\.venv\Scripts\python.exe`
  - Scripts chính: `omniflash\youtube\flow_batch.py`, `omniflash.youtube.flow_ui_batch`, `omniflash\youtube\flow_tts.py`, `omniflash\FlowMusic_Auto\flowmusic_batch.py`, `omniflash\youtube\qa_audio_sync_merge.py`, `omniflash\youtube\super_merge.py`

## 3. Bộ Nhớ Dài Hạn Cách Ly Từng Ngách (`MEMORY.md` Riêng — Cấm Trộn Ngách)
- **Bộ nhớ chung hạ tầng Team 12 (CHỈ lưu luật dùng chung `.venv`/CWD):** `%USERPROFILE%\.gemini\config\team_memory\teams\team-youtube-factory\MEMORY.md`
- **Bộ nhớ `MEMORY.md` riêng từng Ngách (trùng tên thư mục ngách trên ổ `E:`):**
  - `niches\01_Ngach_Khao_Co_Va_Huyen_Thoai_US\MEMORY.md` (3 kênh: Every Myth Explained, Before Us Decoded, Relics & Myths Forensics)
  - `niches\02_Ngach_KosmosGeist_Sleep_Science_US\MEMORY.md` (3 kênh: KosmosGeist, NeuroDrift, QuantumSlumber)
  - *(Ngách mới `03_Ngach_...` tự tạo `niches\<TEN_NGACH>\MEMORY.md` khi truyền `--niche`)*
- **Tra cứu & ghi bài học đúng Ngách bằng `team_memory_cli.py`:**
  ```powershell
  $PY = "python"
  $CLI = "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py"
  & $PY $CLI --list-niches team-youtube-factory
  & $PY $CLI --read team-youtube-factory --niche 02_Ngach_KosmosGeist_Sleep_Science_US
  & $PY $CLI --learn team-youtube-factory --niche 02_Ngach_KosmosGeist_Sleep_Science_US --lesson "..."
  ```

## 4. Đa Luồng An Toàn
- **Song song thoải mái:** Có thể chạy 2–4 bản sao `yt-content-writer` hoặc `yt-prompt-director` cho các video/kênh khác nhau (mỗi video 1 thư mục `src\Video\<STT>_<Ten>\` riêng).
- **Tuần tự / tách Profile khi Render:** Bước `yt-omniflash-renderer` giữ `threads: 2` (hoặc Wave-of-3 cho UI batch), `tts_threads: 4` (giảm xuống `2` nếu 429), và KHÔNG dùng chung 1 `flow_profile` cho 2 tiến trình render Google Flow cùng lúc.

## 5. Cổng Khóa Cứng Tự Động (Zero-Defect Render & Audit Gate — Bắt Buộc 100% Tập Mới)
Mọi tập video sản xuất bởi Team 12 bắt buộc đi qua **2 Cổng Tự Động (`Exit code 0`)** + **1 Cổng Mắt Thật Độc Lập** (dùng Python313 `python`):
1. **Cổng 1 — Pre-Render Hard Gate (Chặn trước khi tốn credit Veo/TTS/Suno):**
   ```powershell
   & $PY "E:\DIEN APP\Xây Kênh Youtube\Tool render edit Video\omniflash\youtube\qa_gate_youtube_factory.py" --video-dir "<Video_Dir>" --stage pre-render
   ```
   *(Chặn lệch số cảnh, thiếu Host `uid01`, trống Hook `B8`, ký tự ngoại lai Hán/Hindi, rác thẻ, câu quá dài).*
2. **Render Khóa Giọng + Thumbnail + Master Không Cắt Cụt:**
   - `flow_tts.py` đã tích hợp `[CHANNEL VOICE LOCK]` tự đọc `channel_config.json` của chính kênh đó (không bao giờ lấy nhầm giọng kênh anh em).
   - Phủ chữ Hook chuẩn `1920x1080` PNG thật & tự đồng bộ gói SEO bằng `omniflash\youtube\render_thumbnail_hooks.py --video-dir "<Video_Dir>"`.
   - `render_suno_bgm_and_single_voice_master.py` đã tích hợp **Zero Audio Truncation + Multi-Angle Optical Split + Auto Tail-Guard (`|MP4-SRT| <= 0.45s`)** và xuất thẳng sạch vào `FINAL/` + `GOI_UPLOAD_YOUTUBE_CHUAN_SEO_2026/` (không tạo rác `src/Video/.../FINAL/`).
3. **Cổng 2 — Post-Render Hard Gate + Independent Visual Eye Audit (`yt-production-qa`):**
   ```powershell
   & $PY "E:\DIEN APP\Xây Kênh Youtube\Tool render edit Video\omniflash\youtube\qa_gate_youtube_factory.py" --video-dir "<Video_Dir>" --stage post-render
   ```
   *(Chặn sai Voice ID, lệch `|MP4-SRT| > 0.5s`, biến thiên `< 25s` với tập trước, sai SHA-256 SEO, lệch Chapters `> 2.0s`, còn sót file cũ/backup/`.md` thừa trong gói SEO; bắt buộc kèm `read_file` soi mắt thật 6/6 Thumbnail & 4 Frame MP4 trước khi ký Grade A/B).*

## 6. Tối Ưu CTR, Hook & Retention Hậu Đăng (`yt-growth-optimizer`)
- Thư mục 6 công cụ offline (Python313, 0 dependency, MIT): `plugins\team-youtube-factory\skills\yt-growth-optimizer\scripts\`
  - **`swipe.py`** (`yt-niche-radar`): chấm bội số Outlier `>= 2.0x` so với median chính kênh đối thủ.
  - **`hookscore.py` + `hooks.json`** (`yt-content-writer`, `yt-production-qa`): chấm 5 trục Hook 15s đầu từ 21 công thức → giữ Top 2/5.
  - **`title.py`** (`yt-content-writer`, `yt-prompt-director`, `yt-production-qa`): lint cắt chữ Mobile `40` / Desktop `60`, **cấm lặp chữ giữa Title & Thumbnail**, trần `3` từ Thumbnail.
  - **`retention.py` & `deadair.py` & `chapters.py`** (`yt-production-qa`): đọc file `Audience retention.csv` từ YouTube Studio ghép `.srt` để bắt **Hook Leak**, **Cliffs** (đúng giây & câu nói), **Slide** và chốt 1 điểm sửa lớn nhất cho tập sau.
