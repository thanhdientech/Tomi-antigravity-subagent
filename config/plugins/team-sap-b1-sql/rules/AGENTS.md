# Luật Vận Hành Team 8 — ERP SAP Business One, Beas & Kế Toán SQL

1. **Cấm Tuyệt Đối `UPDATE/INSERT/DELETE` Trực Tiếp Bảng Chuẩn SAP B1:** Mọi thao tác ghi dữ liệu SAP B1 bắt buộc qua **DI API / Service Layer / DTW** — tuyệt đối không viết SQL sửa thẳng bảng chuẩn (`OINV`, `OWOR`, `OJDT`, `OINM`...) gây mất bảo hành hãng.
2. **Tự Kiểm Tra Schema & Chạy SQL Bằng `sql_runner.py` (Không Nhờ SSMS):** Luôn kiểm tra tên cột thực tế bằng `python %USERPROFILE%\.gemini\config\tools\sql_runner.py --server <24|160|160hcm|160lt|52|27|41> --cols <Table>` trước khi viết query; tuyệt đối không bịa tên bảng/cột.
3. **Chuẩn Kế Toán & Tính Toán Xác Định:** Áp dụng Thông tư 99/2025/TT-BTC (từ 01/01/2026 thay TT 200/2014/TT-BTC); cấm tính nhẩm số tiền/thuế suất — luôn dùng SQL/Python313 đối chiếu chính xác `∑Nợ = ∑Có`.
4. **Bảo Mật Dữ Liệu Khách Hàng:** Không in thông tin hạ tầng nội bộ (`<INTERNAL_DB_HOST>`, `<INTERNAL_SAP_DB>`, IP/mật khẩu DB) ra tài liệu công khai cho bên ngoài.
