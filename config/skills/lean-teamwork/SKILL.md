---
name: lean-teamwork
description: "Điều phối đa tác tử (Lean Multi-Agent): tối ưu token, Atomic Task Cards, First-Time Right & kiểm chứng."
group: "Kiểm Toán & Điều Phối AI"
---

# Lean Teamwork Skill & Superpowers Protocol

<!-- JAVIS_TRIGGER_ARCHIVE_START -->
## Khi nào dùng (Triggers & Ngữ cảnh kích hoạt đầy đủ)

> Kích hoạt quy trình điều phối đa tác tử tinh gọn (Lean Multi-Agent Protocol), tối ưu hóa quota/token với Independent Evidence Gates và Atomic Task Cards. Sử dụng khi người dùng yêu cầu làm việc theo mô hình Lean Teamwork, tối ưu token, hoặc chia việc đa agent có kiểm soát chặt chẽ.
<!-- JAVIS_TRIGGER_ARCHIVE_END -->

- **Nguồn gốc / Kho Git Upstream:** [toyota-production-system/lean-agent (Lean TPS)](https://github.com/toyota-production-system/lean-agent) (`Điều Phối Đa Tác Tử`)

Hệ thống điều phối tinh gọn kết hợp kỷ luật thép từ **Superpowers** và cơ chế tối ưu hóa Quota & Token từ **Lean Teamwork Protocol**.

---

## 1. 3 Thiết Luật Bất Biến (The 3 Iron Laws)

Mọi agent và phiên làm việc kích hoạt skill này bắt buộc phải tuân thủ 3 thiết luật:

1. **Thiết Luật Nghiệm Thu (Iron Law of Verification)**:
   > *"NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE"*
   - Không được tuyên bố code chạy, bug đã sửa hay test đã pass nếu chưa chạy lệnh kiểm chứng trực tiếp ngay trong lượt làm việc.
   - Cấm tuyệt đối các từ ngữ phỏng đoán: *"should work"*, *"probably"*, *"looks correct"*, *"tôi tin rằng"*.
2. **Thiết Luật Nguyên Nhân Gốc & Làm Đúng Lần Đầu (Iron Law of Root Cause & First-Time Right Protocol)**:
   > *"NO FIXES WITHOUT ROOT CAUSE — FIRST-TIME RIGHT OVER TRIAL-AND-ERROR"*
   - Cấm sửa mò, thử sai hay sửa triệu chứng (symptom fixing). Phải đọc stacktrace, tái hiện lỗi ổn định và khoanh vùng chính xác trước khi chạm vào code.
   - **Khai tử tư duy "Blind Lean" (Tinh gọn mù quáng)**: Lean KHÔNG PHẢI là mù quáng không đọc tài liệu. Khi chạm vào kiến trúc, framework hay tính năng client mới, **BẮT BUỘC phải đọc tài liệu chuẩn (Inspect First đầy đủ)** để hiểu rõ mọi ràng buộc ngầm.
   - **Cấm đoán mò vì sợ tốn token đọc tài liệu**: Tiết kiệm 1.000 token đọc tài liệu ở đầu phiên mà để phát sinh >2 lượt chat thử-sai do đoán mò là **phạm luật Quota nghiêm trọng** (vì các lượt chat sau mang theo toàn bộ lịch sử khổng lồ làm tốn gấp 5 lần token và lãng phí thời gian của người dùng).
3. **Thiết Luật Tự Quyết Định & Hướng Đi Tốt Nhất (Ruling & Best-Path Fallback)**:
   > *"A RUNNING PLAN DOES NOT WAIT ON A HUMAN FOR MINOR CHOICES"*
   - Tự ra phán quyết cho các vấn đề vi mô kèm ghi chú rủi ro (`Ruling: <Quyết định> — <Lý do> — <Hệ quả nếu sai>`).
   - **Tự quyết khi quá thời gian chờ (Timeout Best-Path Fallback)**:
     - **Thời gian chờ mặc định**: **2.5 phút (150 giây)**.
     - **Hiển thị đếm ngược bắt buộc**: Khi đặt câu hỏi, luôn in rõ:
       `⏱️ Hạn phản hồi: 2.5 phút (đến HH:MM). Hết thời gian mà không có phản hồi, agent sẽ tự động thực hiện theo: [Phương án Recommended].`
     - **Kỹ thuật thực thi**: Trong Antigravity IDE trực tiếp, gọi `schedule` (`DurationSeconds: 150`, `TimerCondition: "any"`). **NGOẠI LỆ BẮT BUỘC TRONG JAVIS OS WEB UI / HEADLESS (`agy -p` hoặc có file `.javis_ngu_canh_*.md`)**: **TUYỆT ĐỐI KHÔNG GỌI `schedule`** (vì trong `agy -p`, `schedule` giữ tiến trình ngầm `waiting for 1 background task(s)` gây nghẽn lượt chat; đối với `invoke_subagent`, `agy` đã tự động đánh thức Agent cha khi xong).
     - Khi hết 2.5 phút: Agent tự động chọn phương án khuyến nghị và tiếp tục thực thi, không để phiên bị treo (never park the session).
   - Chỉ dừng lại chờ người dùng tuyệt đối khi gặp: (1) Thao tác phá hủy/xóa dữ liệu, (2) Thay đổi Auth/Security, (3) Tác động ngoài workspace, hoặc (4) Yêu cầu mâu thuẫn hoàn toàn đến mức mọi đường đi tiếp đều là phỏng đoán mù quáng.

---

## ⚖️ PHẦN BỔ SUNG: 2 BẢNG SO SÁNH CHẾ ĐỘ VẬN HÀNH & BẢN CHẤT GIỮA `GEMINI.md` VÀ `SKILL LEAN-TEAMWORK`

### BẢNG 1: So sánh 2 Chế độ vận hành `lean-teamwork` (Linh hoạt 2 Luồng vs. Ép cứng 100% mọi câu chat) (`🟡 [PHÂN TÍCH / ĐỀ XUẤT CỦA AI]`)

| Tiêu chí so sánh | Phương án 1 (Recommended) ⭐<br>**Tự Động Linh Hoạt 2 Luồng (Đang áp dụng)** | Phương án 2<br>**Ép Cứng 100% `Full lean-teamwork` Mọi Lúc** |
| :--- | :--- | :--- |
| **Cách hoạt động** | • **Hỏi ngắn / Tra cứu (Luồng 1):** Trả lời ngay + kèm nguồn thật (vẫn giữ kỷ luật không đoán mò, không làm ẩu).<br>• **Giao việc / Viết Code / SQL / Video / Kế toán (Luồng 2):** Tự động bật 100% `lean-teamwork` (Bảng phương án + Chia nhỏ Task Card + Test `Exit code 0` + Nghiệm thu `OK 💎`). | • **Bất kể anh gõ câu gì** (kể cả hỏi *"File này nằm ở đâu?"* hay *"Hi"*), AI đều phải dừng lại lập Bảng Phương Án (chờ 150s), tạo Task Card, chạy kiểm thử và cuối câu luôn bắt anh gõ `OK 💎` để đúc kết. |
| **Tốc độ phản hồi** | ⚡ **Rất nhanh (3–5 giây)** với câu hỏi tra cứu; **Chặt chẽ, chuẩn xác** với dự án lớn. | 🐢 **Chậm (tối thiểu 2 lượt chat hoặc chờ 150s)** cho cả những câu hỏi đơn giản nhất. |
| **Chi phí Token / Quota** | 💰 **Tiết kiệm 40%–60% Token** vì không sinh bảng biểu/widget thừa cho các câu hỏi nhỏ. | 💸 **Tốn gấp 2–3 lần Token** do câu hỏi 1 dòng cũng phải in Bảng phương án + Báo cáo nghiệm thu + chạy Subagent đúc kết. |
| **Trải nghiệm của anh** | Mượt mà, tự nhiên: Hỏi nhanh thì đáp gọn; giao việc lớn thì làm kỹ từng bước. | Dễ gây ức chế/mệt mỏi khi anh chỉ muốn hỏi nhanh 1 thông tin nhỏ mà AI cứ bắt chọn phương án. |
| **Độ an toàn / Chống làm ẩu** | 🛡️ **Đạt 100%** (vì 3 Thiết luật chống đoán mò & bắt buộc kiểm chứng vẫn bật ngầm 24/7). | 🛡️ **Đạt 100%** (nhưng dư thừa thủ tục ở các câu hỏi tra cứu). |
| **Độ phù hợp** | **10/10 (Tối ưu nhất cho thực chiến hàng ngày)** | **5/10 (Chỉ hợp khi chạy tự động 100% dự án lớn, không hỏi đáp ngắn)** |

---

### BẢNG 2: So sánh bản chất giữa `Quy Trình 5 Chốt Chặn (GEMINI.md)` và `Skill lean-teamwork` (`🟢 [ĐÃ XÁC MINH THỰC CHỨNG]`)

*(Hai bộ quy chuẩn này đóng **2 vai trò khác nhau** và ghép lại thành một chỉnh thể thống nhất)*:

| Tiêu chí | 🛡️ `QUY_TRINH_CHUNG_5_CHOT_CHAN` (`GEMINI.md`) | ⚙️ `lean-teamwork` (`skills/lean-teamwork/SKILL.md`) |
| :--- | :--- | :--- |
| **Bản chất cốt lõi** | **Là "Hiến Pháp Chống Bịa Đặt & Kiểm Soát Sự Thật"** cho các ngành nghề thực chiến. | **Là "Quy Trình Quản Lý Dự Án, Chia Việc & Tiết Kiệm Token"** khi thực thi. |
| **Câu hỏi nó giải quyết** | *"Thông tin/Số liệu này **có thật không, lấy ở đâu, trang nào, của ai**?"* | *"Làm sao để **chia nhỏ việc, làm đúng ngay lần đầu, không làm tắt và tốn ít token nhất**?"* |
| **Phạm vi bao phủ** | Toàn bộ **5 Chốt Chặn** + Ràng buộc chuyên môn đa ngành (Marketing, Ads, Video, SQL SAP B1, Kế toán TT 99/2025, Pháp lý, Y sinh...). | Phụ trách chuyên sâu **Chốt Chặn 1B** (Đề xuất kỹ thuật 150s), **Chốt Chặn 3** (Chia nhỏ Atomic Task Card, Root-Cause Debugging) và **Sau Chốt 5** (Nghiệm thu `OK 💎` $\rightarrow$ tự học vào `learned_patterns.md`). |
| **Công cụ đặc trưng** | • Hệ thống 2 Nguồn (`📂 Nguồn 1` & `🌐📖 Nguồn 2`) + 4 Tọa độ + Câu trích nguyên văn.<br>• Bảng Ánh Xạ Nguồn 6 cột.<br>• Nhãn độ tin cậy (`🟢 / 🟡 / 🔴`). | • Đồng hồ đếm ngược `150s` + Desktop Widget HUD (`teamwork_bridge.py`).<br>• Chia việc cho Subagents (`flash` / `pro`) + `Atomic Task Card`.<br>• Mật mã `OK 💎` / `ok::` để lưu bài học vào `learned_patterns.md`. |
| **Mối quan hệ** | **Là Khung Tổng (Cha):** Chứa `lean-teamwork` bên trong làm Chốt Chặn số 3. | **Là Động Cơ Thực Thi (Con):** Giúp AI chạy qua 5 Chốt Chặn một cách gọn gàng, cuốn chiếu và tự khôn lên sau mỗi lần bấm `OK 💎`. |

---

## 2. Hai Chế Độ Vận Hành

### Chế Độ 1: Daily Lean Mode (Sửa Bug & Tác Vụ Hàng Ngày 1–3 Files)
1. **Systematic Debugging & Pattern Retrieval**:
   - Khi gặp lỗi quen thuộc hoặc phức tạp: liếc nhanh [`~/.gemini/config/learned_patterns.md`](file:///%USERPROFILE%\.gemini\config/learned_patterns.md) để tái sử dụng ngay giải pháp đã từng thành công.
   - Đọc kỹ stacktrace/mã lỗi và tái hiện lỗi qua test case tối thiểu (Red Phase: test bắt buộc fail).
2. **Minimal Compatible Diff**:
   - Sửa đúng nguyên nhân gốc trong 1 thao tác diff nhỏ nhất.
   - Tự sửa lỗi cú pháp vi mô trong 1 lượt duy nhất (Zero-Spawn Minor Remediation).
3. **Green Verification**:
   - Chạy lại test -> Xác nhận PASS (exit code 0).
4. **Tự vấn Quota & Xin xác thực người dùng**.

### Chế Độ 2: Multi-Agent Lean Mode (Tác Vụ Lớn / Tái Cấu Trúc Đa Module)
1. **Intent Architect**: Phỏng vấn tạo và khóa [Execution Brief](./templates/execution_brief_template.md). Khi đặt câu hỏi làm rõ, luôn nêu rõ: *"Nếu không có phản hồi, sẽ tự động áp dụng phương án khuyến nghị để tiếp tục thực hiện."* Không viết code khi chưa chốt phương án.
2. **Subagent Cap (2–4 Subagents)**:
   - 1 Lead Orchestrator
   - Tối đa 2 Workers song song sở hữu file độc quyền
   - 1 Gatekeeper / Independent Auditor
3. **Isolated Context & Workspace Branching**:
   - Subagent **không kế thừa** toàn bộ lịch sử session chat khổng lồ của parent agent; chỉ nhận [Atomic Task Card](./templates/atomic_task_card_template.md).
   - Với tác vụ rủi ro cao: kích hoạt `Workspace: "branch"` trong `invoke_subagent` để cô lập thử nghiệm, bảo vệ an toàn 100% mã nguồn chính.
4. **Model Tiering**:
   - `Model: "flash"` hoặc `"flash_lite"`: Bắt buộc dùng cho Explorer khảo sát, Gatekeeper chạy test, đọc log.
   - `Model: "inherit"` hoặc `"pro"`: Dành riêng cho Lead Orchestrator và Worker viết thuật toán phức tạp.
5. **Compact Handoff**: Báo cáo giữa các agent bắt buộc dưới 20 dòng theo mẫu [Compact Handoff](./templates/compact_handoff_template.md).

---

## 3. Vòng Lặp Tự Vấn Quota Sau Mỗi Chu Kỳ (Cycle Reflection & Quota Audit)

Sau mỗi vòng sửa code / chạy test, agent tự đặt 4 câu hỏi tự vấn theo [Cycle Reflection Template](./templates/cycle_reflection_template.md):
1. **Về Số Lượt & Thử-Sai (Turn Budget & Churn Audit)**: *Task này đã tốn bao nhiêu lượt chat? (Ngưỡng cảnh báo: >2 lượt). Có bị thử-sai hay đổi hướng giải pháp nhiều lần không? Nếu CÓ: Tại sao? Có phải do ban đầu đoán mò vì thiếu tài liệu API/kiến trúc gốc không?*
2. **Về Quota & Token**: *Vừa rồi có đọc thừa file nào không? Log terminal có quá dài không? Có thể rút ngắn handoff hoặc lược bớt bước nào để tiết kiệm token ở vòng kế tiếp không?*
3. **Về Bằng Chứng (Anti-Rationalization Check)**: *Đã có bằng chứng khách quan (exit code 0, kết quả chạy thật) chưa, hay còn điểm nào phỏng đoán?*
4. **Về Tinh Gọn & Anti-Pattern**: *Có phát hiện mẫu lặp lại (pattern) cần lưu hoặc sai lầm thử-sai (anti-pattern) cần chặn không?*

---

## 4. Cổng Xác Thực Đích Đến Từ Người Dùng (Goal Confirmation Gate)

Khi tất cả các tiêu chí trong Execution Brief hoặc mục tiêu sửa bug đã đạt bằng chứng khách quan:
1. **Dừng lại và xin xác nhận rõ ràng**:
   > *"Tác vụ đã hoàn thành theo yêu cầu. Bạn đã kiểm tra và xác nhận OK chưa?"*
2. **Không tự đóng phiên**: Bắt buộc chờ phản hồi của người dùng trước khi chuyển sang bước đúc kết.

---

## 4.5. Chuyển Hướng Toàn Bộ Đề Xuất & Nghiệm Thu Về Desktop Widget Popover HUD (Widget HUD Decoupled — Rảnh Khung Chat 100%)

Hệ thống chuyển hướng toàn bộ khâu Đề xuất Kỹ thuật (🧭) và Nghiệm thu Hoàn thiện (💎) sang **Desktop Widget Popover HUD** thông qua IPC Bridge (`scripts/teamwork_bridge.py`), **BỎ HOÀN TOÀN modal `ask_question` cũ trong khung chat**:

### 1. 🧭 [CHẾ ĐỘ ĐỀ XUẤT KỸ THUẬT] 💡 (2 Lối Song Hành: Chat Stream + Widget HUD Popover)
- **Khi nào kích hoạt**: Khi vừa nhận yêu cầu mới, phân tích hướng đi, hoặc đứng trước các ngã rẽ kỹ thuật quan trọng.
- **Quy chuẩn thực thi 2 Lối Song Hành**:
  1. **Lối 1 (Khung Chat Antigravity)**:
     - Agent in trực tiếp danh sách phương án ra khung chat, đánh số thứ tự rõ ràng kèm phương án `[1] (Recommended) ⭐`.
     - **Chỉ gọi công cụ `schedule`** (`DurationSeconds: 150`, `TimerCondition: "any"`) khi đang chạy trực tiếp trên Antigravity IDE. **Nếu đang chạy qua Javis OS Web UI / Headless (`agy -p` hoặc đọc `.javis_ngu_canh_*.md`), TUYỆT ĐỐI KHÔNG gọi `schedule`** — in đề xuất xong là kết thúc lượt ngay để trả kết quả ra khung chat.
     - Nếu người dùng có mặt và gõ phím/chọn: Timer `schedule` tự hủy ngay lập tức.
     - Nếu người dùng vắng mặt: Hết 2.5 phút, `schedule` tự động đánh thức AI chọn phương án 1 và tiếp tục code, không để đứt đoạn mạch công việc.
  2. **Lối 2 (Desktop Widget HUD Popover)**:
     - Agent đồng thời gọi `teamwork_bridge.publish_proposal(title, options, duration_seconds=150)` để đẩy đề xuất lên Desktop Widget.
     - Widget tự động bung Popover to rõ trên Desktop với đồng hồ đếm ngược 7 màu Spectrum và danh sách phương án trực quan.
     - Người dùng có thể click chọn trực tiếp trên Desktop Widget (Widget tự động focus và gửi phím số xuống IDE).
     - **Tự động trả về 1 khi hết giờ**: Khi Widget đếm đủ thời gian (hết 150 giây) mà người dùng chưa bấm chọn gì, Widget sẽ **tự động gửi phím '1' về Antigravity IDE cho gọn** và tự đóng Popover!
  3. **TUYỆT ĐỐI KHÔNG GỌI modal `ask_question`**: Khung chat hoàn toàn rảnh rang, không bị modal pop-up chiếm chỗ hay đóng băng tiến trình.

### 2. 💎 [CHẾ ĐỘ NGHIỆM THU HOÀN THIỆN] ✨ (Widget HUD Decoupled — Treo Cố Định Widget)
- **Khi nào kích hoạt**: Khi code đã viết xong, toàn bộ kiểm thử tích hợp đạt 100% PASS (Exit Code 0).
- **Quy trình Nghiệm Thu Tách Nhịp 2 Bước Rảnh Khung Chat (Two-Beat Decoupled Acceptance)**:
  - **BƯỚC 1 (In Báo Cáo Ra Chat)**: In toàn văn Báo cáo phân tích, kết quả kiểm thử và hướng dẫn đối chứng thực tế ra màn hình chat. Khung chat hiển thị sạch sẽ, minh bạch.
  - **BƯỚC 2 (Treo Nghiệm Thu Trên Desktop Widget)**:
    - Agent gọi `teamwork_bridge.publish_acceptance(title, summary, exit_code=0, files_changed=[...])` để đẩy trạng thái Nghiệm Thu lên Desktop Widget.
    - Popover trên Desktop Widget tự động bung ra và **TREO CỐ ĐỊNH VĨNH VIỄN TRÊN WIDGET** theo **Cấu trúc Popup 2 Trạng Thái** kinh điển:
      1. `💎 [100% HOÀN TẤT] ✨` (Chấp thuận & Khóa tri thức tự động)
      2. `⚡ [SUPERPOWERS DEBUG] 🛠️` (Yêu cầu AI chuyên trách truy vết sâu)
    - **TUYỆT ĐỐI KHÔNG GỌI modal `ask_question`**: Loại bỏ hoàn toàn modal popup cũ trong khung chat. Người dùng kiểm tra đối chứng xong có thể bấm trực tiếp từ Desktop Widget bất kỳ lúc nào mà không lo bị che mất chữ trong khung chat.

### 3. Quy Trình Sửa Lỗi 4 Pha & Điểm Dừng Duy Nhất
- **Khi người dùng chọn nút 2 (`⚡ [SUPERPOWERS DEBUG] 🛠️`) trên Widget**:
  - Main Agent kích hoạt Subagent chuyên trách (`invoke_subagent`, model: `flash`, role: `Superpowers Debugger & Remediation Worker`).
  - Subagent thực thi chuẩn xác quy trình 4 pha từ [Superpowers Systematic Debugging](./references/systematic-debugging.md): (1) Root Cause -> (2) Hypothesis & Red Test -> (3) Minimal Fix -> (4) Green Verification.
- **Điểm dừng duy nhất & Chuẩn Hóa Mật Mã Nghiệm Thu (`OK 💎` / `ok::`)**:
  - Tín hiệu nghiệm thu hoàn tất duy nhất là mật mã **`OK 💎`** (được Desktop Widget tự động gửi khi bấm nút `💎 [100% HOÀN TẤT] ✨` hoặc do người dùng gõ `OK 💎`, hoặc phím tắt siêu tốc **`ok::`**).
  - **Quy tắc Chống Nhầm Lẫn (Anti-False-Acceptance)**: Các trao đổi thông thường chứa chữ "ok" (ví dụ: *"ok làm tiếp đi", "ok bạn", "ok nhé", "ok để mình xem"...*) TUYỆT ĐỐI KHÔNG phải là lệnh nghiệm thu hoàn tất. AI chỉ kích hoạt Self-Evolution khi nhận được mật mã có kèm emoji kim cương `OK 💎` (hoặc `💎 OK`, `[ACCEPT] 💎`, hoặc phím tắt siêu tốc `ok::`).
  - Khi bắt được mật mã `OK 💎` hoặc `ok::`, AI hiểu ngay 100% người dùng đã nghiệm thu chấp thuận và kích hoạt Subagent (`flash`, role: `Knowledge & Quota Synthesizer`) thực thi **Bộ Khung Tự Vấn Phản Tư 6 Chiều** và **Cơ chế Khử Phình Tri Thức** (Merge & Prune), rà soát lỗi trung gian từ mốc hoàn tất gần nhất vào `docs/learned_patterns.md` (hoặc `~/.gemini/config/learned_patterns.md`). Tuyệt đối không nạp vào `SKILL.md`.

---

---

> 📖 **Chi tiết đầy đủ:** Xem [DETAIL.md](./references/DETAIL.md) — chứa bảng tra cứu, checklist và ví dụ mở rộng.
