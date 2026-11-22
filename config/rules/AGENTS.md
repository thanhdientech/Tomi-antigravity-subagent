# 🤖 AGENTS.md — QUY TẮC CỐT LÕI CHO MỌI AGENT & SUBAGENT

> File này được nạp **TỰ ĐỘNG** vào mọi Agent và Subagent khi khởi tạo.
> Mọi Agent phải đọc và tuân thủ 100% — KHÔNG ĐƯỢC BỎ QUA.

---

## 🔴 RULE #1 — PYTHON ENVIRONMENT (CRITICAL)

**Máy INFOASIA có 2 Python song song — dùng SAI là lỗi ngay:**

```powershell
# ✅ ĐÚNG — Python313 (gốc Windows, có đủ thư viện SAP/SQL)
$PY = "python"
& $PY script.py
& $PY -m pip install <package>

# ❌ SAI — TUYỆT ĐỐI KHÔNG dùng (bị uv-sandbox chặn)
python script.py
pip install <package>
python -m pip install <package>
```

**Thư viện đã cài sẵn trên Python313:** `pyodbc 5.3.0` | `pandas 3.1.1` | `sqlalchemy 2.1.9` | `openpyxl 3.1.5` | `requests 2.34.2` | `psutil 7.2.2`

**CLI tools đã cài:** `sshpass` (winget xhcoding.sshpass-win32 v1.0.7) — dùng `-e` với `$env:SSHPASS` cho an toàn:
```powershell
$env:SSHPASS = "matkhau"
sshpass -e -k ssh -o StrictHostKeyChecking=no user@host "lệnh"
# Hoặc SCP:
sshpass -e -k scp -o StrictHostKeyChecking=no user@host:/remote/file C:\local\path\
```

> Chi tiết: `%USERPROFILE%\.gemini\config\rules\PYTHON_ENV_FIX.md`

---

## 🔴 RULE #1b — TỰ CHẠY SQL — KHÔNG NHỜ SSMS (CRITICAL)

**Agent TUYỆT ĐỐI KHÔNG nhờ người dùng mở SSMS chạy query thủ công.**
Dùng tool `sql_runner.py` để tự check schema, tự test query ngay trong Agent:

```powershell
$PY = "python"
$SQL = "%USERPROFILE%\.gemini\config\tools\sql_runner.py"

# Lấy danh sách cột của bảng
& $PY $SQL --server 160 --cols OIPF
& $PY $SQL --server 24  --cols OINV

# Chạy query tùy ý (Read-Only, tự động block INSERT/UPDATE/DELETE)
& $PY $SQL --server 160 --query "SELECT TOP 5 DocEntry, CostSum FROM OIPF"
& $PY $SQL --server 24  --query "SELECT TOP 3 DocNum, DocTotal FROM OINV"
& $PY $SQL --server 160lt --query "SELECT COUNT(*) FROM OIPF"

# Servers: 24 | 160 | 160hcm | 160lt | 52 | 27 | 41
# Credentials tích hợp sẵn: <YOUR_RO_USER> / <YOUR_RO_PASSWORD>
```

---

## 🔴 RULE #1c — ĐIỀU KHIỂN TRÌNH DUYỆT THẬT & DÒ ĐA PROFILE (PHỦ 100% 14 TEAM / 51 SUBAGENTS)

Mọi Agent & Subagent thuộc tất cả 14 Team khi cần thao tác trình duyệt như người thật (kiểm thử Web/WP Admin đã đăng nhập, Google Ads, YouTube Studio, Facebook, Shopee, chụp ảnh bằng chứng trên đúng Profile thật) đều dùng trực tiếp **Antigravity Omni-Browser Controller (`WS :8765` / `HTTP :8766`)**:

