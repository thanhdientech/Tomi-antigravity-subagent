# 📘 HƯỚNG DẪN SỬ DỤNG HỆ THỐNG 11 TEAM ANTIGRAVITY × JAVISOS (INFOASIA)

> **Cập nhật:** 19/11/2026 · **Trạng thái hệ thống:** `11/11 Teams LIVE` · `39/39 Subagents LIVE` · `43/43 Javis Wiki/Sources Pinned` · `SessionStart Hook ACTIVE`

---

## 1. 4 Cách Gọi Team & Điều Phối Công Việc

### Cách 1 — Gọi tự nhiên theo số Team *(Dùng hằng ngày — nhanh nhất)*
Chỉ cần nhắn tên Team + yêu cầu, Agent chính sẽ tự kích hoạt đúng Trưởng nhóm (`LEADER`), Thành viên (`MEMBER`) và Kiểm toán viên độc lập (`INDEPENDENT_AUDITOR`) theo `RULE #7`:

- *"Gọi **Team 0** phỏng vấn Grill-Me và lập Master Blueprint cho dự án X trước khi làm."*
- *"Gọi **Team 2** sửa website WordPress này rồi cho **Team 1** (`qa-visual-human-tester`) mở dùng thử như người thật, chụp & đọc ảnh kiểm tra."*
- *"Gọi **Team 8** check schema cột thật và viết T-SQL SAP B1 báo cáo tồn kho trên Server 160."*
- *"Gọi **Team 6** kiểm tra CPU, RAM, Disk, Nginx và SSL trên VPS Ubuntu..."*

### Cách 2 — Gọi đích danh 1 Subagent cụ thể *(Khi cần 1 chuyên gia chạy ngay)*
- *"Gọi `web-seo-geo-specialist` kiểm toán SEO & Schema JSON-LD cho trang `https://...`"*
- *"Gọi `ads-performance-specialist` kiểm toán file Google Ads CSV này và xuất Google Ads Editor CSV."*
- *"Gọi `qa-visual-human-tester` mở `http://localhost:81/...` click thử, chụp ảnh Desktop/Mobile & đọc ảnh báo lỗi."*
- *"Gọi `video-qa-verifier` kiểm tra `ffprobe` và trích frame PNG mở đọc kiểm tra phụ đề file `output.mp4`."*

### Cách 3 — Chạy trọn dây chuyền 4 pha chuẩn JavisOS *(Ép cứng QA + Auto-Retry + Tự lưu `MEMORY.md`)*
Nhắn theo mẫu:
> *"Chạy `javis_team_runner` cho **`<tên-team>`** với mục tiêu `...` (URL test: `...`, từ khóa wiki: `...`)"*

Hệ thống chạy workflow `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py` theo đúng 4 pha:
1. **Pha 1 (`Plan`):** Đọc `MEMORY.md` của Team + tra JavisOS Wiki → chia Atomic Steps & tiêu chí QA.
2. **Pha 2 (`Work`):** Giao đúng chuyên gia trong Team thực thi.
3. **Pha 3 (`Verify` + `Auto-Retry`):** Chạy song song `qa-code-tester` + `qa-visual-human-tester` (nếu có URL) + Auditor chuyên ngành. Nếu `FAIL` → tự động trả lỗi cho Worker sửa 1 vòng rồi kiểm lại.
4. **Pha 4 (`Synthesize` + `Long Memory`):** `qa-ifixai-auditor` ký Scorecard A–F → tự động ghi nhật ký `runs/` và bài học vào `MEMORY.md`.

### Cách 4 — Dùng Slash Command (`/`) chính chủ của Antigravity
Gõ `/` trong khung chat rồi chọn:

