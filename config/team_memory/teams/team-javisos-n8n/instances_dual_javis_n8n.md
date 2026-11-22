# HỒ SƠ HẠ TẦNG DUAL-JAVISOS & N8N (LOCAL + VPS `<INTERNAL_SERVER_IP>`)

## 1. Hai Bản JavisOS Production (Cách Ly Tuyệt Đối Logo, Name, Repo & Brain)
| Hạng mục | Bản 1 — TOMI AI AGENT | Bản 2 — INFOASIA AI AGENT | Bản JavisOS Mới (Template) |
| :--- | :--- | :--- | :--- |
| **Tên hiển thị (`JAVIS_NAME`)** | **Tomi AI Agent** (`Tomi`) | **InfoAsia AI Agent** (`InfoAsia`) | `<Brand_Name_Mới>` |
| **GitHub Repo Độc Lập** | `https://github.com/thanhdientech/Tomi_ai_agent.git` | `https://github.com/thanhdientech/Infoasia-ai-javisos.git` | Repo Git riêng |
| **Commit mốc đã chốt** | `4600732` (`refactor: remove Tomi Office 3D files per user request`) | `81d7f56` (`feat: initial commit for InfoAsia AI Agent JavisOS (ERP, SAP B1 and Beas, zero 3D office)` — `27,496 files`) | Commit khởi tạo |
| **Logo / Branding** | **100% thương hiệu Tomi** | **100% thương hiệu InfoAsia** (`logo.png`, `icon-192.png`, `icon-512.png`, `favicon.png`) | `branding_<slug>/` riêng |
| **Port LAN (`42.29`)** | `7777` (`http://<INTERNAL_SERVER_IP>:7777`) | `7778` (`http://<INTERNAL_SERVER_IP>:7778`) | Port trống mới (vd `7779+`) |
| **Domain SSL (WAN)** | `https://ai.infoasia.vn:19443` | `https://ai.infoasia.vn:9443` | Nginx SSL port mới |
| **Thư mục Brain** | `brains/` (Tuyệt đối KHÔNG chứa tài liệu ERP/CSDL InfoAsia) | `brains/` trong repo (`brains_infoasia/` trên VPS): toàn bộ tri thức SAP B1, Boyum Beas, SQL Server & `Infoasia_AI_agent/` | `brains_<slug>/` |
| **Thư mục State** | `state_dien/` (local `state/`) | `state_infoasia/` | `state_<slug>/` |
| **Chính sách Phòng 3D** | **Zero 3D Office:** Đã xóa `tomi-office-2d.js` & toàn bộ file demo 3D khỏi kho | **Zero 3D Office:** Đã loại sạch `tomi-company-3d*`, `densankhau*`, `tomi-office-2d.js` | Theo yêu cầu dự án |

### Chi tiết 2 Kho GitHub Chính Thức (Ghi nhận `2026-11-22`)
1. **Kho 1 — InfoAsia AI Agent JavisOS**
   - **GitHub URL:** `https://github.com/thanhdientech/Infoasia-ai-javisos.git`
   - **Commit mới nhất:** `81d7f56` (`feat: initial commit for InfoAsia AI Agent JavisOS (ERP, SAP B1 and Beas, zero 3D office)`)
   - **Số lượng file đã push:** `27,496 files`
   - **Cấu hình chuẩn:** Port `7778` (`JAVIS_NAME=InfoAsia AI Agent`); nhận diện 100% InfoAsia (`logo.png`, `icon-192.png`, `icon-512.png`, `favicon.png`); thư mục `brains/` chứa toàn bộ tri thức SAP B1, Boyum Beas, SQL Server và tài liệu nội bộ `Infoasia_AI_agent/`; đã loại sạch toàn bộ file `tomi-company-3d*`, `densankhau*`, `tomi-office-2d.js`.
2. **Kho 2 — Tomi AI Agent**
   - **GitHub URL:** `https://github.com/thanhdientech/Tomi_ai_agent.git`
   - **Commit mới nhất:** `4600732` (`refactor: remove Tomi Office 3D files per user request`)
   - **Cấu hình chuẩn:** Port `7777` (`JAVIS_NAME=Tomi AI Agent`); nhận diện 100% Tomi; đã xóa bỏ `tomi-office-2d.js` và các file demo 3D khỏi kho; cách ly tuyệt đối — không chứa tài liệu ERP / cơ sở dữ liệu của InfoAsia.

## 2. Hai Cụm n8n Automation Trên VPS `<INTERNAL_SERVER_IP>`
| Cụm n8n | Port LAN | Domain SSL | Container & Thư mục | Vai trò |
| :--- | :---: | :--- | :--- | :--- |
| **n8n Chính (`v2.42.0`)** | `5678` | `https://n8n.infoasia.com.vn:6443` | `n8n-n8n-1` (`/home/n8n`) + PostgreSQL 18 `:5432` | Production chính |
| **n8n Bản v2** | `5679` | `https://n8n.infoasia.com.vn:7443` | `n8n-v2` (`/home/n8n_v2`) | Staging / Test / Workflow mới |

## 3. Đầu Nối Hệ Sinh Thái Trên Cùng Server `<INTERNAL_SERVER_IP>`
- **9Router AI API:** `:20128` | **SAP API Server:** `:50001` | **ERPNext v16:** `:8787` | **Omni IT Manager:** `:8090`
- **Lệnh quản trị JavisOS trên VPS (`ssh infoasia@<INTERNAL_SERVER_IP>`):**
  - `cd /home/infoasia/javis-os && ./update-javis-safe.sh`
  - `cd /home/infoasia/javis-os && ./restart-both-javis.sh`
