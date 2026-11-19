# Hướng Dẫn Tạo User SQL & User Windows Dùng Chung Cho `INFOASIA AI AGENT`

Tất cả các máy chủ (`Con 24`, `Con 52`, `Con 160` và các máy chủ mở rộng sau này) sử dụng **cùng 1 tài khoản & mật khẩu duy nhất** để cấp cho `INFOASIA AI AGENT`:

- **Username dùng chung (cả SQL & Windows):** `<YOUR_RO_USER>`
- **Password dùng chung (cả SQL & Windows):** `<YOUR_RO_PASSWORD>`
- **Riêng Con 24 (`<INTERNAL_DB_HOST>` - SAP 10.0):**
  - Kết nối SQL vẫn dùng `<YOUR_RO_USER>` (`Read-Only 100%`, không dùng `sa`).
  - Kết nối ghi dữ liệu vào SAP B1 đi qua **SAP Service Layer (`https://<INTERNAL_SQL_SERVER_IP>:50000/b1s/v1`)** bằng tài khoản SAP **`manager`**.
- **Các máy còn lại (`Con 52`, `Con 160` - SAP 9.3):**
  - Chạy **100% Read-Only SQL (`<YOUR_RO_USER>`)**, khóa cứng `INSERT`, `UPDATE`, `DELETE`, `ALTER`, `EXEC`.

---

## 1. Danh Sách File Trong `%JAVIS_BRAIN_DIR%\create user\` & Trạng Thái Kiểm Thử

- **Con 24 (`<INTERNAL_SQL_SERVER_IP>` - Máy `INFOASIASAP24`, DB `<INTERNAL_DB_HOST>` - `Infoasia Demo Company`, SAP 10.0 + Beas):**
  - **SQL Read-Only (`<YOUR_RO_USER>`):** Đã test kết nối & truy vấn `SELECT` thành công 100% (`HasAccess = 1` trên `<INTERNAL_DB_HOST>`) + **SAP Service Layer (`:50000`)** `connected (HTTP 200)`.
  - **Windows User (`<YOUR_RO_USER>`) & mở rộng các DB phụ trên Con 24:** Chạy file `03_Run_All_OneClick_Setup.bat` (`Run as administrator`) hoặc chạy lệnh PowerShell/SQL ở Mục 2.A bên dưới.
- **Con 52 (`<INTERNAL_SQL_SERVER_IP>` - Máy `WIN-TTRG9UMG3IU` / `PENFLEX-VN-VM`, DB `PenflexPRD_NEW` - `PENFLEX VIETNAM CO.,LTD`, SAP 9.3 + Beas):**
  - **Đã hoàn tất 100% cả Windows User & SQL Read-Only User `<YOUR_RO_USER>` / `<YOUR_RO_PASSWORD>`** (`HasAccess = 1`, chặn cứng `UPDATE` với `Error 229`).
- **Con 160 (`<INTERNAL_SQL_SERVER_IP>` - Máy `INFOASIASAP03`, SAP 9.3 + Beas):**
  - **Đã test thành công 100%** trên `FVIVN_GoLive_2024` (`/160 hcm`) và `<INTERNAL_SAP_DB>` (`/160 lt`) (`HasAccess = 1`). Riêng `<INTERNAL_SAP_DB_TRAIN>` chạy thêm Mục 2.C bên dưới.