| Lệnh `/` | Khi nào dùng |
| :--- | :--- |
| **`/plan`** | Muốn lập bản kế hoạch chi tiết từng bước để anh duyệt trước khi sửa code. |
| **`/grill-me`** | Muốn AI phỏng vấn hỏi xoáy gỡ điểm mù thiết kế trước khi làm. |
| **`/boost`** | Bug cực khó, thuật toán/lỗi hóc búa cần nhiều vòng phản biện & kiểm chứng sâu. |
| **`/swarm`** | Việc rộng chia tách được theo nhiều file/video độc lập — các worker bàn bạc song song trên 1 bảng tin chung (`@mention`) + có `@verifier`. |
| **`/teamwork`** | Dự án lớn nhiều ngày, nhiều cột mốc (`Sentinel`, `Project Orchestrator`, `Critic`, `Challenger`, `Auditor`, `Success Auditor`). |
| **`/goal`** | Cho Agent chạy bền bỉ liên tục cho đến khi hoàn thành trọn vẹn mục tiêu mới dừng. |
| **`/compact`** | Tóm tắt gọn hội thoại đang dài để giải phóng context window, tránh AI bị quên. |
| **`/schedule`** | Đặt lịch chạy định kỳ (cron) hoặc hẹn giờ tự động kiểm tra web/VPS/báo cáo. |
| **`/learn`** | Lưu lại bài học/sửa sai vừa xong để Agent nhớ lâu dài. |

---

## 2. Danh Bạ Nhanh 11 Phòng Ban & 39 Subagent Cố Định

> Bật/tắt lẻ từng Phòng Ban trong mục **Customizations** của Antigravity App. Nên luôn giữ bật **Team 0 + Team 1**, còn Team 2–10 bật theo mảng đang làm để tiết kiệm quota và nhẹ context.

| Team | Plugin (`plugins\team-*`) | Trưởng nhóm (`LEADER`) | Thành viên (`MEMBER`) | Kiểm toán độc lập (`INDEPENDENT_AUDITOR` — Cấm sửa file) | Câu gọi mẫu nhanh |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Team 0** | `team-planning-blueprint` | `solution-architect` | `blueprint-interviewer`, `blueprint-spec-validator` | *(Cấm code sớm 100%)* | *"Gọi Team 0 lập Master Blueprint cho dự án..."* |
| **Team 1** | `team-orchestrator-qa` | `orchestrator-planner` | — | `qa-code-tester`, `qa-visual-human-tester`, `qa-ifixai-auditor` | *"Gọi Team 1 test code + mở web chụp & đọc ảnh + chấm Scorecard"* |
| **Team 2** | `team-web-wordpress-seo` | `web-wp-builder` | `web-landingpage-coder`, `web-seo-geo-specialist` | `web-performance-auditor` | *"Gọi Team 2 dựng/sửa WordPress Flatsome hoặc kiểm toán SEO..."* |
| **Team 3** | `team-design-creative` | `design-ui-ux-architect` | `design-brand-identity`, `design-visual-asset-creator` | `design-ux-cro-auditor` | *"Gọi Team 3 thiết kế Logo SVG / CIP / UI-UX / dàn trang PDF..."* |
| **Team 4** | `team-video-film-channel` | `film-scriptwriter` | `film-prompt-director`, `film-studio-producer`, `channel-growth-automation` | *(QA qua Team 1 & Team 5)* | *"Gọi Team 4 viết kịch bản + CSV Prompt phim AI / xây kênh..."* |
| **Team 5** | `team-video-editing-motion` | `video-editor-ffmpeg` | `video-motion-coder`, `video-tutorial-producer` | `video-qa-verifier` | *"Gọi Team 5 edit video FFmpeg/Remotion/Recordly + soi frame MP4"* |
| **Team 6** | `team-server-vps-hosting` | `infra-linux-vps` | `infra-windows-server`, `infra-directadmin-hosting` | `infra-qa-security-verifier` | *"Gọi Team 6 kiểm tra VPS Ubuntu / DirectAdmin / XAMPP..."* |
| **Team 7** | `team-web-research` | `web-search-scout` | `web-synthesis-editor` | `web-fact-checker` | *"Gọi Team 7 tra cứu & kiểm chứng 2 nguồn đủ 4 tọa độ về..."* |
| **Team 8** | `team-sap-b1-sql` | `sap-b1-architect` | `sap-sql-developer` | `sap-accounting-auditor` | *"Gọi Team 8 check cột & viết SQL SAP B1/Beas trên Server..."* |
| **Team 9** | `team-marketing-ads` | `mkt-persona-strategist` | `ads-performance-specialist`, `mkt-copy-offer-creator` | *(QA qua Team 1)* | *"Gọi Team 9 vẽ chân dung 9 phần / kiểm toán Google Ads CSV..."* |
| **Team 10** | `team-reverse-security` | `rev-binary-analyst` | `rev-cleanroom-builder` | `sec-vulnerability-auditor` | *"Gọi Team 10 phân tích app bằng REA/Craft Anything & audit bảo mật"* |
| **Team 12** | `team-youtube-factory` | `yt-niche-radar` | `yt-content-writer`, `yt-prompt-director`, `yt-omniflash-renderer` | `yt-production-qa` | *"Gọi Team 12 quét ngách Tim Ngach hoặc sản xuất video OmniFlash cho kênh..."* |
| **Team 13** | `team-skill-curator` | `skill-repo-scout` | `skill-ingestor-builder` | `skill-security-qa` | *"Gọi Team 13 tìm/check repo skill GitHub & tư vấn nạp vào Antigravity"* |
| **Team 14** | `team-short-video-affiliate` | `short-channel-product-scout` | `short-script-storyboarder`, `short-kol-studio-producer` | `short-video-qa-auditor` | *"Gọi Team 14 làm video ngắn 9:16 Facebook Reels / Shopee Affiliate theo 13 kênh mẫu"* |

