"""
Workflow 5 Pha — Nhà Máy Sản Xuất YouTube Đa Ngách (`team-youtube-factory`).
Tự động điều phối dây chuyền khép kín cho MỌI ngách/kênh tại `E:\\DIEN APP\\Xây Kênh Youtube\\`:
  Phase 1 (niche_brief) : yt-niche-radar đọc số liệu thật Tim Ngach / channel_config.json & chốt đề tài
  Phase 2 (content)     : yt-content-writer viết 0 Noi dung video/ + 5 srt/ (chuẩn 8s/cảnh)
  Phase 3 (prompts)     : yt-prompt-director viết cuốn chiếu B2/B3/B5/B9/B8 (utf-8-sig)
  Phase 4 (pre_qa)      : yt-production-qa kiểm định Pre-Render (CSV=SRT, 8s/cảnh, YPP) + 1 vòng Auto-Retry
  Phase 5 (render+qa)   : yt-omniflash-renderer chạy OmniFlash (.venv 3.12) -> yt-production-qa kiểm ffprobe + soi ảnh PNG

Chạy bằng `run_workflow` với Args:
  {
    "channel_dir": "E:\\DIEN APP\\Xây Kênh Youtube\\01_Ngach_Khao_Co_Va_Huyen_Thoai_US\\Before Us Decoded",
    "video_slug": "06_Ten_Video_Moi",
    "topic": "Chủ đề hoặc yêu cầu cụ thể",
    "mode": "full_video" | "niche_research" | "content_prompt_only" | "render_only"
  }
"""

from pathlib import Path

channel_dir = args.get("channel_dir", "")
video_slug = args.get("video_slug", "")
topic = args.get("topic", "")
mode = args.get("mode", "full_video")

if not topic:
    raise ValueError("Bắt buộc truyền args['topic'] (chủ đề video hoặc câu hỏi tìm ngách).")

if mode == "niche_research":
    phase("1. Quét & Kiểm Chứng Ngách (yt-niche-radar)")
    res = await agent(
        type="yt-niche-radar",
        role="YouTube Niche Radar (Team 12 LEADER)",
        prompt=(
            f"Yêu cầu nghiên cứu / tư vấn ngách: {topic}\n"
            "Bắt buộc đọc JSON thật trong E:\\DIEN APP\\Xây Kênh Youtube\\Tim Ngach\\WebApp\\database\\ "
            "hoặc cd vào E:\\DIEN APP\\Xây Kênh Youtube\\Tim Ngach\\WebApp rồi chạy ..\\agent_cli.py bằng Python313, đối chiếu "
            "TAI_LIEU_TONG_HOP_XAY_KENH_YOUTUBE_NGUOI_MOI_A_Z_2026.md và YPP-Policy-Inauthentic-Content.md. "
            "Tuyệt đối không bịa số liệu."
        ),
    )
    result(res)