Danh sách 5 file trong thư mục **`%JAVIS_BRAIN_DIR%\create user\`**:
1. [`THONG_TIN_KET_NOI_USER_CAC_SERVER.txt`](file:///e:/DIEN%20APP/JavisOS/create%20user/THONG_TIN_KET_NOI_USER_CAC_SERVER.txt): File `.txt` tổng hợp toàn bộ thông tin kết nối, tài khoản, trạng thái test và lệnh copy-paste nhanh.
2. [`01_Create_SQL_ReadOnly_Agent_User.sql`](file:///e:/DIEN%20APP/JavisOS/create%20user/01_Create_SQL_ReadOnly_Agent_User.sql): Script T-SQL tự động tạo Login/User `<YOUR_RO_USER>` chỉ đọc dữ liệu (`REVOKE CONTROL`, `GRANT CONNECT`, `db_datareader`, `db_denydatawriter`, `DENY INSERT, UPDATE, DELETE, ALTER, EXECUTE`) trên tất cả Database SAP B1 của Con 24, Con 52, Con 160.
3. [`02_Create_Windows_Limited_Agent_User.ps1`](file:///e:/DIEN%20APP/JavisOS/create%20user/02_Create_Windows_Limited_Agent_User.ps1): Script PowerShell tạo User Windows `<YOUR_RO_USER>` thuộc nhóm `Users`, `Performance Monitor Users`, `Event Log Readers` (không có quyền `Administrators`).
4. [`03_Run_All_OneClick_Setup.bat`](file:///e:/DIEN%20APP/JavisOS/create%20user/03_Run_All_OneClick_Setup.bat): Chạy 1-click (`Run as administrator`) để thiết lập đồng thời cả Windows User và SQL User trên Con 24 (hoặc bất kỳ server nào).
5. [`HUONG_DAN_TAO_USER_SQL_VA_WINDOWS_DUNG_CHUNG.md`](file:///e:/DIEN%20APP/JavisOS/create%20user/HUONG_DAN_TAO_USER_SQL_VA_WINDOWS_DUNG_CHUNG.md): Tài liệu hướng dẫn chi tiết.

---

## 2. Câu Lệnh Rút Gọn Tạo Trên Con 24, Con 52, Con 160

### A. Chạy trên Con 24 (`<INTERNAL_SQL_SERVER_IP>` - `INFOASIASAP24` - Database `<INTERNAL_DB_HOST>`)

**Bước 1 — Tạo Windows User `<YOUR_RO_USER>` (Mở PowerShell `Run as Administrator` trên Con 24):**
```powershell
$u = "<YOUR_RO_USER>"
$p = ConvertTo-SecureString "<YOUR_RO_PASSWORD>" -AsPlainText -Force
if (!(Get-LocalUser -Name $u -ErrorAction SilentlyContinue)) {
    New-LocalUser -Name $u -Password $p -FullName "InfoAsia AI Agent RO" -Description "InfoAsia AI Agent Read-Only User" -PasswordNeverExpires -UserMayNotChangePassword
} else {
    Set-LocalUser -Name $u -Password $p -PasswordNeverExpires $true -UserMayNotChangePassword $true
    Enable-LocalUser -Name $u
}
@("Users", "Performance Monitor Users", "Event Log Readers") | ForEach-Object {
    Add-LocalGroupMember -Group $_ -Member $u -ErrorAction SilentlyContinue
}
Remove-LocalGroupMember -Group "Administrators" -Member $u -ErrorAction SilentlyContinue
```

**Bước 2 — Tạo/Chuẩn hóa SQL Read-Only User `<YOUR_RO_USER>` trên Con 24 (Chạy trong SSMS Con 24):**
```sql
USE [master];
GO
IF NOT EXISTS (SELECT 1 FROM sys.server_principals WHERE name = N'<YOUR_RO_USER>')
    CREATE LOGIN [<YOUR_RO_USER>] WITH PASSWORD = N'<YOUR_RO_PASSWORD>', DEFAULT_DATABASE = [<INTERNAL_DB_HOST>], CHECK_EXPIRATION = OFF, CHECK_POLICY = OFF;
ELSE
    ALTER LOGIN [<YOUR_RO_USER>] WITH PASSWORD = N'<YOUR_RO_PASSWORD>', DEFAULT_DATABASE = [<INTERNAL_DB_HOST>], CHECK_EXPIRATION = OFF, CHECK_POLICY = OFF;
ALTER LOGIN [<YOUR_RO_USER>] ENABLE;
GO

