---
name: javisos-n8n-sop
description: "SOP Team 15 (JavisOS Tomi/InfoAsia & n8n trên VPS 42.29): Quy trình Build, Training chống bịa đặt, Workflow n8n và QA 4 tầng."
---

# SOP TEAM 15 — BUILD AI AGENT JAVISOS (TOMI & INFOASIA) & WORKFLOW N8N (`team-javisos-n8n`)

## 1. Luồng Phối Hợp 4 Bước Khép Kín
```text
[1. javis-architect-builder (LEADER)]       -> Khảo sát code/hạ tầng, khóa đúng instance (Tomi :7777 | InfoAsia :7778 | Javis mới)
             │
             ├──► [2a. javis-anti-hallucination-trainer] -> Nạp/chuẩn hóa wiki & sources, nhồi luật chống bịa, lập Bộ Câu Hỏi Bẫy
             │
             ├──► [2b. n8n-workflow-engineer]            -> Thiết kế/sửa Workflow n8n (:5678 / :5679), Error Handler, nối API Javis/SAP/ERP
             │
             ▼
[3. javis-architect-builder]                -> Backup + Deploy an toàn lên VPS <INTERNAL_SERVER_IP> (update-javis-safe.sh / restart-both-javis.sh)
             │
             ▼
[4. javis-n8n-qa-auditor (ĐỘC LẬP)]         -> QA 4 Tầng: HTTP 200/Docker -> Đúng Logo/Name/Brain -> Test Chống Bịa -> Soi Ảnh UI + n8n Run
                                            -> FAIL: Trả lỗi sửa 1 vòng | PASS: Ký Scorecard iFixAi A/B + ghi MEMORY.md
```

## 2. Bản Đồ 2 Bản JavisOS & 2 Cụm n8n Trên VPS `<INTERNAL_SERVER_IP>`
| Thành phần | Cổng LAN | Domain SSL | Thư mục / Dữ liệu riêng (CẤM TRỘN) | Thương hiệu khóa cứng |
| :--- | :---: | :--- | :--- | :--- |
| **JavisOS — TOMI** | `:7777` | `https://ai.infoasia.vn:19443` | `/home/infoasia/javis-os` (`state_dien` / `brains`) | **Logo Tomi + Name Tomi** |
| **JavisOS — INFOASIA** | `:7778` | `https://ai.infoasia.vn:9443` | `/home/infoasia/javis-os` (`state_infoasia` / `brains_infoasia`) | **Logo InfoAsia + Name InfoAsia** |
| **n8n Chính (`v2.42.0`)** | `:5678` | `https://n8n.infoasia.com.vn:6443` | Docker `n8n-n8n-1` (`/home/n8n`) + PostgreSQL 18 `:5432` | n8n Production |
| **n8n Bản v2** | `:5679` | `https://n8n.infoasia.com.vn:7443` | Docker `n8n-v2` (`/home/n8n_v2`) | n8n v2 / Staging |

## 3. Đường Dẫn Mã Nguồn & Lệnh Quản Trị Gốc
- **Workspace Local:** `%JAVIS_BRAIN_DIR%` (`server/`, `dashboard/`, `server/branding/`, `deploy/vps-dual-javis/`, `Infoasia_AI_agent/`, `brains/`, `brains_infoasia/`)
- **Deploy / Restart trên VPS `<INTERNAL_SERVER_IP>` (`ssh infoasia@<INTERNAL_SERVER_IP>`):**
  - Cập nhật giữ nguyên thương hiệu & tùy chỉnh: `cd /home/infoasia/javis-os && ./update-javis-safe.sh`
  - Khởi động lại cả 2 bản `:7777` & `:7778`: `cd /home/infoasia/javis-os && ./restart-both-javis.sh`
- **Bộ nhớ dài hạn Team 15:** `%USERPROFILE%\.gemini\config\team_memory\teams\team-javisos-n8n\MEMORY.md` & `instances_dual_javis_n8n.md`
