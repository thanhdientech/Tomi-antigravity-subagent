# Luật Vận Hành Team 0 — Lên Kế Hoạch & Chốt Đặc Tả Với Người Dùng TRƯỚC Khi Làm

Toàn bộ thành viên Team 0 bắt buộc tuân thủ 4 thiết luật của Cổng Chặn Thực Thi Sớm (Zero Premature Execution Gate):

1. **Cấm Code Sớm 100%:** Khi đang ở Team 0, tuyệt đối KHÔNG viết code chức năng, KHÔNG sửa DB/Server, KHÔNG dựng giao diện khi người dùng chưa duyệt file `BLUEPRINT_<TEN_DU_AN>.md` (hoặc chưa chọn Phương án).
2. **Khảo Sát Trước Khi Hỏi (`Context First`):** Luôn đọc workspace, cấu trúc thư mục, file cấu hình hoặc DB schema sẵn có trước; tuyệt đối không hỏi lại người dùng những gì dự án đã có.
3. **Không Để Chữ Mập Mờ:** File `BLUEPRINT_<TEN_DU_AN>.md` cấm chứa `"TBD"`, `"TODO"`, `"xử lý sau"` hoặc tên skill bịa đặt không tồn tại trên máy.
4. **Kiểm Định Tự Động `Exit code 0` Trước Khi Trình Duyệt:** Luôn chạy `python %USERPROFILE%\.gemini\config\skills\project-blueprint-architect\scripts\validate_blueprint.py` để xác nhận file Blueprint đạt chuẩn trước khi trình người dùng ký duyệt.
