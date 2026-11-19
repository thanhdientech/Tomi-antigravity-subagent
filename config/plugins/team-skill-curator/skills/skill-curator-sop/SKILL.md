---
name: skill-curator-sop
description: "SOP Team 13 (Săn, Check, Tư Vấn & Nạp Repo Skill): Quy trình 4 bước chống mã độc/trùng lặp, chuẩn hóa 3 ngăn Javis FTS5."
---

# SOP TEAM 13 — SĂN, TƯ VẤN & NẠP REPO SKILL VÀO ANTIGRAVITY (`team-skill-curator`)

## 1. Luồng Phối Hợp 4 Bước (Có Cổng Tư Vấn & Khiên Bảo Mật)
```text
[1. skill-repo-scout (LEADER)]    -> Tìm repo GitHub/Marketplace + Check HTTP 200/Stars/License + So trùng với kho máy
                                  -> Lập Bảng Tư Vấn 3 Ngăn (Global / Plugin Team / References / Bỏ qua) -> CHỜ NGƯỜI DÙNG DUYỆT
             │
             ▼ (Người dùng chốt nạp repo X vào ngăn Y)
[2. skill-security-qa (Cổng 1)]   -> Quét trong vùng cách ly scratch/skill_quarantine/: mã độc, shell nguy hiểm, prompt injection
                                  -> PASS mới cho phép nạp! (FAIL -> CHẶN & cảnh báo ngay)
             │
             ▼
[3. skill-ingestor-builder]       -> Chuẩn hóa UTF-8 (0 BOM), description <= 145 ký tự, chuyển tool sang chuẩn Antigravity
                                  -> Nạp đúng ngăn -> Chạy agy_skill_engine.py cập nhật FTS5 -> Ghi upstream_registry.json
             │
             ▼
[4. skill-security-qa (Cổng 2)]   -> Audit 0 warning, 0 trùng lặp, test 3 câu search (Việt có dấu / không dấu / Anh) -> Scorecard A-F
```

## 2. Nguyên Tắc Chọn Đúng 3 Ngăn Lưu Trữ
| Ngăn | Đường dẫn đích | Khi nào chọn |
| :--- | :--- | :--- |
| **Ngăn 1 — Gộp `references/`** | `%USERPROFILE%\.gemini\config\skills\<skill-co-san>\references\` | Tài liệu / mẫu mới cùng chuyên ngành với Skill đã có → **0 tốn thêm ngân sách description Global**. |
| **Ngăn 2 — Gắn vào Plugin Team** | `%USERPROFILE%\.gemini\config\plugins\team-<ten>\skills\<slug>\` | Skill chuyên sâu phục vụ riêng 1 Phòng Ban (Team 0–12) → bật/tắt gọn theo Team, không làm nặng Global. |
| **Ngăn 3 — Global Skill mới** | `%USERPROFILE%\.gemini\config\skills\<slug>\` | Mảng năng lực hoàn toàn mới dùng chung nhiều dự án/team (đảm bảo `description <= 145` ký tự). |

## 3. Lệnh Kiểm Tra & Đồng Bộ Chỉ Mục Chuẩn (Python313)
```powershell
$PY = "python"
# Đồng bộ & kiểm toán sức khỏe toàn kho Skill
& $PY -c "import sys; sys.path.insert(0, r'%USERPROFILE%\.gemini\config\scripts'); import agy_skill_engine; print(agy_skill_engine.get_engine().audit_report(force_rebuild=False))"
# Tìm kiếm kiểm chứng truy xuất (thay <tu_khoa>)
& $PY -c "import sys; sys.path.insert(0, r'%USERPROFILE%\.gemini\config\scripts'); import agy_skill_engine; print(agy_skill_engine.get_engine().search('<tu_khoa>', top_k=5))"
```

## 4. Tài Liệu & Bộ Nhớ Liên Kết
- Sổ tay hướng dẫn cho người dùng: `%USERPROFILE%\.gemini\config\docs\HUONG_DAN_TIM_VA_NAP_REPO_SKILL_ANTIGRAVITY.md`
- Quy chuẩn nạp tài liệu 5 bước: `%USERPROFILE%\.gemini\config\skills\nap-tai-lieu-antigravity\SKILL.md`
- Sổ theo dõi nguồn repo đã nạp: `%USERPROFILE%\.gemini\config\team_memory\teams\team-skill-curator\upstream_registry.json`
- Bộ nhớ nhóm: `%USERPROFILE%\.gemini\config\team_memory\teams\team-skill-curator\MEMORY.md`
