# 📘 HƯỚNG DẪN TÌM, KIỂM TRA & NẠP REPO SKILL VÀO ANTIGRAVITY (TEAM 13 — `team-skill-curator`)

> **Phiên bản:** 1.0 · **Phòng ban phụ trách:** **Team 13 (`team-skill-curator`)** · **Cơ chế an toàn:** Tư vấn 3 Ngăn trước khi nạp + Khiên Bảo Mật 2 Cổng + Chỉ mục lai FTS5 (`agy-skill-hub`)

---

## 1. Tại Sao Phải Qua Team 13 Trước Khi Nạp Repo Skill Ngoài?

Khi anh tìm thấy 1 repo Skill / Agent hay trên GitHub (`skills.sh`, Anthropic, Google, cộng đồng Claude Code / Cursor...), **không nên copy thẳng vào `skills/`** vì 3 lý do:
1. **Chống mã độc & Prompt Injection:** Repo lạ có thể giấu lệnh xóa file, đánh cắp `.env`/SSH hoặc cài câu lệnh ẩn trong `SKILL.md`.
2. **Chống trùng lặp & nặng máy:** Máy đã có sẵn **41 Global Skills + 12 Teams** — nạp trùng sẽ làm loãng trigger và phình Context Window.
3. **Tự động chuyển đổi chuẩn Antigravity × Javis:** Tự sửa lỗi BOM, rút gọn `description <= 145` ký tự, đổi tên tool tương thích Antigravity và dựng lại chỉ mục tìm kiếm siêu nhanh `agy_skill_index.db`.

---

## 2. Quy Trình 4 Bước Người Dùng Thao Tác (Cực Kỳ Đơn Giản)

```text
Bước 1: Anh gửi từ khóa hoặc link GitHub cho Team 13 ("check & tư vấn giúp anh")
        ↓
Bước 2: `skill-repo-scout` quét thật (HTTP 200, stars, license) + so trùng kho máy
        → Trả Bảng Tư Vấn 3 Ngăn (KHÔNG tự ý nạp khi anh chưa gật đầu!)
        ↓
Bước 3: Anh chốt 1 câu: "OK nạp repo X vào Ngăn ..."
        ↓
Bước 4: Hệ thống tự động chạy khép kín:
        [Tải vùng cách ly] → [Cổng 1: Quét bảo mật & Prompt Injection]
        → [Chuẩn hóa & Nạp đúng ngăn + Dựng FTS5]
        → [Cổng 2: Test 3 câu search thật + In Scorecard A–F]
```

---

## 3. Cách Đọc "Bảng Tư Vấn 3 Ngăn" Để Chọn Nơi Nạp Chuẩn Nhất

Mỗi lần `skill-repo-scout` kiểm tra xong sẽ tư vấn anh 1 trong 4 quyết định:

| Quyết định tư vấn | Vị trí lưu trong Antigravity | Khi nào nên chọn |
| :--- | :--- | :--- |
| **🟢 Ngăn 1 — Gộp `references/`** | `%USERPROFILE%\.gemini\config\skills\<skill-co-san>\references\` | Repo mới bổ sung tài liệu/mẫu cho mảng anh **đã có Skill** (vd: thêm mẫu SQL SAP, thêm mẹo SEO, thêm prompt video) → **tốn 0 ký tự ngân sách Global**. |
| **🟢 Ngăn 2 — Gắn vào Plugin Team** | `%USERPROFILE%\.gemini\config\plugins\team-<ten>\skills\<slug>\` | Skill chuyên sâu chỉ phục vụ **1 Phòng Ban cụ thể** (Team 0–12) → bật/tắt gọn theo Team đó. |
| **🟢 Ngăn 3 — Tạo Global Skill mới** | `%USERPROFILE%\.gemini\config\skills\<slug-moi>\` | Năng lực **mới hoàn toàn** dùng chung cho nhiều Team/dự án (vd: n8n automation, Docker K8s, Excel VBA...). |
| **🔴 Bỏ qua (Không nạp)** | *(Không nạp vào máy)* | Trùng >70% với skill đang có, repo bỏ hoang nhiều năm, hoặc có cảnh báo bảo mật. |

---

## 4. 6 Câu Lệnh Mẫu Copy-Paste Dùng Ngay Trong Khung Chat

### Mẫu 1 — Nhờ Team 13 đi săn repo Skill hay theo nhu cầu
> *"Gọi **Team 13 (`skill-repo-scout`)** tìm giúp anh 3–5 repo Skill GitHub uy tín nhất về **[Docker / Next.js / n8n / Excel Automation...]**, kiểm tra stars + ngày cập nhật + đối chiếu trùng lặp với kho máy anh rồi lập Bảng Tư Vấn nên nạp cái nào."*

### Mẫu 2 — Gửi 1 link GitHub cụ thể nhờ check & tư vấn trước khi nạp
> *"Gọi **Team 13** kiểm tra repo `https://github.com/<owner>/<repo>` xem bên trong có những skill nào, có trùng với kho đang có không và tư vấn anh nên nạp vào ngăn nào (chưa nạp vội)."*

