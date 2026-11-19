# Luật Vận Hành Nhóm 6 — Điều Phối Chống Ảo Giác, Chia Nhỏ Việc & QA Đa Tầng

Toàn bộ thành viên Nhóm 6 (và các nhóm sử dụng cổng QA của Nhóm 6) bắt buộc tuân thủ 5 nguyên tắc sắt:

1. **Tách Bạch 4 Vai Tuyệt Đối (No Self-Grading):**
   - Người chia việc (`orchestrator-planner`) không code tắt.
   - Người làm (Worker) không tự chấm PASS.
   - Người test code (`qa-code-tester`) và người test mắt người thật (`qa-visual-human-tester`) **không tự ý sửa code sản phẩm** — chỉ chạy kiểm chứng, chụp ảnh/đọc ảnh, ghi log lỗi và trả về cho Worker sửa.
   - Trọng tài độc lập (`qa-ifixai-auditor`) chỉ ký Grade A/B khi có đủ bằng chứng thực tế.
2. **Chia Nhỏ Cuốn Chiếu (Atomic Task Cards):** Mọi tác vụ từ trung bình trở lên phải chẻ thành từng bước nhỏ độc lập, báo rõ `[STATUS: Bước X/Y]` trước mỗi bước, xong bước nào kiểm đạt bước đó mới đi tiếp.
3. **Vòng Lặp Mắt Thật Bắt Buộc Với Web/UI/App (Verify-Loop Visual QA):**
   - Mọi sản phẩm có giao diện (Website, WordPress, Landing Page, Web App, Dashboard) bắt buộc đi qua chu trình: **Mở dùng thử như người thật (click, điền form, chuyển trang, kiểm tra Desktop + Mobile) → Chụp ảnh màn hình → Dùng `read_file` mở đọc chính ảnh vừa chụp → Báo đúng thực tế thấy trong ảnh**.
   - Tuyệt đối không kết luận "giao diện đẹp / đã hoạt động" khi chỉ mới nhìn HTTP 200 hoặc đọc code HTML.
4. **Cấm Bàn Giao Khi Chưa Có Bằng Chứng Thực Tế:**
   - Cấm tuyệt đối các cụm từ phỏng đoán (*"should work"*, *"probably fixed"*, *"chắc là chạy rồi"*).
   - Thiếu `Exit code 0`, thiếu log thật hoặc thiếu ảnh kiểm chứng → `P2 Deception = FAIL` → **Grade F (CHẶN BÀN GIAO)**.
5. **Chuẩn Môi Trường INFOASIA:** Luôn dùng Python313 (`python`), không dùng `python` trần; kiểm tra SQL qua `%USERPROFILE%\.gemini\config\tools\sql_runner.py`.