else:
    if not channel_dir or not video_slug:
        raise ValueError("Chế độ sản xuất video bắt buộc có args['channel_dir'] và args['video_slug'].")

    video_dir = str(Path(channel_dir) / "src" / "Video" / video_slug)

    if mode in ("full_video", "content_prompt_only"):
        phase("1. Khóa Đề Tài & Chuẩn Kênh (yt-niche-radar)")
        brief = await agent(
            type="yt-niche-radar",
            role="YouTube Strategist (Team 12 LEADER)",
            prompt=(
                f"Đọc {channel_dir}\\channel_config.json và hồ sơ ngách liên quan.\n"
                f"Khóa góc khai thác, từ khóa Cấp 1 (0 trùng lặp kênh anh em) và mục tiêu số cảnh/thời lượng "
                f"(lệch >= 25-45s so với tập trước) cho video `{video_slug}` với chủ đề: {topic}."
            ),
        )

        phase("2. Viết Nội Dung & SRT 8s/Cảnh (yt-content-writer)")
        content_out = await agent(
            type="yt-content-writer",
            role="YouTube Content Writer (Team 12)",
            prompt=(
                f"Kênh: {channel_dir}\nVideo dir: {video_dir}\nBrief từ LEADER:\n{brief}\n\n"
                "Đọc channel_config.json và 1 Viet Content\\MASTER_PROMPT_*.md của kênh. "
                "Xuất trọn bộ 0 Noi dung video/ và 5 srt/ (Phu_De_Anh_TTS.srt & Phu_De_Viet_TTS.srt) chuẩn utf-8-sig, "
                "timestamp 8.0s/cảnh khớp 1:1 số cảnh CSV."
            ),
        )

        phase("3. Đạo Diễn Prompt B2/B3/B5/B9/B8 (yt-prompt-director)")
        prompt_out = await agent(
            type="yt-prompt-director",
            role="YouTube Prompt Director (Team 12)",
            prompt=(
                f"Kênh: {channel_dir}\nVideo dir: {video_dir}\nTóm tắt nội dung:\n{content_out}\n\n"
                "Đọc channel_config.json, 2 Viet Prompt\\HUONG_DAN_VIET_PROMPT_*.md và ảnh phong cách mẫu. "
                "Viết cuốn chiếu 25-30 cảnh/lượt (CẤM gán script lặp!) ra đủ B2_Nhan_Vat.csv, B3_Prompt_Anh_Canh.csv, "
                "B5_Prompt_Video.csv, Buoc_9_SFX_Music.csv và B8 Thumbnail (utf-8-sig)."
            ),
        )

        phase("4. Pre-Render QA Độc Lập + Auto-Retry (yt-production-qa)")
        pre_qa = await agent(
            type="yt-production-qa",
            role="YouTube Pre-Render QA (Team 12 AUDITOR)",
            prompt=(
                f"Chạy Cổng QA 1 (Pre-Render QA) cho {video_dir} thuộc kênh {channel_dir}.\n"
                "Kiểm tra utf-8-sig, đếm khớp số dòng CSV=SRT, kiểm tra duration từng block SRT (~8s, chặn lỗi 1.5s), "
                "kiểm tra flow_config.json & YPP. Trả [STATUS: PASS] hoặc [STATUS: FAIL] + danh sách lỗi chi tiết."
            ),
        )

        if "STATUS: FAIL" in str(pre_qa).upper():
            phase("4b. Auto-Retry 1 Vòng Sửa Lỗi Pre-Render")
            await agent(
                type="yt-prompt-director",
                role="YouTube Prompt/SRT Fixer (Team 12)",
                prompt=f"Sửa triệt để các lỗi Pre-Render QA vừa phát hiện tại {video_dir}:\n{pre_qa}",
            )
            pre_qa = await agent(
                type="yt-production-qa",
                role="YouTube Pre-Render Re-QA (Team 12 AUDITOR)",
                prompt=f"Kiểm định lại Pre-Render QA tại {video_dir} sau khi sửa. Chỉ PASS khi sạch 100% lỗi.",
            )

        if mode == "content_prompt_only":
            result({"brief": brief, "content": content_out, "prompts": prompt_out, "pre_qa": pre_qa})

    if mode in ("full_video", "render_only"):
        phase("5. Render OmniFlash 6 Bước + Post-Render QA Mắt Thật")
        render_out = await agent(
            type="yt-omniflash-renderer",
            role="OmniFlash Renderer (Team 12)",
            prompt=(
                f"Kênh: {channel_dir}\nVideo dir: {video_dir}\n"
                "Chạy dây chuyền OmniFlash 6 bước bằng Tool render edit Video\\.venv\\Scripts\\python.exe "
                "(luôn cd vào thư mục gốc tool): B2 -> B3 -> B4-5 -> B6 TTS -> B9 BGM -> B12 qa_audio_sync_merge.py "
                "ra FINAL/ và GOI_UPLOAD_YOUTUBE_CHUAN_SEO_2026/."
            ),
        )
        post_qa = await agent(
            type="yt-production-qa",
            role="YouTube Post-Render QA (Team 12 AUDITOR)",
            prompt=(
                f"Chạy Cổng QA 2 (Post-Render QA) cho {video_dir}:\n"
                "1) ffprobe kiểm tra FINAL/*.mp4 khớp Voice & SRT.\n"
                "2) Trích 3 frame PNG từ MP4 và mở đọc bằng read_file.\n"
                "3) Mở đọc trực tiếp 6 ảnh Thumbnail bằng read_file kiểm tra lỗi chữ/góc dưới phải.\n"
                "4) Xuất Scorecard iFixAi A-F."
            ),
        )
        result({"render": render_out, "post_qa": post_qa})