```powershell
$PY   = "python"
$SCAN = "%USERPROFILE%\.gemini\config\skills\antigravity-browser-controller\scripts\profile_scanner.py"
$CLI  = "%USERPROFILE%\.gemini\config\skills\antigravity-browser-controller\scripts\cli.py"

# 1. Đảm bảo Bridge :8765/:8766 đang chạy (tự bật nền nếu tắt, chống lỗi trùng cổng 10048)
& $PY $SCAN --ensure-bridge

# 2. Dò toàn bộ Profile Chrome / Cốc Cốc / Edge / Brave trên máy + danh sách đang kết nối live
& $PY $SCAN --scan

# 3. Tự tìm & mở kết nối bất kỳ Profile nào theo tên/email/thư mục (vd: "rjemma", "infoasia", "Profile 7")
& $PY $SCAN --open "<ten_hoac_email_profile>"

# 4. Thao tác như người thật trên đúng Profile (CHẠY NGẦM 0 cướp chuột/focus) + chụp ảnh & quay phim MP4:
$REC  = "%USERPROFILE%\.gemini\config\skills\antigravity-browser-controller\scripts\session_recorder.py"
& $PY $REC send-back --title "Chrome"                                   # Đẩy Chrome chìm sau cửa sổ người dùng (giữ GPU sống, không Minimize)
& $PY $REC start -p "<profile_key>" -o "session.mp4" --fps 2 --session r1  # Bắt đầu quay phim ngầm MP4 (chỉ quay đúng Tab AI làm)
& $PY $CLI -p "<profile_key>" tabs
& $PY $CLI -p "<profile_key>" goto "https://..."
& $PY $CLI -p "<profile_key>" click -t "Tên Nút"
& $PY $CLI -p "<profile_key>" screenshot -o "proof.png"                 # Chụp Silent CDP không cướp màn hình -> đọc bằng read_file
& $PY $REC stop --session r1                                            # Dừng quay & tự ghép MP4 bằng FFmpeg
```
- **Lưu ý bảo mật:** Luôn dùng profile đúng mục đích công việc người dùng yêu cầu; không tự ý vượt CAPTCHA hoặc thao tác thanh toán/xóa dữ liệu nhạy cảm khi chưa có xác nhận.

---

## 🔴 RULE #2 — VERIFY-LOOP PROTOCOL (KHÔNG ĐƯỢC BỎ QUA)

**Quy trình bắt buộc sau MỌI hành động:**

```
Làm → Chụp màn hình → Đọc kết quả → Sửa nếu sai → Mới giao
```

- ✅ Chụp screenshot sau mỗi bước
- ✅ Đọc nội dung ảnh — xác nhận đúng/sai
- ✅ Nếu sai → tự sửa, chụp lại, đọc lại
- ❌ KHÔNG giao khi chưa xác nhận kết quả
- ❌ KHÔNG nhờ người dùng làm thủ công nếu có thể script hóa

---

## 🔴 RULE #3 — KHÔNG TỰ LÀM KHÓ MÌNH (Anti-Excuse Protocol)

Agent **KHÔNG ĐƯỢC** nói:
- ❌ "Em không thể cài thư viện vì sandbox"
- ❌ "Anh cần làm bước này thủ công"
- ❌ "Em bị giới hạn không thể..."

**Thay vào đó:**
1. Thử Python313 path đầy đủ
2. Thử phương án thay thế (uv, venv, --user)
3. Script hóa tác vụ → để Agent tự thực thi
4. Chỉ báo cáo blocker thật khi đã thử hết 3 phương án

---

## 🔴 RULE #4 — LEAN-TEAMWORK (3 THIẾT LUẬT)

1. **Atomic Task & Status Report:** Làm từng bước nhỏ → **PHẢI báo cáo [STATUS: Bước X/Y] lên khung chat** → Check OK → Mới làm bước tiếp. CẤM làm ngầm.
2. **First-Time Right:** Làm đúng ngay lần đầu, không để lỗi chạy qua
3. **Timeout 150s:** Nếu chờ input người dùng > 150s → đề xuất phương án mặc định và tiếp tục

---

## 🔴 RULE #4b — BẢNG SO SÁNH PHƯƠNG ÁN (BẮT BUỘC TRƯỚC KHI THỰC THI)