### Mẫu 3 — Chốt duyệt nạp (chạy trọn gói Quét Bảo Mật → Chuẩn Hóa → Nạp → Test FTS5)
> *"OK duyệt nạp repo `https://github.com/<owner>/<repo>` vào **Ngăn 2 (gắn vào Team 2)** / **Ngăn 3 (Global Skill mới `<slug>`)** — cho **Team 13** quét bảo mật Cổng 1, chuẩn hóa nạp vào Antigravity và chạy QA Cổng 2 test 3 câu search."*

### Mẫu 4 — Chạy bằng Workflow tự động 4 pha (`skill_curator_pipeline.py`)
> *"Chạy `skill_curator_pipeline` mode `scout_and_advise` cho yêu cầu: `tìm skill tối ưu PostgreSQL`"*
*(Sau khi duyệt xong):*
> *"Chạy `skill_curator_pipeline` mode `ingest_approved` cho URL `https://github.com/...` với `target_slot: plugin:team-server-vps-hosting`"*

### Mẫu 5 — Nạp file tài liệu nội bộ (PDF, Word, Sách, SQL) trên máy thành Skill
> *"Gọi `skill-ingestor-builder` nạp file `D:\TaiLieu\...` theo quy chuẩn 5 bước `nap-tai-lieu-antigravity` rồi cho `skill-security-qa` kiểm toán FTS5."*

### Mẫu 6 — Kiểm tra lại các repo ngoài đã nạp & xem có bản cập nhật mới không
> *"Gọi **Team 13 (`skill-repo-scout`)** đọc sổ `upstream_registry.json` kiểm tra xem các repo skill đã nạp có bản cập nhật mới nào trên GitHub không."*

---

## 5. Hướng Dẫn Tự Kiểm Tra Trên Antigravity Sau Khi Nạp Xong

1. **Mở hội thoại mới (`+ New Conversation`):** Antigravity tự nạp cấu hình skill/plugin mới ở lượt chat kế tiếp hoặc hội thoại mới.
2. **Bật/Tắt trong giao diện App:** Vào **Customizations → Plugins / Skills** trên Antigravity App để kiểm tra Skill / Plugin mới đã hiện màu xanh (Enabled).
   - *Mẹo tiết kiệm context:* Khi chưa có nhu cầu săn repo mới, anh có thể **tắt tạm `team-skill-curator`** trong Customizations, khi nào cần tìm/nạp skill thì bật lên lại trong 1 giây.
3. **Kiểm tra thủ công bằng PowerShell (nếu muốn tự soi):**
   ```powershell
   $PY = "python"
   # Xem sức khỏe toàn kho Skill & FTS5
   & $PY -c "import sys; sys.path.insert(0, r'%USERPROFILE%\.gemini\config\scripts'); import agy_skill_engine; print(agy_skill_engine.get_engine().audit_report(force_rebuild=False)['sync'])"
   ```
4. **Cách gỡ bỏ an toàn khi không dùng nữa:**
   - Di chuyển thư mục skill sang `E:\DIEN APP\Antigravity_Config_Backup_20261119\` (không cần xóa vĩnh viễn) → chạy lại lệnh `audit_report(force_rebuild=True)` ở trên để dọn khỏi chỉ mục `agy_skill_index.db`.

---

## 6. Đường Dẫn Quan Trọng Của Team 13
- **Plugin Team 13:** `%USERPROFILE%\.gemini\config\plugins\team-skill-curator\`
- **Workflow 4 Pha:** `%USERPROFILE%\.gemini\config\workflows\skill_curator_pipeline.py`
- **Sổ Theo Dõi Nguồn Repo Đã Nạp:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-skill-curator\upstream_registry.json`
- **Bộ Nhớ Nhóm Team 13:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-skill-curator\MEMORY.md`
