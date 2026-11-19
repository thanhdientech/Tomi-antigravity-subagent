# Sổ Tay Kinh Nghiệm Phim AI & Xây Kênh (Learned Patterns — Team 4)

1. **Chia cụm cuốn chiếu 25–30 cảnh/lần:** Không viết 1 lèo 100 cảnh trong 1 lượt tránh model bị đuối ý và cụt mô tả ở các cảnh cuối.
2. **Định dạng CSV chuẩn Excel/Studio:** Luôn ghi `encoding="utf-8-sig"` bằng Python313, verify bằng `csv.reader` đếm đủ số dòng & số cột trước khi bàn giao.
3. **Omni-Browser Bridge (`:8765/:8766`):** Luôn khởi động `scripts/server.py` bằng Python313 (`python`) và kiểm tra `/status` trước khi đăng tự động.
