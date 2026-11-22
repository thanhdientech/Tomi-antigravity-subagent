# Luật Vận Hành Team 15 — Build AI Agent JavisOS (Tomi & InfoAsia), Training Chống Bịa & n8n (`team-javisos-n8n`)

Toàn bộ 4 thành viên (`javis-architect-builder`, `javis-anti-hallucination-trainer`, `n8n-workflow-engineer`, `javis-n8n-qa-auditor`) bắt buộc tuân thủ 6 thiết luật khi làm việc với `%JAVIS_BRAIN_DIR%` và máy chủ VPS `<INTERNAL_SERVER_IP>`:

1. **Cách Ly Tuyệt Đối 2 Bản JavisOS & Thương Hiệu (`Zero Cross-Brand / Cross-Brain Leak`):**
   - **Bản 1 — TOMI AI AGENT:** Logo **Tomi**, Name **Tomi**, Port `:7777` (`https://ai.infoasia.vn:19443`), dữ liệu riêng `brains/` & `state_dien` (local `state/`).
   - **Bản 2 — INFOASIA AI AGENT:** Logo **InfoAsia**, Name **InfoAsia**, Port `:7778` (`https://ai.infoasia.vn:9443`), dữ liệu riêng `brains_infoasia/` & `state_infoasia/`.
   - **Bản JavisOS mới:** Khi build instance mới, bắt buộc cấp port riêng, thư mục `state_<slug>`, `brains_<slug>` và bộ `branding/` riêng — tuyệt đối KHÔNG ghi đè logo/tên/dữ liệu chéo giữa Tomi và InfoAsia.
2. **Backup & Deploy An Toàn Trên VPS `<INTERNAL_SERVER_IP>` (`/home/infoasia/javis-os`):**
   - Trước mọi chỉnh sửa production, bắt buộc tạo bản sao lưu có timestamp (`.bak_YYYYMMDD_HHMMSS`).
   - Nâng cấp code lên VPS dùng đúng script an toàn `./update-javis-safe.sh` (bảo toàn logo/tên/giọng/tên miền) và khởi động lại bằng `./restart-both-javis.sh`; dừng xin xác nhận trước lệnh phá hủy (`rm -rf`, `DROP`, đổi firewall/SSL).
3. **Training Chống Bịa Đặt Bắt Buộc (`Zero-Hallucination Training Lock`):**
   - Mọi đợt đào tạo Agent (Javis cũ hay Javis mới) bắt buộc nhồi đủ 5 Chốt Chặn Chống Ảo Giác (`quy-trinh-rang-buoc-chong-ao-giac-ai.md`), Khuôn 4 Tọa Độ Nguồn, nguyên tắc *"thà nhận chưa có thông tin còn hơn bịa 1 con số/tên bảng/URL"*, và xuất kèm **Bộ Câu Hỏi Bẫy Kiểm Chứng** để QA chạy test thực tế.
4. **Chuẩn Bảo Mật & Độ Tin Cậy Workflow n8n (`:5678` Chính & `:5679` v2):**
   - Không bao giờ hardcode mật khẩu, API key, JWT hay token vào JSON workflow n8n (dùng Credentials Store hoặc biến môi trường của n8n).
   - Mọi workflow production phải có Error Handling / Retry-Backoff và kiểm tra không tạo vòng lặp vô tận webhook.
5. **Chuẩn Môi Trường & Trình Duyệt Thật:**
   - Script kiểm định local chạy bằng Python313 (`python`); khi cần kiểm tra giao diện Web JavisOS (`:7777/:7778`) hoặc n8n (`:5678/:5679`) dùng `antigravity-browser-controller` (`RULE #1c`) chụp Silent CDP và mở đọc ảnh bằng `read_file`.
6. **Tách Vai Xây Dựng/Training & Vai QA Kiểm Toán Độc Lập 4 Tầng (`No Self-Grading`):**
   - `javis-n8n-qa-auditor` chỉ đọc & chạy kiểm định (**CẤM** `edit_file`/`write_file`), bắt buộc chốt đủ 4 tầng QA (HTTP 200 & Docker `Up` → Đúng Logo/Name & 0 rò Brain → Chạy bộ Test Chống Bịa Đặt → Ảnh UI mở đọc bằng `read_file` & n8n execution `success`) + chấm Scorecard iFixAi A–F trước khi bàn giao.
