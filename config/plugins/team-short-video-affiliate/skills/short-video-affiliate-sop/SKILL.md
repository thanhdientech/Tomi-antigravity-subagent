---
name: short-video-affiliate-sop
description: "SOP Team 14 (Video Ngắn 9:16 Facebook Reels & Shopee Affiliate): Vận hành Shopee KOL Studio (:8600) và 13 Kênh Mẫu chống nhảy bước."
---

# SOP TEAM 14 — NHÀ MÁY VIDEO NGẮN 9:16 & SHOPEE AFFILIATE (`team-short-video-affiliate`)

## 1. Luồng Phối Hợp 4 Bước Khép Kín (Áp Dụng Cho 13+ Kênh Mẫu & Mọi Ngành Shopee)
```text
[1. short-channel-product-scout (LEADER)] -> Đối chiếu 13 Kênh Mẫu (01..13) + Quét SP Shopee thật (:8600) + Chốt Voice ID
             │
             ▼
[2. short-script-storyboarder]            -> Kịch bản 6 phong cách KOL + Phân cảnh Step_{k-1}->Step_k + Text Safe-Zone 9:16
             │
             ▼
[3a. short-video-qa-auditor (Cổng 1)]     -> Soi ảnh Step_01..08 bằng read_file (bắt nhảy bước, Tool-Tip, chữ Hán, mất người)
             │
             ▼
[3b. short-kol-studio-producer]           -> Render .venv Shopee Studio (:8600/:8100/:8010/Three.js) + Cắt 0.0s->3.4s + Xuất kép
             │
             ▼
[4. short-video-qa-auditor (Cổng 2)]      -> ffprobe (1080x1920, 30fps) + soi ảnh qa_end_step_*.jpg bằng read_file -> Scorecard A-F
```

## 2. Đường Dẫn Công Cụ & Kho 13 Kênh Mẫu Gốc (Đã Xác Minh Tại Ổ E)
- **Shopee KOL Studio (`:8600`):** `E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Shopee_KOL_Studio_Tool`
  - Python `.venv`: `Shopee_KOL_Studio_Tool\.venv\Scripts\python.exe`
  - Khởi động 5 dịch vụ (`:8600/:8650/:8100/:8010/:8766`): `START_SHOPEE_STUDIO.bat` (`STOP_ALL_SERVICES.bat` / `RESTART_ALL_SERVICES.bat`)
  - CLI nhanh: `%USERPROFILE%\.gemini\config\skills\shopee-affiliate-video-studio\scripts\shopee_story_cli.py`
- **Kho 13 Dạng Kênh Mẫu (`01`..`13`):** `E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Nghien_Cuu_Kenh_Moi_Huong_Dan`
  - Master SOP: `00_MASTER_SOP_TOAN_BO_CAC_KENH_CHO_AGENT.md`
  - Bảng giọng đọc: `BANG_TRA_CUU_GIONG_DOC_AI33_VI_EN.md`
  - Quy chuẩn chống nhảy bước & biến hình: `QUY_CHUAN_TAM_DONG_NHAT_VA_LOGIC_VIDEO.md`

## 3. Danh Mục Nhanh 13 Kênh Mẫu Đã Nghiên Cứu (`01`..`13`)
1. `01` Ô tô KOC Cabin (Xe điện vs Xe xăng) · 2. `02` Thời trang Hotgirl Dance · 3. `03` Thời trang KOL Color Palette · 4. `04` Mẹo vặt khoa học 60s (Host Anh Tuấn) · 5. `05` Decor chữa lành · 6. `06` Thể thao Calisthenics · 7. `07` Ô tô KOC lắp phụ kiện 7 góc · 8. `08` Mẹo lái xe Dual-View PiP · 9. `09` DIY Nghệ thuật 8 bước · 10. `10` Tiếng Anh 3D Flashcard + Suno (Kyna) · 11. `11` Cờ vua 3D Forgiro (`Three.js`) · 12. `12` Món ngon & Mẹo bếp Top-Down · 13. `13` Cờ tướng 3D Cờ Thế Giang Hồ (`Three.js`).

## 4. Bộ Nhớ Dài Hạn Team 14
- Bộ nhớ nhóm: `%USERPROFILE%\.gemini\config\team_memory\teams\team-short-video-affiliate\MEMORY.md`
- Hồ sơ 13 kênh mẫu: `%USERPROFILE%\.gemini\config\team_memory\teams\team-short-video-affiliate\archetypes_13_channels.md`
