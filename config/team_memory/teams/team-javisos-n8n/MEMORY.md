# TEAM MEMORY — `team-javisos-n8n` (Team 15: JavisOS Tomi & InfoAsia + n8n VPS 42.29)

- **Trưởng nhóm (`LEADER`):** `javis-architect-builder`
- **Thành viên (`MEMBER`):** `javis-anti-hallucination-trainer`, `n8n-workflow-engineer`
- **Kiểm toán độc lập 4 tầng (`INDEPENDENT_AUDITOR`):** `javis-n8n-qa-auditor`
- **Mã nguồn Local:** `%JAVIS_BRAIN_DIR%`
- **Hồ sơ 2 bản JavisOS & 2 cụm n8n:** `instances_dual_javis_n8n.md`

## 2 Kho GitHub Chính Thức (Tách Biệt 100% & Zero 3D Office)
1. **Kho 1 — InfoAsia AI Agent JavisOS (`:7778` | `JAVIS_NAME=InfoAsia AI Agent`):**
   - **GitHub URL:** `https://github.com/thanhdientech/Infoasia-ai-javisos.git`
   - **Commit mốc:** `81d7f56` (`feat: initial commit for InfoAsia AI Agent JavisOS (ERP, SAP B1 and Beas, zero 3D office)` — `27,496 files`)
   - **Đặc điểm:** 100% thương hiệu InfoAsia (`logo.png`, `icon-192.png`, `icon-512.png`, `favicon.png`); `brains/` chứa trọn bộ tri thức SAP B1, Boyum Beas, SQL Server & `Infoasia_AI_agent/`; đã loại sạch `tomi-company-3d*`, `densankhau*`, `tomi-office-2d.js`.
2. **Kho 2 — Tomi AI Agent (`:7777` | `JAVIS_NAME=Tomi AI Agent`):**
   - **GitHub URL:** `https://github.com/thanhdientech/Tomi_ai_agent.git`
   - **Commit mốc:** `4600732` (`refactor: remove Tomi Office 3D files per user request`)
   - **Đặc điểm:** 100% thương hiệu Tomi; đã xóa bỏ `tomi-office-2d.js` & toàn bộ file demo 3D; cách ly tuyệt đối — không chứa tài liệu ERP / CSDL của InfoAsia.

## Bài học tích lũy (Learned Patterns)
- `[2026-11-22]` **Cách ly tuyệt đối 2 bản trên VPS 42.29:** Bản **Tomi** (`:7777` / `https://ai.infoasia.vn:19443`, Logo & Name **Tomi**, dữ liệu `state_dien` + `brains/`) tách biệt hoàn toàn với bản **InfoAsia** (`:7778` / `https://ai.infoasia.vn:9443`, Logo & Name **InfoAsia**, dữ liệu `state_infoasia` + `brains_infoasia/`).
- `[2026-11-22]` **Khóa chuẩn 2 Repo GitHub & Zero 3D Office:** Luôn đẩy code đúng kho (`Infoasia-ai-javisos.git` cho InfoAsia `:7778` vs `Tomi_ai_agent.git` cho Tomi `:7777`); tuyệt đối không đưa lại các file phòng 3D (`tomi-company-3d*`, `densankhau*`, `tomi-office-2d.js`) và không rò rỉ tài liệu ERP InfoAsia sang kho Tomi.
- `[2026-11-22]` **Deploy an toàn giữ thương hiệu:** Trên VPS `<INTERNAL_SERVER_IP>`, luôn dùng `cd /home/infoasia/javis-os && ./update-javis-safe.sh` và `./restart-both-javis.sh` để không mất tùy chỉnh logo, giọng nói & tên miền.
- `[2026-11-22]` **QA Chống Bịa Đặt bắt buộc:** Sau mỗi lần đào tạo Agent JavisOS phải chạy tối thiểu 5 câu test (3 câu thật + 2 câu bẫy không có trong tài liệu / hỏi chéo Brain) — bịa dù 1 thông số → `FAIL` ngay!
- `[2026-11-22]` VPS <INTERNAL_SERVER_IP> dung dai port tach biet 100% khoi 42.29: Javis InfoAsia Native systemd javis@infoasia :7800 (dai 78xx cho da-instance DB), n8n v2.48.7 Docker :5680 + PG17 pgvector loopback 127.0.0.1:5433; ket noi live <INTERNAL_SERVER_IP> (SAP B1 10.0 FAL_OCT_2025, has_beas=False, SL=CLOSED) qua FreeTDS + RBAC 5 nhom 3 lop.
- `[2026-11-23]` Cap thanh cong SSL Let's Encrypt cho n8n.infoasia.vn qua acme.sh DNS TXT challenge; n8n chay song song n8n.infoasia.vn:6443 va n8n.infoasia.vn:7443; cronjob acme.sh tu dong kiem tra va gia han 4 lan/ngay.
- `[2026-11-23]` JavisOS 0.628.5 gom khoi code >=24 dong/>=800 ky tu thanh .jv-art[data-art] va gom nhieu GET vao POST /batch -> chart-inline.js phai doc ca window.JavisArtifacts.get(id), con cach ly hoi thoai da-user phai khoa dong thoi DB rbac_session_owners, SessionStore SQL, _auth_guard (gom POST /batch & WS) va xoa localStorage khi doi user.