USE [<INTERNAL_DB_HOST>];
GO
IF NOT EXISTS (SELECT 1 FROM sys.database_principals WHERE name = N'<YOUR_RO_USER>')
    CREATE USER [<YOUR_RO_USER>] FOR LOGIN [<YOUR_RO_USER>];
ELSE
    ALTER USER [<YOUR_RO_USER>] WITH LOGIN = [<YOUR_RO_USER>];

REVOKE CONTROL TO [<YOUR_RO_USER>];
GRANT CONNECT TO [<YOUR_RO_USER>];
ALTER ROLE [db_datareader] ADD MEMBER [<YOUR_RO_USER>];
ALTER ROLE [db_denydatawriter] ADD MEMBER [<YOUR_RO_USER>];
GRANT VIEW DEFINITION TO [<YOUR_RO_USER>];
DENY INSERT, UPDATE, DELETE, ALTER, EXECUTE TO [<YOUR_RO_USER>];
GO
```

---

### B. Chạy trên Con 52 (`<INTERNAL_SQL_SERVER_IP>` - Database `PenflexPRD_NEW`) *(Đã chạy & test thành công 100%)*
```sql
USE [master];
GO
IF NOT EXISTS (SELECT 1 FROM sys.server_principals WHERE name = N'<YOUR_RO_USER>')
    CREATE LOGIN [<YOUR_RO_USER>] WITH PASSWORD = N'<YOUR_RO_PASSWORD>', DEFAULT_DATABASE = [PenflexPRD_NEW], CHECK_EXPIRATION = OFF, CHECK_POLICY = OFF;
ELSE
    ALTER LOGIN [<YOUR_RO_USER>] WITH PASSWORD = N'<YOUR_RO_PASSWORD>', DEFAULT_DATABASE = [PenflexPRD_NEW], CHECK_EXPIRATION = OFF, CHECK_POLICY = OFF;
ALTER LOGIN [<YOUR_RO_USER>] ENABLE;
GO

USE [PenflexPRD_NEW];
GO
IF NOT EXISTS (SELECT 1 FROM sys.database_principals WHERE name = N'<YOUR_RO_USER>')
    CREATE USER [<YOUR_RO_USER>] FOR LOGIN [<YOUR_RO_USER>];
ELSE
    ALTER USER [<YOUR_RO_USER>] WITH LOGIN = [<YOUR_RO_USER>];

REVOKE CONTROL TO [<YOUR_RO_USER>];
GRANT CONNECT TO [<YOUR_RO_USER>];
ALTER ROLE [db_datareader] ADD MEMBER [<YOUR_RO_USER>];
ALTER ROLE [db_denydatawriter] ADD MEMBER [<YOUR_RO_USER>];
GRANT VIEW DEFINITION TO [<YOUR_RO_USER>];
DENY INSERT, UPDATE, DELETE, ALTER, EXECUTE TO [<YOUR_RO_USER>];
GO
```

---

### C. Chạy bổ sung trên Con 160 (`<INTERNAL_SQL_SERVER_IP>` - Cấp thêm quyền cho Database `<INTERNAL_SAP_DB_TRAIN>`)
```sql
USE [<INTERNAL_SAP_DB_TRAIN>];
GO
IF NOT EXISTS (SELECT 1 FROM sys.database_principals WHERE name = N'<YOUR_RO_USER>')
    CREATE USER [<YOUR_RO_USER>] FOR LOGIN [<YOUR_RO_USER>];
ELSE
    ALTER USER [<YOUR_RO_USER>] WITH LOGIN = [<YOUR_RO_USER>];

REVOKE CONTROL TO [<YOUR_RO_USER>];
GRANT CONNECT TO [<YOUR_RO_USER>];
ALTER ROLE [db_datareader] ADD MEMBER [<YOUR_RO_USER>];
ALTER ROLE [db_denydatawriter] ADD MEMBER [<YOUR_RO_USER>];
GRANT VIEW DEFINITION TO [<YOUR_RO_USER>];
DENY INSERT, UPDATE, DELETE, ALTER, EXECUTE TO [<YOUR_RO_USER>];
GO
```
