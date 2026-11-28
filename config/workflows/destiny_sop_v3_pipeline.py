"""
Workflow 4 Pha — Chiêm Tinh: Tử Vi Đẩu Số, Bát Tự 24 Tiết Khí & Thần Số Học (`team-tu-vi-bat-tu-than-so-hoc`).
Vòng đời khép kín có QA 13 bước độc lập & Auto-Retry 1 vòng:
  Phase 1 (engine) : destiny-chart-engineer kiểm đủ 4 dữ kiện cứng & chạy destiny_pipeline.py -> facts_*.json + HTML
  Phase 2 (analyze): song song destiny-tuvi-battu-master (Tử Vi 12 cung + Bát Tự) & destiny-numerology-advisor (TSH + 10 file SOP V3.0)
  Phase 3 (qa_13)  : destiny-qa-auditor chạy qa_dossier_auditor.py (13 bước) đối chiếu facts_*.json + soi Tinh bàn HTML
  Phase 4 (retry)  : Nếu FAIL -> trả lỗi về chuyên gia sửa 1 vòng rồi tái kiểm toán; PASS -> xuất Scorecard iFixAi A-F

Chạy bằng `run_workflow` với Args:
  {
    "subject_info": "Họ tên, giới tính, ngày sinh Dương lịch, giờ sinh, nơi sinh (hoặc đường dẫn profiles.json)",
    "output_dir": "Đường dẫn thư mục xuất hồ sơ",
    "mode": "quick_reading" | "full_sop_v3" | "family_compatibility",
    "target_year": 2026
  }
"""

subject_info = args.get("subject_info", "")
output_dir = args.get("output_dir", "")
mode = args.get("mode", "full_sop_v3")
target_year = args.get("target_year", 2026)

if not subject_info or not output_dir:
    raise ValueError("Bắt buộc truyền args['subject_info'] và args['output_dir'].")

phase(f"1. Lập Lá Số & Khóa Facts Tất Định ({mode} / {target_year})")
chart_out = await agent(
    type="destiny-chart-engineer",
    role="Destiny Chart Engineer (Team 16 LEADER)",
    prompt=(
        f"Dữ liệu đương số: {subject_info}\nThư mục xuất: {output_dir}\nNăm xem hạn: {target_year}\nChế độ: {mode}\n"
        "1) Kiểm tra đủ 4 dữ kiện cứng (Họ tên, Giới tính, Ngày sinh Dương lịch, Giờ sinh). Nếu thiếu giờ sinh, báo rõ giới hạn.\n"
        "2) Chạy destiny_pipeline.py (Exit code 0) để xuất facts_*.json, 01_Ho_So_Goc_*_TOOL.md và Ban_Do_La_So_*_TOOL.html.\n"
        "3) Trả về đường dẫn chính xác các tệp vừa xuất và Bảng An Sao tường minh."
    ),
)

phase("2. Luận Giải Chuyên Sâu Song Song (Tử Vi – Bát Tự & Thần Số Học SOP V3.0)")
tuvi_task = agent(
    type="destiny-tuvi-battu-master",
    role="Tu Vi & Bat Tu Master (Team 16)",
    prompt=(
        f"Chế độ: {mode} | Năm: {target_year} | Thư mục: {output_dir}\nKết quả từ LEADER:\n{chart_out}\n\n"
        "Đọc facts_*.json và 01_Ho_So_Goc_*_TOOL.md làm Nguồn Sự Thật Duy Nhất. "
        "Tách bạch 3 tầng sao (Tọa Thủ / Hội Chiếu / Giáp Cung), chốt Dụng-Hỷ-Kỵ Thần theo Lệnh Tháng 24 Tiết Khí, "
        "cấm dùng 0%/100%, biên soạn 02_Menh_Thu_Tong_Quan_8_Chuong.md (>=3,000 từ nếu full_sop_v3), "
        "03_Luan_Giai_Tu_Vi_Chi_Tiet_14_Cung.md, 04_Bat_Tu_Chuyen_Sau_Va_Cai_Van.md và 05_Lo_Trinh_Van_Han_Tung_Nam.md."
    ),
)
num_task = agent(
    type="destiny-numerology-advisor",
    role="Numerology & Dossier Advisor (Team 16)",
    prompt=(
        f"Chế độ: {mode} | Năm: {target_year} | Thư mục: {output_dir}\nKết quả từ LEADER:\n{chart_out}\n\n"
        "Đọc facts_*.json làm Nguồn Sự Thật Duy Nhất. "
        "Biên soạn 07_Goc_Nhin_Than_So_Hoc_Chuyen_Sau.md (18 chỉ số Pythagoras + Phillips 3x3 & 8 Mũi tên), "
        "00_HUONG_DAN_DOC_HO_SO.md, 00_TONG_HOP_COT_LOI_VA_LUU_Y_QUAN_TRONG.md và chuyên đề gia đình/hôn phối/7 đại họa nếu yêu cầu."
    ),
)
tuvi_out, num_out = await gather(tuvi_task, num_task)

phase("3. Kiểm Toán QA Độc Lập 13 Bước (destiny-qa-auditor)")
qa_out = await agent(
    type="destiny-qa-auditor",
    role="Destiny QA Auditor (Team 16 AUDITOR)",
    prompt=(
        f"Kiểm toán độc lập 13 bước cho bộ hồ sơ tại {output_dir} (mode={mode}):\n"
        f"- Tử Vi & Bát Tự:\n{tuvi_out}\n- Thần Số Học & Tổng hợp:\n{num_out}\n\n"
        "Chạy qa_dossier_auditor.py (Exit code 0) đối chiếu toàn bộ .md với facts_*.json, kiểm tra Tinh bàn HTML và chấm Scorecard iFixAi A-F. "
        "Nếu có bất kỳ sai lệch nào -> trả STATUS: FAIL kèm danh sách dòng sai chính xác."
    ),
)

if "FAIL" in str(qa_out).upper() and "GRADE: A" not in str(qa_out).upper() and "GRADE: B" not in str(qa_out).upper():
    phase("4. Sửa Lỗi Theo Báo Cáo QA & Tái Kiểm Toán (Auto-Retry 1 Vòng)")
    fix_out = await agent(
        type="destiny-tuvi-battu-master",
        role="Destiny Fixer (Team 16)",
        prompt=f"Sửa triệt để toàn bộ lỗi mà QA Auditor phát hiện tại {output_dir}:\n{qa_out}",
    )
    qa_out = await agent(
        type="destiny-qa-auditor",
        role="Destiny QA Re-Audit (Team 16 AUDITOR)",
        prompt=f"Tái chạy qa_dossier_auditor.py tại {output_dir} sau khi sửa:\n{fix_out}\nChốt Scorecard iFixAi cuối cùng.",
    )

result = {
    "team": "team-tu-vi-bat-tu-than-so-hoc",
    "mode": mode,
    "output_dir": output_dir,
    "qa_verdict": qa_out,
}
