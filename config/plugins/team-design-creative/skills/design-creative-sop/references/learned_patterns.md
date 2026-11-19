# Sổ Tay Kinh Nghiệm Thiết Kế (Learned Patterns — Team 3)

1. **Font tiếng Việt khi xuất PDF / SVG / Typst / PPTX:** Luôn chọn font hỗ trợ đầy đủ dấu tiếng Việt (`Be Vietnam Pro`, `Inter`, `Roboto`, `Noto Sans`, `Plus Jakarta Sans`) để tránh lỗi rơi dấu hoặc ô vuông.
2. **Kiểm tra tràn lề & Responsive:** Luôn soi ảnh render thực tế bằng `read_file` ở cả 2 khổ Desktop (`1440px`) và Mobile (`390px`), hoặc từng trang PDF xuất ra PNG.
3. **Tái sử dụng Design Token:** Chốt bảng màu (Primary/Surface/Accent), font scale và spacing ngay từ đầu để đồng bộ 100% giữa Logo, Banner, Slide và Web UI.
