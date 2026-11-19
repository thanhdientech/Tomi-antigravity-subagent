"""
Workflow mẫu Nhóm 5: Săn nguồn (Scout) -> Kiểm chứng độc lập (Fact-Checker) -> Biên tập 3 tầng (Editor).
Chạy qua công cụ `run_workflow` với Args:
  {
    "topic": "Chủ đề hoặc câu hỏi cần tra cứu kiểm chứng",
    "output_path": "(Tùy chọn) Đường dẫn lưu file báo cáo cuối cùng"
  }
"""

topic = args.get("topic", "")
output_path = args.get("output_path", "")

if not topic:
    raise ValueError("Thiếu tham số bắt buộc: args['topic']")

phase("1. Web Search Scout")
scout_data = await agent(
    prompt=(
        f"Tra cứu thông tin chính thống (ưu tiên Tier 1-2) cho chủ đề:\n{topic}\n\n"
        f"Thu thập tối thiểu 2 nguồn độc lập, kiểm tra URL sống HTTP 200, "
        f"ghi đủ 4 tọa độ (Ở đâu/URL, Bài/Văn bản, Mục/Trang, Tác giả/Ngày) và câu trích nguyên văn <= 25 từ."
    ),
    type_name="web-search-scout",
    role="Web Search Scout",
    schema={
        "type": "object",
        "properties": {
            "findings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "claim": {"type": "string"},
                        "url": {"type": "string"},
                        "http_status": {"type": "integer"},
                        "title": {"type": "string"},
                        "section_or_page": {"type": "string"},
                        "author_date": {"type": "string"},
                        "exact_quote": {"type": "string"},
                    },
                    "required": ["claim", "url", "title", "author_date", "exact_quote"],
                },
            },
            "gaps": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["findings", "gaps"],
    },
)
log("Scout findings count:", len(scout_data.get("findings", [])))

phase("2. Independent Fact-Checking")
verified_data = await agent(
    prompt=(
        f"Kiểm chứng ĐỘC LẬP các phát hiện sau cho chủ đề: {topic}\n\n"
        f"Dữ liệu từ Scout:\n{scout_data}\n\n"
        f"Xác minh lại link sống (HTTP 200), đối chiếu chéo mâu thuẫn, kiểm tra câu trích nguyên văn <= 25 từ "
        f"và gắn nhãn độ tin cậy (VERIFIED / AI_ANALYSIS / UNVERIFIED) cho từng luận điểm."
    ),
    type_name="web-fact-checker",
    role="Independent Web Fact-Checker",
    schema={
        "type": "object",
        "properties": {
            "verified_items": {"type": "array", "items": {"type": "object"}},
            "rejected_items": {"type": "array", "items": {"type": "object"}},
            "overall_grade": {"type": "string"},
        },
        "required": ["verified_items", "rejected_items", "overall_grade"],
    },
)
log("Fact-checker grade:", verified_data.get("overall_grade"))

phase("3. 3-Tier Synthesis Report")
final_report = await agent(
    prompt=(
        f"Biên tập báo cáo hoàn chỉnh chuẩn 3 tầng cho chủ đề: {topic}\n"
        f"- Dữ liệu đã kiểm chứng: {verified_data}\n"
        f"- File xuất (nếu có): {output_path}\n\n"
        f"Tầng 1: Nội dung sạch 100% không chèn URL/nhãn vào giữa câu.\n"
        f"Tầng 2: Tài liệu tham khảo ngắn gọn cuối bài.\n"
        f"Tầng 3: Bảng đối chiếu kiểm chứng 6 cột riêng cho người dùng."
    ),
    type_name="web-synthesis-editor",
    role="Web Synthesis Editor",
    schema={"type": "string"},
)

{"grade": verified_data.get("overall_grade"), "report": final_report}
