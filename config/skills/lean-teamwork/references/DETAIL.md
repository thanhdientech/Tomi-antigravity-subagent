# lean-teamwork — Chi Tiết Đầy Đủ

> File này chứa bảng tra cứu, checklist và ví dụ mở rộng của skill `lean-teamwork`.
> Được tách từ SKILL.md để tuân thủ giới hạn 24KB của Antigravity.
> Xem hướng dẫn chính tại [SKILL.md](../SKILL.md)

---

## 5. Nguyên Tắc Cách Ly Tri Thức & Tự Tiến Hóa (Knowledge Segregation & Continuous Self-Evolution)

> *"TUYỆT ĐỐI KHÔNG NẠP HẾT KINH NGHIỆM VÀO SKILL.MD — TRÁNH BẮT AGY PHẢI ĐỌC TOÀN BỘ MỖI LẦN KHỞI CHẠY"*

1. **SKILL.md là Bộ Quy Tắc Tối Giản (Orchestration Rules Only)**:
   - `SKILL.md` chỉ chứa luật chơi, cấu trúc điều phối và giao thức tương tác (<150 dòng). Tuyệt đối không nhồi nhét log sửa lỗi, bài học tình huống, hay code snippets mẫu vào đây.
2. **Kho Tri Thức Nằm Hoàn Toàn Bên Ngoài (External Segmented Store)**:
   - Mọi bài học đúc kết được lưu tại [`~/.gemini/config/learned_patterns.md`](file:///%USERPROFILE%\.gemini\config/learned_patterns.md) (cấp dự án) và `~/.gemini/config/learned_patterns.md` (toàn cục máy phát triển).
3. **Truy Xuất Đúng Tag Khi Cần (Progressive On-Demand Retrieval)**:
   - Khi bước vào tác vụ mới, agent **không đọc toàn bộ** kho tri thức.
   - Chỉ khi gặp đúng lỗi/chủ đề cụ thể (ví dụ: `[Database]`, `[Build]`, `[Network]`), agent mới dùng `grep_search` quét đúng `[Tag]` tương ứng để đọc đúng 2–3 dòng giải pháp tối thiểu. Nhờ đó, lượng token context ban đầu luôn ở mức thấp nhất.
4. **Cơ Chế Two-Way Adaptive Sync (Đồng bộ 2 chiều tự thích ứng giữa PC & Laptop)**:
   - Trước khi thực thi hoặc sau khi đúc kết tri thức: Liếc nhanh số hiệu phiên bản giữa folder gốc (`VERSION`) và máy tính (`~/.gemini/config/skills/lean-teamwork/VERSION`).
   - Chạy lệnh duy nhất `py sync_skill.py`:
     - **PULL**: Nếu folder gốc mới hơn (`ver_source > ver_installed`) -> Tự động kéo bản cập nhật vào máy tính.
     - **PUSH**: Nếu máy tính vừa học hỏi kiến thức mới (`ver_installed > ver_source`) -> Tự động đẩy ngược về folder gốc để PC/thiết bị khác dùng ngay.
     - **SYNC 2 CHIỀU**: Cân bằng 2 chiều tri thức `learned_patterns.md` (bảo toàn 100% bài học ở cả 2 nơi).
   - Tuyệt đối tuân thủ Zero-Scan Protocol: Không đọc quét lan man các file mã nguồn, tiết kiệm 100% quota token.
5. **Phá Bỏ Thiên Lệch Kẻ Sống Sót & Kiểm Toán Thử-Sai Từ Lần Hoàn Tất Gần Nhất (Anti-Survivorship Bias, Trajectory Churn Audit & From-Last-Completion Retrospective Anchor)**:
   - **Biên độ tổng hợp bắt buộc từ lần bấm Hoàn tất gần nhất (From-Last-Completion Anchor)**: Nếu người dùng chưa bấm Hoàn tất vì còn lỗi và tiếp tục trao đổi qua nhiều lượt chat trung gian, khi người dùng bấm `💎 [100% HOÀN TẤT] ✨`, Subagent đúc kết BẮT BUỘC phải rà soát và tổng hợp TOÀN BỘ chuỗi lỗi, các giả định sai và các lần sửa **TỪ LẦN BẤM HOÀN TẤT GẦN NHẤT ĐẾN NAY**, tuyệt đối không được bỏ sót bất kỳ lỗi trung gian nào.
   - **Cấm chỉ nhìn vào kết quả thành công cuối cùng (Anti-Survivorship Bias)**: Tuyệt đối không chỉ nhìn vào Git diff cuối cùng hay lượt chat chót mà bỏ qua các lần test đỏ, exception hay phản hồi chỉnh sửa của người dùng ở các lượt giữa.
   - **Kiểm toán số lượt hội thoại (Turn Budget Audit)**: Nếu tác vụ tốn >2 lượt chat mới xong, Subagent BẮT BUỘC phải mổ xẻ nguyên nhân gốc: *Tại sao lần đầu làm sai? Có phải do cấm đoán đọc tài liệu chuẩn dẫn đến phỏng đoán mò mẫm không?*
   - **Đúc kết Anti-Pattern song song**: Rút ra cả `[Pattern]` (cách làm đúng) và `[Anti-Pattern]` (những phán đoán/thao tác sai lầm cấm lặp lại) lưu vào `learned_patterns.md`.
6. **Bộ Khung Tự Vấn Phản Tư 6 Chiều & Khử Phình Quy Tắc (6-Point Reflective Inquiry & Anti-Rule-Bloat)**:
   - **Chống phình to quy tắc (Anti-Rule-Bloat)**: Không tích lũy vô hạn. Subagent sau nghiệm thu tự vấn 6 câu (Nguyên nhân thử-sai, Làm chuẩn lần 1, Tiết kiệm quota, Tăng tốc tiến trình, Khử quy tắc thừa, Tự vấn đệ quy & Rà soát điểm nghẽn mãn tính).
   - **Nén, Tỉa & Trị Điểm Nghẽn Mãn Tính (Merge, Prune & Remediate)**: Hợp nhất các mẫu tương tự, tỉa bỏ quy tắc lỗi thời và tự động hành động khắc phục những điểm nghẽn đã cải tiến nhiều lần mà chưa mượt, giữ kho tri thức luôn súc tích và bộ não AI luôn sắc bén.
7. **Kiểm Toán & Tinh Gọn Kỹ Năng Sẵn Có Qua 3–4 Chu Kỳ Nghiệm Thu (Multi-Cycle Skill Usage Audit & On-Demand Context Pruning)**:
   - **Rà soát chuỗi 3–4 mốc nghiệm thu gần nhất**: Khi kết thúc nhiệm vụ, Subagent đúc kết (hoặc Agent nghiệm thu) BẮT BUỘC nhìn lại toàn bộ quá trình qua 3–4 chu kỳ nghiệm thu gần đây để đánh giá danh mục các kỹ năng sẵn có trong Antigravity (`~/.gemini/config/skills/`):
     - *Kỹ năng nòng cốt & đang dùng*: Giữ nguyên các skill thiết yếu (`lean-teamwork`, `git-workflow`, `agentic-engineering`, v.v.) và các skill thuộc tech-stack dự án hiện tại.
     - *Kỹ năng thừa cần tắt bớt*: Tạm tắt các skill hoàn toàn không đụng tới trong suốt 3–4 chu kỳ vừa qua hoặc không thuộc tech-stack của dự án (ví dụ: `laravel-*`, `django-*`, `quarkus-*`, `blender-*`, `csharp-*`, `fsharp-*`, `homelab-*`...) bằng cách chuyển vào `~/.gemini/config/skills_archive/` (hoặc chạy `py scripts/manage_skills.py --prune`). Việc này giải phóng hàng nghìn token trong system prompt ở mọi lượt gọi model tiếp theo.
   - **Báo cáo minh bạch & Gọi lại tức thì khi cần (Transparent Report & Instant Recall On-Demand)**:
     - Báo cáo rõ ràng trong phần đúc kết: Danh sách các skill đã tắt và lý do tắt để tiết kiệm Context Window.
     - Luôn đính kèm hướng dẫn: Các skill này không hề bị mất. Bất cứ khi nào cần lại skill nào trong tương lai, người dùng hoặc AI chỉ cần yêu cầu: *"Bật lại skill [tên skill]"* (hoặc chạy `py scripts/manage_skills.py --restore <tên_skill>`), kỹ năng sẽ lập tức được kích hoạt trở lại 100%!
8. **Chuyển Giao Kỹ Năng Động & Dự Phóng Nhu Cầu Đón Đầu (Predictive Skill Switcher & Sandboxing)**:
   - **Skill Sandboxing (Cô lập skill kiểm thử nặng qua Subagent)**: Cấm bơm các skill nặng (`browser-qa`, `e2e-testing`, `a11y-debugging`, `postgres-patterns`...) trực tiếp vào Main Context. Các tác vụ kiểm thử và rà soát chuyên sâu bắt buộc được ủy quyền cho Subagent độc lập (`Model: "flash"`). Khi Subagent kết thúc, toàn bộ context của skill đó tự động tiêu biến, giữ cho Main Context luôn tinh gọn tuyệt đối.
   - **Speculative Next-Step & Skill Proposal (Dự phóng nhu cầu tại Bước 1 Nghiệm Thu)**: Tại Bước 1 của Chế độ Nghiệm Thu, Agent nắm giữ trọn vẹn bức tranh kỹ thuật vừa hoàn thành và BẮT BUỘC dự phóng 2-3 kịch bản logic tự nhiên tiếp theo kèm danh mục kỹ năng đón đầu (chạy `py scripts/manage_skills.py --predict <domain>`):
     - Xác định rõ: (1) Tính năng đã xong $\rightarrow$ (2) Dự phóng kịch bản tiếp theo $\rightarrow$ (3) Kỹ năng đề xuất cất gọn (`unload`) $\rightarrow$ (4) Kỹ năng đề xuất nạp đón đầu (`preload`).
   - **Dynamic Skill Switch & Clean-Slate Turn (Chuyển giao kỹ năng động)**: Sử dụng lệnh `py scripts/manage_skills.py --switch --unload <a,b> --load <c,d>` để tự động cất kỹ năng cũ và nạp kỹ năng mới, triệt tiêu 100% xung đột quy tắc (Instruction Drift) và ô nhiễm ngữ cảnh (Context Bloat).
9. **Kho Thẩm Mỹ UI/UX Riêng & Tự Động Nạp Gu Thiết Kế (Dedicated UI/UX Design DNA & Auto-Taste Injection)**:
   - **Tách bạch kho tri thức (Knowledge Segregation)**: Toàn bộ quy chuẩn thẩm mỹ (Dark theme `#0D1117`, Acrylic Glassmorphism, bo góc Squircle 12-16px, macOS Spectrum 7 màu, Pill buttons, Anti-patterns) được lưu tại kho chuyên biệt [`docs/ui_ux_taste_profile.md`](../../docs/ui_ux_taste_profile.md), tuyệt đối không nhồi nhét vào `learned_patterns.md` để tránh làm rác ngữ cảnh khi thực hiện các tác vụ Backend/Script.
   - **Khối Design DNA Siêu Tinh Gọn (~150 Tokens)**: Khi phát hiện tác vụ có liên quan đến UI/UX, Agent tự động nạp khối `<UI_UX_DESIGN_DNA>` (trích xuất nhanh qua `py scripts/manage_skills.py --dna`) giúp AI thiết kế chuẩn xác ngay từ Turn 1 (First-Time Right UI), xóa bỏ 100% việc người dùng phải lặp đi lặp lại mô tả giao diện.
   - **Tự động trích xuất & cập nhật tại Nghiệm Thu**: Khi người dùng nghiệm thu `💎 [100% HOÀN TẤT] ✨`, Agent tự động tổng kết và cập nhật các tinh chỉnh thẩm mỹ mới nhất vào Taste Profile để các phiên làm việc sau luôn kế thừa trọn vẹn.

---

## 6. Tài Liệu Tham Chiếu Chi Tiết

- [Tích hợp Superpowers](./references/superpowers-integration.md)
- [Cẩm nang Systematic Debugging](./references/systematic-debugging.md)
- [Kiến trúc & Cổng bằng chứng](./references/architecture.md)
- [Quy tắc kiểm soát Quota & Token](./references/lean-protocol.md)