### 🧭 Sơ Đồ 3 Tầng Điều Phối Viên (Nhớ Nhanh)
- **Tầng 1 (Tổng Chỉ Huy):** Khung chat chính (Agent chính) nhận lệnh trực tiếp từ anh và tự định tuyến theo `RULE #7`.
- **Tầng 2 (Điều Phối Chính & Chốt Kế Hoạch):** **Team 0 (`team-planning-blueprint`)** chốt kế hoạch & Master Blueprint trước khi làm → **Team 1 (`team-orchestrator-qa`, trưởng nhóm `orchestrator-planner`)** điều phối chia việc & ép chạy QA độc lập.
- **Tầng 3 (Điều Phối Nội Bộ):** Mỗi Team chuyên môn (Team 2–12) có 1 `LEADER` riêng điều phối các thành viên trong chính phòng mình.

---

## 3. Sử Dụng Bộ Nhớ Dài Hạn & Cầu Nối JavisOS Wiki (`team_memory_cli.py`)

Mỗi khi anh bấm **`+ New Conversation`**, hook `SessionStart` (`scripts\session_memory_loader_hook.py`) **tự động chạy 1 lần** để nạp danh bạ dự án `PROJECTS_INDEX.md` và nhận diện Team khớp với workspace hiện tại.

Các lệnh tra cứu & ghi trí nhớ thủ công hoặc để Agent tự chạy bằng Python313:

```powershell
$PY  = "python"
$CLI = "%USERPROFILE%\.gemini\config\tools\team_memory_cli.py"

# 1. Xem danh sách 11 Team, số tài liệu ghim & số lần chạy
& $PY $CLI --list-teams

# 2. Đọc bộ nhớ chung + 3 nhật ký gần nhất của 1 Team
& $PY $CLI --read team-sap-b1-sql

# 3. Đọc bộ nhớ riêng của 1 Subagent
& $PY $CLI --agent-read sap-sql-developer

# 4. Tìm nhanh trong toàn bộ kho JavisOS Wiki (47 bài) & Sources (82 file)
& $PY $CLI --search-wiki "WIP 154"

# 5. Lưu bài học mới cho Team hoặc riêng 1 Subagent (có chống trùng)
& $PY $CLI --learn team-web-wordpress-seo --lesson "Không define WP_HOME 2 lần trong wp-config.php"
& $PY $CLI --agent-learn sap-sql-developer --lesson "Luôn chạy --cols qua sql_runner.py trước khi viết JOIN"

# 6. Ghi nhật ký hoàn thành 1 ca làm việc vào runs/
& $PY $CLI --log-run team-web-wordpress-seo --agent web-wp-builder --task "Fix wp-config" --status PASS --summary "Đã bỏ dòng override domain cũ" --evidence "HTTP 200, 2745 posts"

# 7. Cập nhật danh bạ dự án đang làm (để mở chat mới không bao giờ quên)
& $PY $CLI --update-project --name "Ten Du An" --path "D:\path" --team "Team 2" --status "Dang chay" --next "QA Visual"
```

---

## 4. Quy Tắc Chạy Đa Luồng An Toàn (Chạy Song Song Nhiều Job)