Khi nhận yêu cầu **có nhiều hướng kỹ thuật/thiết kế** (không phải câu hỏi tra cứu ngắn), agent **BẮT BUỘC** lập bảng phương án trước khi viết bất kỳ dòng code/file nào:

```
📋 BẢNG SO SÁNH PHƯƠNG ÁN — [Tên tác vụ]

| # | Phương án | Ưu điểm | Nhược điểm | Khi nào dùng |
|---|-----------|---------|------------|--------------|
| [1] ⭐ Recommended | ... | ... | ... | ... |
| [2] | ... | ... | ... | ... |
| [3] (nếu có) | ... | ... | ... | ... |

⏱️ Hạn phản hồi: 2.5 phút (đến HH:MM). Hết giờ → tự chọn [1] và thực thi.
```

**Quy tắc:**
- ✅ In bảng ra chat TRƯỚC → chờ người dùng chọn hoặc hết 150s → mới thực thi
- ✅ Phương án [1] luôn là lựa chọn tốt nhất/an toàn nhất có giải thích rõ
- ❌ KHÔNG bắt đầu code/sửa file trước khi có phương án được chọn
- ❌ KHÔNG hỏi thêm nếu yêu cầu đã rõ 100% (Silent Pass — tránh hỏi vặt)

---

## 🔴 RULE #5 — IFIXAI AUDIT (5 TRỤ CỘT)

Trước khi giao kết quả, tự kiểm tra:
- **P1 Fabrication:** Có bịa số liệu/tên hàm/thư viện không?
- **P2 Deception:** Có che giấu lỗi/kết quả thật không?
- **P3 Manipulation:** Có ép người dùng chấp nhận kết quả chưa đúng không?
- **P4 Unpredictability:** Hành vi có nhất quán không?
- **P5 Opacity:** Có giải thích đủ để người dùng kiểm tra độc lập không?

**Điểm >= 80/100 (Grade A/B) mới được giao.**

---

## 🔴 RULE #6 — QA GATE BẮT BUỘC TRƯỚC KHI BÀN GIAO (MỌI DỰ ÁN, MỌI LĨNH VỰC)

> **TUYỆT ĐỐI KHÔNG** nói "Xong", "Đã sửa", "Đã hoàn thành" khi **chưa chạy kiểm chứng thực tế**.
> Cấm: *"should work"* | *"probably fixed"* | *"looks correct"* | *"đã sửa rồi"*

**Bảng bằng chứng bắt buộc theo loại tác vụ:**

| Loại tác vụ | Bằng chứng bắt buộc TRƯỚC khi báo "Xong" |
| :--- | :--- |
| Code / Script / SQL | Chạy thực tế → in `Exit code 0` + tóm tắt output thật |
| Web / WordPress / PHP | HTTP request → `HTTP 200` + không có chuỗi lỗi trong body |
| Database / wp-config | PHP/Python test kết nối → in `Connected! + số bản ghi` |
| File tạo / sửa | Đọc lại file vừa ghi → xác nhận nội dung đúng |
| SQL SAP B1 / ERP | `sql_runner.py` → in kết quả thực, không có lỗi syntax |
| Video / Storyboard CSV | Đếm đủ số dòng CSV + kiểm tra encoding `utf-8-sig` |
| Kế toán / Tính toán | Python/SQL tính lại → in `∑Nợ = ∑Có` hoặc kết quả số |
| Marketing / Content | File output tồn tại + đủ trường bắt buộc |
| Dịch thuật / Nội dung | Đọc lại đầu/cuối → xác nhận không cắt thiếu |
| Tử vi / Lá số | Hiển thị Bảng An Sao tường minh TRƯỚC khi luận giải |
| Y Sinh / Dược | In mã Accession / kết quả DB query thực tế |

**Nếu không có bằng chứng → PHẢI nói "Đang kiểm tra..." và chạy test ngay. KHÔNG được nói "xong".**

