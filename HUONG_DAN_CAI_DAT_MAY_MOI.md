# 🚀 HƯỚNG DẪN CÀI ĐẶT SANG MÁY MỚI TỪ A ĐẾN Z (`Tomi-antigravity-subagent`)

> Chỉ cần làm đúng **3 Bước** bên dưới là máy tính Windows mới sẽ có trọn bộ **14 Team (51 Subagents) + 41 Global Skills + 4 Workflows + Bộ nhớ dài hạn + 2 Hooks (`PreInvocation` & `SessionStart`) + Chỉ mục FTS5 (`agy-skill-hub`)**.

---

## BƯỚC 1: CÀI ĐẶT CÁC PHẦN MỀM NỀN TẢNG TRÊN MÁY MỚI

### 1.1. Phần mềm BẮT BUỘC (3 phần mềm — bắt buộc có để chạy hệ thống 14 Team)

| STT | Phần mềm | Phiên bản khuyên dùng | Lệnh cài nhanh 1 dòng (PowerShell `winget`) / Link tải | Phục vụ cho |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Google Antigravity IDE** | Bản mới nhất | Tải tại [antigravity.google](https://antigravity.google) | Nền tảng chính chạy 14 Team / 51 Subagents |
| **2** | **Python** *(NHỚ TÍCH `Add python.exe to PATH`!)* | **3.11 – 3.13** *(khuyên 3.13)* | `winget install -e --id Python.Python.3.13` | Chạy Hooks, MCP `agy-skill-hub`, FTS5, `team_memory_cli.py`, mọi script |
| **3** | **Git for Windows** | Bản mới nhất | `winget install -e --id Git.Git` | Clone repo, kéo bản cập nhật, Team 13 nạp repo skill |

### 1.2. Phần mềm TÙY CHỌN (Chỉ cài cái nào ứng với Team anh sử dụng trên máy mới)

| Phần mềm | Dùng cho Team nào | Lệnh cài nhanh (`winget`) / Ghi chú |
| :--- | :--- | :--- |
| **Node.js (LTS 20/22)** | Team 2 (Web), Team 3 (UI/GSAP), Team 5 (Remotion), Team 10 (REA), Team 14 (Three.js) | `winget install -e --id OpenJS.NodeJS.LTS` |
| **FFmpeg & FFprobe** | Team 4, Team 5, Team 12 (YouTube), Team 14 (Short Video QA) | `winget install -e --id Gyan.FFmpeg` |
| **ODBC Driver 17 (hoặc 18) for SQL Server** | Team 8 (SAP B1 & Beas SQL — kết nối SQL Server qua `pyodbc`) | `winget install -e --id Microsoft.msodbcsql.17` |
| **XAMPP (Apache + MySQL + PHP)** | Team 2 (WordPress Flatsome local) & Team 6 | Tải tại [apachefriends.org](https://www.apachefriends.org) |
| **OpenSSH Client & `sshpass`** | Team 6 (Quản trị Linux VPS / SCP không tương tác) | `winget install -e --id xhcoding.sshpass-win32` |
| **Google Chrome / Edge** | Team 1 (`qa-visual-human-tester`), Team 4, Team 14 (`Shopee Studio`) | Có sẵn trên Windows hoặc tải Chrome bản mới nhất |

*(Mở **PowerShell** gõ nhanh để cài 1 lượt toàn bộ phần mềm lõi + phổ thông):*
```powershell
winget install -e --id Python.Python.3.13
winget install -e --id Git.Git
winget install -e --id OpenJS.NodeJS.LTS
winget install -e --id Gyan.FFmpeg
```
*(Sau khi cài xong, đóng mở lại cửa sổ PowerShell mới để Windows nhận `PATH`.)*

---

## BƯỚC 2: TẢI REPO & CHẠY CÀI ĐẶT 1-CLICK (2 PHÚT)

1. **Tải (Clone) repo về máy mới:**
   ```powershell
   git clone https://github.com/thanhdientech/Tomi-antigravity-subagent.git
   cd Tomi-antigravity-subagent
   ```
2. **Bấm đúp chạy `CAI_DAT_1_CLICK_WINDOWS.bat`:**
   - Tự động copy đủ **14 Team Plugins (`plugins\team-*`)**, **41 Global Skills (`skills\`)**, **`rules\`**, **`docs\`**, **`scripts\`**, **`tools\`**, **`workflows\`** và khởi tạo khung **`team_memory\`** vào `%USERPROFILE%\.gemini\config\`.
   - Tự động đăng ký MCP Server `agy-skill-hub` vào `mcp_config.json` và cả 2 Hook (`PreInvocation` + `SessionStart`) vào `hooks.json`.
3. **Bấm đúp chạy `CAI_THU_VIEN_PYTHON_CHO_SKILLS.bat`:**
   - Tự động cài trọn bộ thư viện trong `requirements.txt` (xem bảng chi tiết ở Mục 3 bên dưới) và dựng lại chỉ mục SQLite FTS5 (`agy_skill_index.db`) chuẩn theo đường dẫn máy mới!

---

## BƯỚC 3: DANH SÁCH THƯ VIỆN PYTHON CÀI TỰ ĐỘNG (`requirements.txt`)

| Nhóm | Thư viện Python | Chức năng |
| :--- | :--- | :--- |
| **Lõi bắt buộc** | `pyyaml`, `mcp`, `requests`, `psutil`, `aiohttp`, `websockets` | Chạy MCP `agy-skill-hub`, phân tích frontmatter Skill/Agent, Bridge điều khiển trình duyệt thật `:8765/:8766`, kiểm tra HTTP 200 |
| **Dữ liệu & Office** | `pandas`, `openpyxl`, `pillow`, `beautifulsoup4`, `lxml` | Đọc/xuất CSV/Excel/Báo cáo Ads/Kế toán, xử lý ảnh PNG/WebP, kiểm toán HTML/SEO |
| **VPS & SQL SAP B1** | `paramiko`, `pyodbc`, `sqlalchemy` | SSH/SCP tự động tới Linux VPS (Team 6), kết nối Read-Only tới SQL Server SAP B1 (Team 8) |
| **YouTube & Tử Vi** | `scrapetube`, `iztro-py` | Quét dữ liệu kênh/video YouTube (`Tim Ngach` Team 12), an sao Tử Vi chuẩn |

---

## BƯỚC 4: CẤU HÌNH BỔ SUNG CHO CÁC TEAM ĐẶC THÙ (NẾU DÙNG)

1. **Team 8 (SAP B1 SQL):** Vì đây là repo **PUBLIC**, toàn bộ tài khoản & mật khẩu SQL Read-Only đã bị chặn không đẩy lên Git. Nếu máy mới cần kết nối SQL nội bộ:
   - Copy thủ công 2 file nội bộ của anh từ máy cũ sang đúng vị trí ở máy mới:
     - `%USERPROFILE%\.gemini\config\tools\sql_runner.py`
     - `%USERPROFILE%\.gemini\config\skills\sql-sap-b1\config.json` *(hoặc điền từ `config.example.json`)*
2. **Team 12 (YouTube Factory) & Team 14 (Short Video Shopee):**
   - Các bộ tool render nặng (`Tool render edit Video` OmniFlash, `Tim Ngach`, `Shopee_KOL_Studio_Tool`, `Nghien_Cuu_Kenh_Moi_Huong_Dan`) nằm riêng ngoài repo config. Khi sang máy mới, chép thư mục tool vào ổ đĩa (khuyên giữ nguyên cấu trúc) và chạy `pip install` trong `.venv` của từng tool tương ứng.
3. **Kết nối kho tri thức ngoài (JavisOS / Obsidian Wiki):**
   - Đặt biến môi trường Windows `JAVIS_BRAIN_DIR` trỏ tới thư mục chứa `brains\Brain Default\wiki` để lệnh `team_memory_cli.py --search-wiki "..."` tự động tìm được tài liệu của anh.
4. **Cài Extension "Antigravity Browser" để 100% 14 Team điều khiển trình duyệt thật (Chrome / Cốc Cốc / Edge):**
   - Mở `chrome://extensions/` (hoặc `coccoc://extensions/` / `edge://extensions/`) trên từng Profile muốn cho AI điều khiển → bật **Developer mode** → bấm **Load unpacked** → chọn thư mục:
     `%USERPROFILE%\.gemini\config\skills\antigravity-browser-controller\extension`
   - Bấm icon **Antigravity Browser** đặt tên Profile (vd: `work`, `ads`, `youtube`) → bấm **Lưu**.
   - Bật Bridge & dò toàn bộ Profile trên máy bằng 1 lệnh:
     ```powershell
     python "%USERPROFILE%\.gemini\config\skills\antigravity-browser-controller\scripts\profile_scanner.py" --ensure-bridge
     python "%USERPROFILE%\.gemini\config\skills\antigravity-browser-controller\scripts\profile_scanner.py" --scan
     ```

---

## BƯỚC 5: KIỂM CHỨNG SAU KHI CÀI XONG TRÊN MÁY MỚI (`Exit code 0`)

Mở PowerShell chạy 3 lệnh kiểm tra nhanh:
```powershell
# 1. Kiểm tra danh sách 14 Team trong bộ nhớ
python "$env:USERPROFILE\.gemini\config\tools\team_memory_cli.py" --list-teams

# 2. Kiểm tra Hook SessionStart chạy sạch Exit code 0
'{"workspacePaths":["C:\\test"]}' | python "$env:USERPROFILE\.gemini\config\scripts\session_memory_loader_hook.py"

# 3. Kiểm tra chỉ mục FTS5 & 0 trùng lặp
python -c "import sys, os; sys.path.insert(0, os.path.expanduser('~/.gemini/config/scripts')); import agy_skill_engine; print(agy_skill_engine.get_engine().audit_report(force_rebuild=False)['sync'])"
```
Sau đó mở lại **Google Antigravity App** → vào mục **Customizations → Plugins** → kiểm tra 14 Team đã hiện đủ (nên luôn bật **Team 0 + Team 1**, các Team 2–14 bật theo mảng đang làm) → mở **`+ New Conversation`** và bắt đầu gọi Team theo [README.md](./README.md)!
