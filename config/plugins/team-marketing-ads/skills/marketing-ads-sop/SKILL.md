---
name: marketing-ads-sop
description: "SOP Team 9 (Marketing & Ads): Điều phối 3 subagent cho Chân dung 9 phần, Google/Meta Ads & CRO, và Copywriting/Sản phẩm số."
---

# SOP Team 9 — Marketing, Quảng Cáo & Sản Phẩm Số (`team-marketing-ads`)

## 1. Nhân Sự Cố Định Trong Team 9
- **`mkt-persona-strategist`**: Phân tích chân dung khách hàng 9 phần (`chan-dung-khach-hang-9-phan`), phễu THU–NUÔI–CHỐT và góc bán hàng.
- **`ads-performance-specialist`**: Siêu Hub 12 skill Google Ads & CRO (`google-ads-master`: từ khóa, tracking, audit A1–A14, Search/PMax, ROAS, Google Ads Editor CSV).
- **`mkt-copy-offer-creator`**: Viết content bán hàng/quảng cáo theo 14 công thức (`cong-thuc-viet-content-by-noti-v4`) & đồng hành tạo sản phẩm số (`tao-san-pham-so-bang-ai`).

## 2. Sổ Tay Kinh Nghiệm
Đọc [learned_patterns.md](./references/learned_patterns.md) trước khi xuất file Google Ads Editor CSV hoặc chiến dịch mới.

## 🧠 Bộ Nhớ Dài Hạn & Kho Tri Thức Ghim Cứng (Javis Bridge)
- **Trưởng nhóm (Leader):** `mkt-persona-strategist` | **Bộ nhớ riêng:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-marketing-ads\MEMORY.md`
- **Đầu ca đọc bộ nhớ & nhật ký chạy:**
  ```powershell
  & "python" "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py" --read team-marketing-ads
  ```
- **Cuối ca ghi nhận kết quả & bài học:** dùng `--log-run team-marketing-ads ...` và `--learn team-marketing-ads --lesson "..."`.
- **Tra cứu Javis Wiki/Sources:** `--search-wiki "<từ_khóa>"` hoặc đọc trực tiếp tài liệu ghim cứng:
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\opc-doanh-nghiep-khong-nhan-vien.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\tao-san-pham-so-bang-ai-7-ngay.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\bo-30-prompt-san-pham-so.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\7-template-ban-ve-doanh-nghiep-opc.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\chan-dung-khach-hang-mua-khoa-hoc-va-tool.md`
- *(+2 tài liệu khác trong `team_memory/WIKI_BRIDGE.md`)*
- **Chạy dây chuyền 4 pha chuẩn Javis (`plan → work → verify+retry → memory`):** gọi `run_workflow` với `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py` (`Args: {"team": "team-marketing-ads", "goal": "..."}`).
