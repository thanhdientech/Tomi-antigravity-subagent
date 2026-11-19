# Sổ Tay Kinh Nghiệm SAP B1 & SQL (Learned Patterns — Team 8)

1. **Luôn check cột bằng `--cols` trước khi viết JOIN:** Không bao giờ đoán tên cột Beas (`BEAS_FTHAUPT`, `BEAS_FTSTL`, `BEAS_FTAPL`) hay bảng SAP B1 (`OIPF`, `OINV`, `OWOR`) bằng trí nhớ.
2. **Môi trường Python313 bắt buộc cho `sql_runner.py`:** Dùng `python` (đã có sẵn `pyodbc 5.3.0`, `pandas 3.1.1`, `openpyxl 3.1.5`).
3. **Phân tách kỳ kế toán:** Kỳ từ `01/01/2026` trở đi đối chiếu Thông tư `99/2025/TT-BTC`; dữ liệu lịch sử trước `2026` đối chiếu `200/2014/TT-BTC`.
