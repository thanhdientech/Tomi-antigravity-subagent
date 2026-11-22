# TEAM MEMORY — `team-javisos-n8n` (Team 15: JavisOS Tomi & InfoAsia + n8n VPS 42.29)

- **Trưởng nhóm (`LEADER`):** `javis-architect-builder`
- **Thành viên (`MEMBER`):** `javis-anti-hallucination-trainer`, `n8n-workflow-engineer`
- **Kiểm toán độc lập 4 tầng (`INDEPENDENT_AUDITOR`):** `javis-n8n-qa-auditor`
- **Mã nguồn Local:** `%JAVIS_BRAIN_DIR%`
- **Hồ sơ 2 bản JavisOS & 2 cụm n8n:** `instances_dual_javis_n8n.md`

## Bài học tích lũy (Learned Patterns)
- `[2026-11-22]` **Cách ly tuyệt đối 2 bản trên VPS 42.29:** Bản **Tomi** (`:7777` / `https://ai.infoasia.vn:19443`, Logo & Name **Tomi**, dữ liệu `state_dien` + `brains/`) tách biệt hoàn toàn với bản **InfoAsia** (`:7778` / `https://ai.infoasia.vn:9443`, Logo & Name **InfoAsia**, dữ liệu `state_infoasia` + `brains_infoasia/`).
- `[2026-11-22]` **Deploy an toàn giữ thương hiệu:** Trên VPS `<INTERNAL_SERVER_IP>`, luôn dùng `cd /home/infoasia/javis-os && ./update-javis-safe.sh` và `./restart-both-javis.sh` để không mất tùy chỉnh logo, giọng nói & tên miền.
- `[2026-11-22]` **QA Chống Bịa Đặt bắt buộc:** Sau mỗi lần đào tạo Agent JavisOS phải chạy tối thiểu 5 câu test (3 câu thật + 2 câu bẫy không có trong tài liệu / hỏi chéo Brain) — bịa dù 1 thông số → `FAIL` ngay!
