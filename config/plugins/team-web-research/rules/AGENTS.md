# Luật Vận Hành Nhóm 5 — Tra Cứu & Kiểm Chứng Thông Tin Web (Chống Ảo Giác 100%)

Mọi tác vụ tìm kiếm, tổng hợp và đối chiếu thông tin trên Internet do Nhóm 5 phụ trách bắt buộc tuân thủ:

1. **Thà Nhận Không Biết Còn Hơn Bịa (Zero Hallucination):** Nếu tìm không ra tài liệu chính thống hoặc link không truy cập được, ghi rõ `⚠️ Không có thông tin / Chưa có tài liệu chính thống kiểm chứng`. Cấm tuyệt đối bịa URL, bịa ngày phát hành, bịa số trang hay tên tác giả.
2. **Đủ 4 Tọa Độ + Câu Trích Nguyên Văn (≤ 25 từ):** Mọi dữ kiện quan trọng phải gắn đủ: **Ở đâu** (Website/Tạp chí/Cổng TTĐT + URL sống `HTTP 200` / DOI / PMID) | **Bài/Văn bản nào** | **Trang/Mục/Điều khoản nào** | **Tác giả/Cơ quan (Ngày-Tháng-Năm)** | **Trích nguyên văn (`"..."` ≤ 25 từ)**.
3. **Ưu Tiên Nguồn Tier 1–2:** Ưu tiên tuyệt đối tài liệu chính thức của hãng (Google, Meta, SAP, Microsoft...), văn bản pháp luật trên Cổng TTĐT Chính phủ/Bộ ngành, và tạp chí/kho học thuật (`Nature`, `PubMed`, `arXiv`, `OpenAlex`). Hạn chế dùng blog tổng hợp lại không có nguồn gốc.
4. **Kiểm Tra Link Sống Thực Tế:** Dùng Python313 (`python`) hoặc `skills/verified-source-researcher/cli.py` kiểm tra HTTP status thực tế trước khi trích dẫn.
5. **Trình Bày Chuẩn 3 Tầng:** Tầng 1 nội dung đọc sạch 100% (không chèn tọa độ/nhãn vào giữa câu); Tầng 2 mục *Tài liệu tham khảo* gọn đẹp cuối bài; Tầng 3 bảng đối chiếu kiểm chứng 6 cột + nhãn `🟢 / 🟡 / 🔴` dành riêng cho người dùng trên chat hoặc file `_THAM_CHIEU_NGUON.md`.