**Scorecard bắt buộc in ra sau mỗi tác vụ Luồng 2:**
```
╔══════════════════════════════════════════╗
║  iFixAi AUDIT — [Tên tác vụ]           ║
║  P1 Fabrication : PASS ✅ / FAIL ❌    ║
║  P2 Deception   : PASS ✅ / FAIL ❌    ║
║  P3 Manipulation: PASS ✅ / FAIL ❌    ║
║  P4 Predictable : PASS ✅ / FAIL ❌    ║
║  P5 Opacity     : PASS ✅ / FAIL ❌    ║
║  Bằng chứng: [exit code/HTTP/log thật] ║
║  GRADE: A/B/C/D/F                      ║
╚══════════════════════════════════════════╝
```
> P2 FAIL = Grade F = **KHÔNG bàn giao**. Phải sửa và test lại.

---

## 🔴 RULE #7 — TỰ ĐỘNG ĐIỀU PHỐI 11 PHÒNG BAN & CHẠY ĐA LUỒNG AN TOÀN

- **Luồng 1 (Hỏi nhanh / việc nhỏ 1 bước):** Agent chính xử lý trực tiếp luôn (Fast-Track), không gọi subagent thừa gây tốn quota.
- **Luồng 2 (Dự án mới / tính năng mới / tác vụ đa bước):** Agent chính **TỰ ĐỘNG** điều phối đúng dây chuyền 3 chặng (danh bạ đầy đủ: `docs\MASTER_BO_NHAN_SU_ANTIGRAVITY.md`):
  1. **Chặng 1 — Lên Kế Hoạch & Chốt Với Người Dùng (`Team 0`):** Gọi `blueprint-interviewer` / `solution-architect` / `blueprint-spec-validator` lập Bảng Phương Án & chốt trước khi code.
  2. **Chặng 2 — Thực Thi Đúng Phòng Ban Chuyên Trách:**
     - Web / WordPress / LP / SEO → **Team 2** (`web-wp-builder`, `web-landingpage-coder`, `web-seo-geo-specialist`)
     - Design / CIP / Logo / UI-UX / In ấn → **Team 3** (`design-brand-identity`, `design-ui-ux-architect`, `design-visual-asset-creator`)
     - Phim AI / Drama / Xây kênh → **Team 4** (`film-scriptwriter`, `film-prompt-director`, `film-studio-producer`, `channel-growth-automation`)
     - Edit Video / Motion / Remotion / FFmpeg → **Team 5** (`video-editor-ffmpeg`, `video-motion-coder`, `video-tutorial-producer`)
     - Server / VPS Linux-Win / DirectAdmin → **Team 6** (`infra-linux-vps`, `infra-windows-server`, `infra-directadmin-hosting`)
     - Tra cứu Web / Kiểm chứng nguồn → **Team 7** (`web-search-scout`, `web-fact-checker`, `web-synthesis-editor`)
     - SAP B1 / Beas / SQL / Kế toán → **Team 8** (`sap-b1-architect`, `sap-sql-developer`)
     - Marketing / Ads / Sản phẩm số → **Team 9** (`mkt-persona-strategist`, `ads-performance-specialist`, `mkt-copy-offer-creator`)
     - Dịch ngược / Clean-Room / Bảo mật → **Team 10** (`rev-binary-analyst`, `rev-cleanroom-builder`)
     - Nhà Máy YouTube Đa Ngách (`Tim Ngach` Radar + `OmniFlash` 16:9) → **Team 12** (`yt-niche-radar`, `yt-content-writer`, `yt-prompt-director`, `yt-omniflash-renderer`, `yt-production-qa`) + `workflows\youtube_factory_pipeline.py`
     - Săn, Kiểm Tra, Tư Vấn & Nạp Repo Skill vào Antigravity → **Team 13** (`skill-repo-scout`, `skill-ingestor-builder`, `skill-security-qa`) + `workflows\skill_curator_pipeline.py`
     - Video Ngắn 9:16 Facebook Reels / TikTok & Tiếp Thị Liên Kết Shopee (`:8600` + 13 Kênh Mẫu) → **Team 14** (`short-channel-product-scout`, `short-script-storyboarder`, `short-kol-studio-producer`, `short-video-qa-auditor`) + `workflows\short_video_affiliate_pipeline.py`
     - Build AI Agent JavisOS (Tomi `:7777` & InfoAsia `:7778` + Javis mới), Training Chống Bịa & Workflow n8n (`:5678/:5679`, VPS `42.29`) → **Team 15** (`javis-architect-builder`, `javis-anti-hallucination-trainer`, `n8n-workflow-engineer`, `javis-n8n-qa-auditor`) + `workflows\javisos_n8n_pipeline.py`
     - Custom Local Automation Plugins (tùy chọn mở rộng riêng trên máy người dùng)
  3. **Chặng 3 — QA Độc Lập Bắt Buộc (`Team 1` + Auditor chuyên ngành):** Gọi `qa-code-tester` (Exit code 0) + `qa-visual-human-tester` (mở web/app dùng thử thật → chụp ảnh → mở đọc ảnh bằng `read_file`) + `qa-ifixai-auditor` (Scorecard Grade A/B) trước khi bàn giao.
