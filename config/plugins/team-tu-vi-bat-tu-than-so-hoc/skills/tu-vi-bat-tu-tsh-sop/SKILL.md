---
name: tu-vi-bat-tu-tsh-sop
description: "SOP Team 16 (Chiêm Tinh — Tử Vi, Bát Tự 24 Tiết Khí & Thần Số Học): Quy trình 4 bước SOP V3.0 xuất 10 hồ sơ, Tinh bàn HTML & QA 13 bước."
---

# SOP TEAM 16 — CHIÊM TINH: TỬ VI • BÁT TỰ • THẦN SỐ HỌC (`team-tu-vi-bat-tu-than-so-hoc`)

## 1. Luồng Phối Hợp 4 Subagent Khép Kín (SOP V3.0)
```text
[1. destiny-chart-engineer (LEADER)]      -> Kiểm đủ 4 dữ kiện (Hard Stop) -> Chạy destiny_pipeline.py -> Xuất facts_*.json + 01_Ho_So_Goc + Tinh bàn HTML
             │
             ▼
[2. destiny-tuvi-battu-master (MEMBER)]   -> Khóa Dụng/Hỷ/Kỵ Thần -> Viết 02_Menh_Thu + 03_Tu_Vi_14_Cung (tách 3 tầng sao) + 04_Bat_Tu + 05_Van_Han
             │
             ▼
[3. destiny-numerology-advisor (MEMBER)]  -> Luận giải 07_Than_So_Hoc (Pythagoras + Phillips 3x3) + 00_Huong_Dan + 00_Tong_Hop + Chuyên đề 7 Đại họa / Hôn phối
             │
             ▼
[4. destiny-qa-auditor (READ-ONLY QA)]    -> Chạy qa_dossier_auditor.py (13 bước) đối chiếu facts_*.json -> Kiểm tra Tinh bàn HTML -> Scorecard iFixAi A-F
```

## 2. Đường Dẫn Động Cơ & Tài Liệu Chuẩn (Dùng Chung Global Skill `tu-vi-bat-tu-than-so-hoc`)
- **Động cơ tất định:** `%USERPROFILE%\.gemini\config\skills\tu-vi-bat-tu-than-so-hoc\scripts\destiny_pipeline.py`
- **Kiểm toán 13 bước:** `%USERPROFILE%\.gemini\config\skills\tu-vi-bat-tu-than-so-hoc\scripts\qa_dossier_auditor.py`
- **JSON mẫu ẩn danh:** `%USERPROFILE%\.gemini\config\skills\tu-vi-bat-tu-than-so-hoc\examples\sample_profiles.json`
- **4 Tài liệu học thuật & SOP V3.0 (`references/`):**
  1. `01-sop-v3-kien-truc-10-file-va-quy-tac-bat-bien.md` (kiến trúc 10 tệp `00..09`, phân tầng Người lớn vs Trẻ nhỏ)
  2. `02-chuyen-de-7-dai-hoa-sinh-mang-va-hon-phoi-can-tu.md` (7 đại họa, bộ sao cứu giải, Hôn phối, Kim Lâu/Hoang Ốc/Tam Tai, Căn tu)
  3. `03-thuat-toan-than-so-hoc-song-he-va-api.md` (18 chỉ số Pythagoras + Phillips 3x3 & 8 Mũi tên)
  4. `04-co-thu-tu-vi-bat-tu-va-quy-chuan-trich-dan.md` (Dụng Thần Điều Hậu/Phù Ức/Thông Quan & nguồn Cổ thư 3 tầng)

## 3. Lệnh Chạy Nhanh (Python313 — `Exit code 0`)
```powershell
$PY = "python"
$SK = "%USERPROFILE%\.gemini\config\skills\tu-vi-bat-tu-than-so-hoc\scripts"

# 1 cá nhân:
& $PY "$SK\destiny_pipeline.py" --name "Nguyễn Văn An" --dob 1990-08-15 --time 10:30 --gender Nam --birthplace "TP. Hồ Chí Minh" --output-dir "<thu_muc_xuat>" --target-year 2026

# Nhiều thành viên (gia đình / đối tác):
& $PY "$SK\destiny_pipeline.py" --input "<profiles.json>" --output-dir "<thu_muc_xuat>" --target-year 2026 --group-by-member

# Kiểm toán độc lập 13 bước:
& $PY "$SK\qa_dossier_auditor.py" --dossier-dir "<thu_muc_xuat>" --facts-dir "<thu_muc_chua_facts>"
```

## 4. Bộ Nhớ Dài Hạn & Bảo Mật Dữ Liệu Riêng Tư
- **Bộ nhớ Team dùng chung:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-tu-vi-bat-tu-than-so-hoc\MEMORY.md`
- **Lưu ý riêng tư:** Chỉ lưu tên/ngày sinh/lá số thật của người dùng trong thư mục xuất riêng của dự án cục bộ, tuyệt đối không ghi vào `plugins/` hay đẩy lên Git Public.
