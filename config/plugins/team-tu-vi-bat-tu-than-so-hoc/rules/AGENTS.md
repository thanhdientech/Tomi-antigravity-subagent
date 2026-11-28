# Luật Vận Hành Team 16 — Chiêm Tinh: Tử Vi Đẩu Số, Bát Tự 24 Tiết Khí & Thần Số Học (`team-tu-vi-bat-tu-than-so-hoc`)

Toàn bộ 4 thành viên (`destiny-chart-engineer`, `destiny-tuvi-battu-master`, `destiny-numerology-advisor`, `destiny-qa-auditor`) bắt buộc tuân thủ 5 thiết luật sau:

1. **Cấm Tuyệt Đối LLM Tự Nhẩm Lịch / An Sao / Cộng Số (`Deterministic Engine Lock`):**
   - Cấm tự đổi Dương lịch ↔ Âm lịch, cấm tự nhẩm Can Chi, Cục số, vị trí sao hay cộng tổng Thần Số Học bằng trí nhớ LLM.
   - Mọi ca luận giải bắt buộc chạy trước động cơ Python tất định `skills\tu-vi-bat-tu-than-so-hoc\scripts\destiny_pipeline.py` (`iztro-py` `vi-VN` + `lunar_python` 24 Tiết Khí + Pythagoras/Phillips) bằng Python313 (`python`) để xuất `facts_*.json`, `01_Ho_So_Goc_*_TOOL.md` và Tinh bàn HTML làm **Nguồn Sự Thật Duy Nhất**.
2. **Hard Stop Khi Thiếu 4 Dữ Kiện Cứng (`Chốt 1B`):**
   - Phải có đủ **Họ tên khai sinh có dấu**, **Giới tính**, **Ngày-Tháng-Năm sinh Dương lịch**, và **Giờ-Phút sinh**.
   - Nếu thiếu giờ sinh: CHỈ được chạy Thần Số Học và 3 trụ Năm–Tháng–Ngày của Bát Tự; tuyệt đối không tự bịa giờ sinh để lập lá số Tử Vi.
3. **Chuẩn Học Thuật Bắt Buộc (`3-Layer Star Separation` & `24 Solar Terms`):**
   - Tử Vi Đẩu Số bắt buộc tách rạch ròi 3 tầng sao: **Sao Tọa Thủ** ≠ **Sao Xung Chiếu / Tam Hợp Hội Chiếu** ≠ **Sao Giáp Cung** (cấm gộp chung trong ngoặc đơn).
   - Bát Tự Tử Bình bắt buộc cắt **Trụ Tháng theo đúng giờ giao 24 Tiết Khí** từ `lunar_python`, không cắt theo mùng 1 Âm lịch; cấm kết luận cực đoan `0%` hay `100%` tuyệt đối.
4. **Tách Vai Luận Giải & Vai Kiểm Toán Độc Lập 13 Bước (`No Self-Grading`):**
   - `destiny-qa-auditor` chỉ đọc & chạy kiểm định (`CẤM` `edit_file`/`write_file`), bắt buộc chạy `qa_dossier_auditor.py` đối chiếu mọi file `.md` với `facts_*.json` đạt `Exit code 0`, kiểm tra Tinh bàn HTML và xuất Scorecard iFixAi A–F trước khi bàn giao.
5. **Bảo Mật Tuyệt Đối Thông Tin Cá Nhân (`Zero PII Leak`):**
   - Hồ sơ cá nhân, họ tên thật, ngày giờ sinh, ảnh lá số hay PDF riêng tư của người dùng chỉ lưu ở thư mục dự án cục bộ (không bao giờ chép vào thư mục `skills/`, `plugins/` hay đồng bộ lên kho Git Public).
