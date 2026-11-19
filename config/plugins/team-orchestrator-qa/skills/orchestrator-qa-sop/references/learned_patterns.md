# Sổ Tay Kinh Nghiệm Điều Phối & QA (Learned Patterns — Nhóm 6)

> Mọi subagent Nhóm 6 đọc nhanh file này trước khi lập kế hoạch hoặc chạy QA để tránh các lỗi kinh điển.

## 1. Bẫy "HTTP 200 Nhưng Giao Diện Vẫn Lỗi"
- **Bài học:** Một trang WordPress/Web App có thể trả `HTTP 200` nhưng bên trong là trang trắng, hiện `Index of /`, vỡ CSS trên Mobile, ảnh lỗi `404`, hoặc nút bấm JavaScript không phản hồi.
- **Cách chặn:** Luôn kết hợp cả `qa-code-tester` (check HTTP/DB/Log) **VÀ** `qa-visual-human-tester` (mở trình duyệt tương tác thật → chụp ảnh → mở đọc ảnh bằng `read_file`).

## 2. Bẫy "Báo Xong Rồi Người Dùng Mở Thấy Lỗi" (P2 Deception)
- **Bài học:** Agent copy file xong liền báo "đã khôi phục xong" mà chưa kiểm tra `index.php`, `wp-config.php`, kết nối DB thực tế và mở thử URL.
- **Cách chặn:** `qa-ifixai-auditor` chấm ngay `P2 = FAIL / Grade F` cho mọi báo cáo không có `Exit code 0` + output thật + ảnh kiểm chứng (nếu là UI).

## 3. Bẫy "Sửa Xong Quên Dọn File Test Tạm"
- **Bài học:** Tạo file `test_db.php`, `_http_test.py` trong thư mục web `htdocs` rồi quên xóa gây rủi ro bảo mật.
- **Cách chặn:** `qa-code-tester` luôn kiểm tra và yêu cầu dọn sạch mọi file test tạm trước khi trả `PASS`.

## 4. Bẫy "Nhồi Quá Dài Vào Hook Gây Quên Ngữ Cảnh"
- **Bài học:** Tiêm prompt quá dài (>3.000 ký tự) ở mọi lượt chat khiến context bị đẩy mất thông tin dự án đang làm.
- **Cách chặn:** Giữ `orchestrator-planner` xuất Atomic Task Card ngắn gọn (mỗi thẻ ≤ 10 dòng), lưu trạng thái dự án ra file riêng thay vì dựa vào trí nhớ hội thoại.
