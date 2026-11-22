# HỒ SƠ HẠ TẦNG DUAL-JAVISOS & N8N (LOCAL + VPS `<INTERNAL_SERVER_IP>`)

## 1. Hai Bản JavisOS Production (Cách Ly Tuyệt Đối Logo, Name & Brain)
| Hạng mục | Bản 1 — TOMI AI AGENT | Bản 2 — INFOASIA AI AGENT | Bản JavisOS Mới (Template) |
| :--- | :--- | :--- | :--- |
| **Tên hiển thị (Name)** | **Tomi** | **InfoAsia** | `<Brand_Name_Mới>` |
| **Logo / Branding** | **Logo Tomi** (`branding/`) | **Logo InfoAsia** (`branding/`) | `branding_<slug>/` riêng |
| **Port LAN (`42.29`)** | `7777` (`http://<INTERNAL_SERVER_IP>:7777`) | `7778` (`http://<INTERNAL_SERVER_IP>:7778`) | Port trống mới (vd `7779+`) |
| **Domain SSL (WAN)** | `https://ai.infoasia.vn:19443` | `https://ai.infoasia.vn:9443` | Nginx SSL port mới |
| **Thư mục Brain** | `brains/` (`Brain Default`) | `brains_infoasia/` (`Brain Default`) | `brains_<slug>/` |
| **Thư mục State** | `state_dien/` (local `state/`) | `state_infoasia/` | `state_<slug>/` |
| **Gói đào tạo riêng** | Kho chung Tomi | `Infoasia_AI_agent/` (8 nhóm) | Thư mục nguồn riêng |

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