1. **Nhân bản song song thoải mái:** Cùng 1 subagent (ví dụ `video-editor-ffmpeg`) có thể chạy song song nhiều bản sao cho Video A và Video B cùng lúc (qua nhiều `invoke_subagent`, nhiều hội thoại mở song song, `parallel` trong `run_workflow`, hoặc `/swarm`).
2. **Tách thư mục đầu ra:** Mỗi luồng song song bắt buộc có thư mục output riêng (hoặc `Workspace: "branch"` khi sửa chung repo code) để không ghi đè file nhau.
3. **Tránh đụng cổng Web Studio local (`:5186`, `:8500`, `:8600`):** Nếu luồng 1 đang render trên Studio `:5186`, luồng 2 dùng CLI (`ffmpeg` / `Remotion` / `Auto-Editor`) hoặc làm khâu kịch bản/giọng đọc/phụ đề `.SRT`.
4. **Bảo vệ CPU/GPU:** Tối đa **2–3 luồng render MP4 nặng** cùng lúc; các luồng nhẹ (biên kịch, viết prompt, sửa web, SQL, tra cứu, thiết kế) chạy song song 5–10 luồng thoải mái.

---

## 5. Nhóm Lệnh Phân Tích & Tái Lập Phần Mềm (`/mcp:craft-anything:*` — Team 10)

| Lệnh trong menu `/` | Chức năng thực tế |
| :--- | :--- |
| `/mcp:craft-anything:core_feature_explain` | Giải thích một tính năng của app/web hoạt động thế nào, kèm bằng chứng từng bước. |
| `/mcp:craft-anything:app_graphs_compare` | So sánh 2 phiên bản của cùng 1 ứng dụng xem bản mới thay đổi gì. |
| `/mcp:craft-anything:app_rebuild_claim_check` | Đối chiếu bản code mình vừa tái lập lại với bằng chứng từ bản gốc. |
| `/mcp:craft-anything:native_crash_explain` | Phân tích nguyên nhân & vị trí chương trình bị crash. |
| `/mcp:craft-anything:core_unknowns_review` | Rà soát toàn bộ các điểm còn bỏ ngỏ (`open unknowns`) để chốt dứt điểm, thu hẹp hoặc giải trình — chống đoán mò trước khi code tái lập. |
| `/mcp:craft-anything:runtime_run_plan` | Lập kế hoạch chạy thử ngắn, có kiểm soát để xác minh hành vi app. |

---

## 6. Bản Đồ Các File Hệ Thống Quan Trọng Trên Ổ Đĩa

- **11 Plugin Phòng Ban (39 Subagents):** `%USERPROFILE%\.gemini\config\plugins\team-*`
- **Kho Bộ Nhớ Phân Tầng 5 Lớp:** `%USERPROFILE%\.gemini\config\team_memory\` (`COMPANY_MEMORY.md`, `PROJECTS_INDEX.md`, `WIKI_BRIDGE.md`, `teams\`, `agents\`)
- **CLI Trí Nhớ & Tra Javis Wiki:** `%USERPROFILE%\.gemini\config\tools\team_memory_cli.py`
- **Workflow 4 Pha Chuẩn Javis:** `%USERPROFILE%\.gemini\config\workflows\javis_team_runner.py`
- **Luật Hệ Thống & Hook:**
  - `%USERPROFILE%\.gemini\config\GEMINI.md`
  - `%USERPROFILE%\.gemini\config\rules\AGENTS.md`
  - `%USERPROFILE%\.gemini\config\hooks.json`
  - `%USERPROFILE%\.gemini\config\scripts\auto_reanchor_hook.py` *(PreInvocation)*
  - `%USERPROFILE%\.gemini\config\scripts\session_memory_loader_hook.py` *(SessionStart)*
- **Hồ Sơ Kiến Trúc Tổng Thể:** `%USERPROFILE%\.gemini\config\docs\MASTER_BO_NHAN_SU_ANTIGRAVITY.md`
- **Kho Tri Thức Gốc JavisOS (Ghim Cứng):** `%JAVIS_BRAIN_DIR%\brains\Brain Default\` & `%JAVIS_BRAIN_DIR%\brains_team\Brain Default\`
