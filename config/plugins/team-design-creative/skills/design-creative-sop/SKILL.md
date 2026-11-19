---
name: design-creative-sop
description: "SOP Team 3 (Design): Điều phối 4 subagent cho Logo SVG/CIP/In ấn, UI/UX 192 ngành, tài sản hình ảnh/GSAP và kiểm toán UX/CRO."
---

# SOP Team 3 — Design, Thương Hiệu & UI/UX (`team-design-creative`)

## 1. Nhân Sự Cố Định Trong Team 3
- **`design-brand-identity`**: Logo SVG, bộ nhận diện CIP, Banner Ads, Báo giá, Tạp chí & dàn trang in ấn PDF/DOCX/PPTX/Typst (`brand-editorial-graphic-studio`).
- **`design-ui-ux-architect`**: Kiến trúc UI/UX 192 ngành, 79 UI styles, 84 hệ `DESIGN.md` (`ui-ux-design-pro-max`) và luồng tương tác Web App / Admin / ERP / Mobile App (`webapp-app-ux-workflow`).
- **`design-visual-asset-creator`**: Tạo ảnh minh họa/banner/mockup qua subagent `image-generator` và lập trình hiệu ứng chuyển động web 60fps (`gsap-skills`).
- **`design-ux-cro-auditor`**: Kiểm toán độc lập logic UI/UX, Responsive đa khung hình, WCAG 2.2 & CRO Landing Page (`ui-ux-cro-auditor` — chỉ kiểm, không sửa).

## 2. Sổ Tay Kinh Nghiệm
Đọc [learned_patterns.md](./references/learned_patterns.md) trước khi dàn trang hoặc xuất tài liệu thiết kế.

## 🧠 Bộ Nhớ Dài Hạn & Kho Tri Thức Ghim Cứng (Javis Bridge)
- **Trưởng nhóm (Leader):** `design-ui-ux-architect` | **Bộ nhớ riêng:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-design-creative\MEMORY.md`
- **Đầu ca đọc bộ nhớ & nhật ký chạy:**
  ```powershell
  & "python" "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py" --read team-design-creative
  ```
- **Cuối ca ghi nhận kết quả & bài học:** dùng `--log-run team-design-creative ...` và `--learn team-design-creative --lesson "..."`.
- **Tra cứu Javis Wiki/Sources:** `--search-wiki "<từ_khóa>"` hoặc đọc trực tiếp tài liệu ghim cứng:
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\channel-branding-3-kenh-youtube.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\template-khai-bao-channel-branding-kenh-moi.md`
- **Chạy dây chuyền 4 pha chuẩn Javis (`plan → work → verify+retry → memory`):** gọi `run_workflow` với `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py` (`Args: {"team": "team-design-creative", "goal": "..."}`).
