---
name: web-wp-seo-sop
description: "SOP Team 2: Quy trình phát triển WordPress/Flatsome, Landing Page VIP, HTML sang Webcake (.pke) và kiểm toán SEO/GEO kèm QA 2 tầng."
---

# SOP Team 2 — Web, WordPress, Landing Page & SEO (`team-web-wordpress-seo`)

## 1. Nhân Sự Cố Định
- **`web-wp-builder`**: Xây dựng & sửa lỗi WordPress/Flatsome (`wordpress-flatsome-designer`, PHP, WooCommerce, UX Builder, WP-CLI).
- **`web-landingpage-coder`**: Dựng Landing Page VIP (`design-landingpage-vip-v2`: 138 icon SVG, Liquid Glass, form + VietQR + webhook CAPI) & chuyển HTML sang Webcake `.pke` (`html-to-webcake`).
- **`web-seo-geo-specialist`**: Kiểm toán & triển khai SEO/GEO (`claude-seo`, Technical SEO, Schema JSON-LD, E-E-A-T, Local SEO, AI Overviews).
- **`web-performance-auditor`**: Kiểm toán độc lập HTTP 200, lỗi PHP/JS console, Schema hợp lệ, tốc độ tải & checklist 80 điểm Flatsome (chỉ đọc & test — không sửa code).

## 2. Sổ Tay Kinh Nghiệm
Luôn đọc [learned_patterns.md](./references/learned_patterns.md) trước khi chỉnh sửa WordPress/Landing Page.

## 🧠 Bộ Nhớ Dài Hạn & Kho Tri Thức Ghim Cứng (Javis Bridge)
- **Trưởng nhóm (Leader):** `web-wp-builder` | **Bộ nhớ riêng:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-web-wordpress-seo\MEMORY.md`
- **Đầu ca đọc bộ nhớ & nhật ký chạy:**
  ```powershell
  & "python" "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py" --read team-web-wordpress-seo
  ```
- **Cuối ca ghi nhận kết quả & bài học:** dùng `--log-run team-web-wordpress-seo ...` và `--learn team-web-wordpress-seo --lesson "..."`.
- **Tra cứu Javis Wiki/Sources:** `--search-wiki "<từ_khóa>"` hoặc đọc trực tiếp tài liệu ghim cứng:
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\sources\phong-2-web-seo-ads\bao-cao-audit-seo-infoasia.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\sources\phong-2-web-seo-ads\ma-tran-ke-hoach-content-seo.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\sources\phong-4-hoc-vien-lms\ban-thiet-ke-he-thong-web-ban-khoa-hoc-lms.md`
- **Chạy dây chuyền 4 pha chuẩn Javis (`plan → work → verify+retry → memory`):** gọi `run_workflow` với `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py` (`Args: {"team": "team-web-wordpress-seo", "goal": "..."}`).
