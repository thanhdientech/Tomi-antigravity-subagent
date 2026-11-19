---
name: web-research-sop
description: "Quy trình chuẩn (SOP) tìm kiếm, kiểm chứng nguồn 4 tọa độ (chống ảo giác AI) và biên tập báo cáo 3 tầng với 3 subagent cố định."
---

# SOP Điều Phối Nhóm 5 — Tra Cứu & Kiểm Chứng Thông Tin Web

## 1. Danh Sách 3 Nhân Sự Cố Định Trong Nhóm

| Subagent (`TypeName`) | Phạm vi phụ trách | Quyền thao tác |
| :--- | :--- | :--- |
| `web-search-scout` | Săn nguồn chính thống (Docs hãng, luật, báo chí/học thuật Tier 1–2), thu thập dữ kiện gốc & kiểm tra URL sống `HTTP 200` | `search_web`, `read_file`, `run_command` |
| `web-fact-checker` | Kiểm toán độc lập toàn bộ dữ kiện & nguồn từ Scout: đối chiếu chéo ≥ 2 nguồn, xác minh đủ 4 tọa độ + trích nguyên văn ≤ 25 từ, chấm nhãn `🟢/🟡/🔴` | `read_file`, `run_command`, `search_web` |
| `web-synthesis-editor` | Biên tập báo cáo sạch chuẩn 3 tầng từ dữ liệu đã qua Fact-Check (Tầng 1 sạch, Tầng 2 tài liệu tham chiếu, Tầng 3 bảng kiểm chứng 6 cột) | `read_file`, `write_file` |

*(Ghi chú: Khi cần vào trang web render bằng JavaScript, yêu cầu cuộn trang hoặc tương tác trực tiếp mà `search_web` không lấy được nội dung, điều phối viên kết hợp gọi thêm subagent `browser` có sẵn của Antigravity.)*

## 2. Quy Trình 4 Bước Bắt Buộc

1. **Đọc sổ tay lỗi tra cứu:** Mở [learned_patterns.md](./references/learned_patterns.md).
2. **Săn nguồn (`web-search-scout`):** Tìm tối thiểu 2 nguồn chính thống độc lập, kiểm tra HTTP 200 và trích đúng câu gốc.
3. **Kiểm toán độc lập (`web-fact-checker`):** Xác minh link sống, phát hiện thông tin hết hiệu lực/mâu thuẫn giữa các nguồn, gắn nhãn độ tin cậy `🟢 / 🟡 / 🔴`.
4. **Biên tập chuẩn 3 tầng (`web-synthesis-editor`):** Xuất bài/báo cáo sạch cho người dùng và tách riêng bảng kiểm chứng 6 cột.

## 3. Chạy Dây Chuyền Tự Động Bằng Python Workflow

Chạy trọn dây chuyền **Scout → Fact-Checker → Synthesis Editor** theo schema JSON cố định bằng công cụ `run_workflow` với file mẫu [verified_research_pipeline.py](./workflows/verified_research_pipeline.py).

## 🧠 Bộ Nhớ Dài Hạn & Kho Tri Thức Ghim Cứng (Javis Bridge)
- **Trưởng nhóm (Leader):** `web-search-scout` | **Bộ nhớ riêng:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-web-research\MEMORY.md`
- **Đầu ca đọc bộ nhớ & nhật ký chạy:**
  ```powershell
  & "python" "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py" --read team-web-research
  ```
- **Cuối ca ghi nhận kết quả & bài học:** dùng `--log-run team-web-research ...` và `--learn team-web-research --lesson "..."`.
- **Tra cứu Javis Wiki/Sources:** `--search-wiki "<từ_khóa>"` hoặc đọc trực tiếp tài liệu ghim cứng:
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\index.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\wiki\quy-trinh-rang-buoc-chong-ao-giac-ai.md`
- `%JAVIS_BRAIN_DIR%\brains\Brain Default\sources\phong-5-tu-vi-bat-tu\master-prompt-luan-giai-tu-vi-bat-tu-toan-dien.md`
- **Chạy dây chuyền 4 pha chuẩn Javis (`plan → work → verify+retry → memory`):** gọi `run_workflow` với `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py` (`Args: {"team": "team-web-research", "goal": "..."}`).
