# 🐍 PYTHON ENVIRONMENT — QUY TẮC BẮT BUỘC (KHÔNG ĐƯỢC BỎ QUA)

> **NGUYÊN NHÂN:** Máy anh INFOASIA có 2 Python song song:
> - `python` / `python.exe` trần → trỏ vào **uv-managed Python** do Antigravity quản lý → BỊ KHÓA `externally-managed-environment` → **CẤM dùng pip install**
> - `python` → Python gốc Windows → **CÓ ĐẦY ĐỦ THƯ VIỆN SAP/SQL**

---

## ✅ QUY TẮC CỨNG — MỌI SUBAGENT PHẢI TUÂN THỦ

### 1. LUÔN DÙNG ĐƯỜNG DẪN ĐẦY ĐỦ KHI CHẠY PYTHON

```powershell
# ✅ ĐÚNG — Dùng Python313 (gốc Windows, có pyodbc, pandas...)
python script.py

# ✅ ĐÚNG — pip install qua Python313
python -m pip install <package>

# ❌ SAI — TUYỆT ĐỐI KHÔNG dùng lệnh trần (bị sandbox chặn)
python script.py
pip install <package>
python -m pip install <package>
```

### 2. SHORTCUT — Tạo biến alias để dùng nhanh

```powershell
$PY = "python"
$PIP = "python -m pip"

# Sử dụng:
& $PY script.py
& $PY -m pip install pyodbc
```

### 3. CÁC THƯ VIỆN ĐÃ CÀI SẴN TRÊN Python313

| Thư viện | Phiên bản | Ghi chú |
|----------|-----------|---------|
| `pyodbc` | 5.3.0 | Kết nối SQL Server / SAP B1 |
| `pandas` | 3.1.1 | Xử lý bảng dữ liệu |
| `openpyxl` | 3.1.5 | Đọc/ghi Excel |
| `requests` | 2.34.2 | HTTP/API |
| `sqlalchemy` | 2.1.9 | ORM Database |
| `psutil` | 7.2.2 | System info |

### 4. NẾU CẦN CÀI THƯ VIỆN MỚI

```powershell
# Luôn dùng Python313 pip
python -m pip install <tên_thư_viện>

# Nếu gặp lỗi, thêm --user
python -m pip install --user <tên_thư_viện>
```

### 5. KIỂM TRA NHANH

```powershell
python -c "import pyodbc; print('OK:', pyodbc.version)"
# Kết quả đúng: OK: 5.3.0
```

---

## ⚠️ LÝ DO KỸ THUẬT

Từ Antigravity update (khoảng Nov 2026), lệnh `python` trần trong run_command của Agent bị chuyển hướng vào `python.cmd` của Antigravity (`%USERPROFILE%\aicoworker\app\nodejs\python.cmd`), được quản lý bởi `uv`. Python này theo **PEP 668** không cho phép `pip install` trực tiếp vào System Environment để bảo vệ cài đặt.

**Giải pháp vĩnh viễn:** Luôn gọi Python313 qua đường dẫn tuyệt đối.
