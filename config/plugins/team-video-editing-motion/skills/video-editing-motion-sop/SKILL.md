---
name: video-editing-motion-sop
description: "SOP Team 5 (Edit & Motion): Điều phối 4 subagent cho Edit FFmpeg/Studio, Motion Code (Remotion/Manim), Recordly và QA MP4."
---

# SOP Team 5 — Edit Video, Motion & Hậu Kỳ (`team-video-editing-motion`)

## 1. Nhân Sự Cố Định Trong Team 5
- **`video-editor-ffmpeg`**: Edit video local `ai-video-studio` `:5186` (28 style HTML→MP4, ~200 HyperFrames, ~90 template, lồng tiếng AI) + `create-and-edit-video` (Auto-Editor, Editly, FFmpeg, xuất TikTok/YT/FB hàng loạt).
- **`video-motion-coder`**: Lập trình video bằng code: `Remotion`, `Motion Canvas`, `Manim`, `kinetic-reel` (Canvas 2D / Three.js khớp nhịp nhạc) và `painted-animation` (p5.js + p5.brush màu nước).
- **`video-tutorial-producer`**: Quay & biên tập video hướng dẫn chức năng (`recordly-tutorial-ai`: giọng đọc AI, phụ đề `.SRT`, Auto-Zoom).
- **`video-qa-verifier`**: Kiểm toán hậu kỳ độc lập (`ffprobe` + kiểm tra `.SRT` UTF-8 + trích frame PNG mở đọc bằng `read_file` — không tự sửa file gốc).

## 2. Sổ Tay Kinh Nghiệm
Đọc [learned_patterns.md](./references/learned_patterns.md) trước khi render hàng loạt.

## 🧠 Bộ Nhớ Dài Hạn & Kho Tri Thức Ghim Cứng (Javis Bridge)
- **Trưởng nhóm (Leader):** `video-editor-ffmpeg` | **Bộ nhớ riêng:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-video-editing-motion\MEMORY.md`
- **Đầu ca đọc bộ nhớ & nhật ký chạy:**
  ```powershell
  & "python" "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py" --read team-video-editing-motion
  ```
- **Cuối ca ghi nhận kết quả & bài học:** dùng `--log-run team-video-editing-motion ...` và `--learn team-video-editing-motion --lesson "..."`.
- **Tra cứu Javis Wiki/Sources:** `--search-wiki "<từ_khóa>"` hoặc đọc trực tiếp tài liệu ghim cứng:
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\kinh-nghiem-render-video-google-flow-va-muse-ai.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\cam-nang-giong-doc-tts-va-voice-call.md`
- **Chạy dây chuyền 4 pha chuẩn Javis (`plan → work → verify+retry → memory`):** gọi `run_workflow` với `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py` (`Args: {"team": "team-video-editing-motion", "goal": "..."}`).
