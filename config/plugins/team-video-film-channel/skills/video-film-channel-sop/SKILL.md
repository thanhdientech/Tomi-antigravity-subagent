---
name: video-film-channel-sop
description: "SOP Team 4 (Phim AI & Kênh MXH): Điều phối 4 subagent cho Biên kịch, Đạo diễn Prompt, Studio (:8500/:8600) và Tự động hóa kênh."
---

# SOP Team 4 — Sản Xuất Phim AI & Xây Kênh MXH (`team-video-film-channel`)

## 1. Nhân Sự Cố Định Trong Team 4
- **`film-scriptwriter`**: Biên kịch đa thể loại (`video-storytelling`, `viet-kich-ban-drama`, `shopee-affiliate-video-studio`).
- **`film-prompt-director`**: Đạo diễn prompt điện ảnh & CSV (`cinematic-video-prompt`, `viet-prompt-lam-phim-drama`, `lam-phim-video-master`).
- **`film-studio-producer`**: Điều khiển OmniFlow Studio `:8500` (`renderlongytb` — video dài 16:9) & Shopee KOL Studio `:8600` (`rendershortvideo` — video ngắn 9:16).
- **`channel-growth-automation`**: Điều khiển dây chuyền xây kênh (`yt-shortcode-commander`) & tự động hóa trình duyệt đa profile (`antigravity-browser-controller`).

## 2. Sổ Tay Kinh Nghiệm
Đọc [learned_patterns.md](./references/learned_patterns.md) trước khi xuất CSV hoặc chạy auto-post.

## 🧠 Bộ Nhớ Dài Hạn & Kho Tri Thức Ghim Cứng (Javis Bridge)
- **Trưởng nhóm (Leader):** `film-scriptwriter` | **Bộ nhớ riêng:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-video-film-channel\MEMORY.md`
- **Đầu ca đọc bộ nhớ & nhật ký chạy:**
  ```powershell
  & "python" "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py" --read team-video-film-channel
  ```
- **Cuối ca ghi nhận kết quả & bài học:** dùng `--log-run team-video-film-channel ...` và `--learn team-video-film-channel --lesson "..."`.
- **Tra cứu Javis Wiki/Sources:** `--search-wiki "<từ_khóa>"` hoặc đọc trực tiếp tài liệu ghim cứng:
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\quy-trinh-auto-youtube-a-den-z-2026.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\cam-nang-chuan-bi-xay-kenh-youtube-cho-nguoi-moi.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\kinh-nghiem-render-video-google-flow-va-muse-ai.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\nhat-ky-van-hanh-auto-youtube.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\dac-ta-ky-thuat-video-02-every-myth-explained.md`
- *(+1 tài liệu khác trong `team_memory/WIKI_BRIDGE.md`)*
- **Chạy dây chuyền 4 pha chuẩn Javis (`plan → work → verify+retry → memory`):** gọi `run_workflow` với `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py` (`Args: {"team": "team-video-film-channel", "goal": "..."}`).
