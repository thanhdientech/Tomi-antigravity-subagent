# Sổ Tay Kinh Nghiệm Dịch Ngược & Bảo Mật (Learned Patterns — Team 10)

1. **Đọc schema MCP lazy trước khi gọi:** Cả `rea` và `craft-anything` đều có nhiều tool lazy-loaded — luôn đọc file schema JSON tương ứng trong `%USERPROFILE%\.gemini\antigravity\mcp\<server>\` trước khi gọi `call_mcp_tool`.
2. **Bảo quản chuỗi bằng chứng (Evidence Bundle):** Ghi lại đầy đủ `evidence` và `unknowns` trước khi chuyển từ giai đoạn phân tích (`rev-binary-analyst`) sang giai đoạn tái lập sạch (`rev-cleanroom-builder`).
3. **Che dấu bí mật trong báo cáo Audit:** Không in nguyên văn secret key/password vào báo cáo markdown; chỉ ghi đường dẫn file, số dòng và mức độ nghiêm trọng.