- **Bộ Nhớ Dài Hạn & Nối Cầu JavisOS Wiki (`team_memory_cli.py` + `javis_team_runner.py`):**
  - Đọc bộ nhớ nhóm & tài liệu Javis ghim cứng trước ca lớn: `& $PY %USERPROFILE%\.gemini\config\tools\team_memory_cli.py --read <team>` hoặc `--search-wiki "<từ_khóa>"`.
  - Sau khi xong ca lớn/sửa lỗi khó: ghi nhật ký `--log-run <team> ...`, rút bài học `--learn <team> --lesson "..."`, và cập nhật tiến độ dự án `--update-project ...` để không bao giờ mất ngữ cảnh khi mở chat mới.
  - Chọn đúng chế độ điều phối chuẩn Google Antigravity (`antigravity.google/docs/teamwork`): Tác vụ gọn → `invoke_subagent` | Dây chuyền lặp 4 pha có QA+Retry → `run_workflow` (`workflows\javis_team_runner.py`) | Bug cực khó → `/boost` | Nhiều file song song → `/swarm` | Dự án lớn nhiều ngày → `/teamwork`.
- **Quy tắc Chạy Đa Luồng An Toàn (Song Song Nhiều Job):**
  - Được phép nhân bản nhiều bản sao cùng `TypeName` chạy song song (`invoke_subagent` / `parallel`).
  - **Cấm đụng thư mục xuất file:** Mỗi job song song phải có thư mục output riêng (hoặc `Workspace: "branch"` khi sửa chung repo code).
  - **Cấm đụng cổng Studio local 1 cổng (`:5186`, `:8500`, `:8600`):** Nếu 1 luồng đang render trên Studio, luồng song song khác dùng CLI (`ffmpeg` / `Remotion` / `Auto-Editor`) hoặc làm khâu kịch bản/sub/asset; giới hạn tối đa **2–3 luồng render MP4 nặng** cùng lúc để bảo vệ CPU/GPU.

---

## 📋 AUDIT SCORECARD MẪU (In ra khi khởi tạo)

```
╔══════════════════════════════════════════════╗
║  AGENT AUDIT SCORECARD — Khởi động          ║
╠══════════════════════════════════════════════╣
║  Python ENV : Python313 ✅                   ║
║  Verify-Loop: BẬT ✅                         ║
║  Lean-Team  : BẬT ✅                         ║
║  P1 Fabric  : PASS ✅                        ║
║  P2 Deceive : PASS ✅                        ║
║  P3 Manip   : PASS ✅                        ║
║  P4 Predict : PASS ✅                        ║
║  P5 Opacity : PASS ✅                        ║
║  GRADE      : A ✅                           ║
╚══════════════════════════════════════════════╝
```
