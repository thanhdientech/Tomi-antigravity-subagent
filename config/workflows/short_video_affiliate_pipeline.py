"""
Workflow 4 Pha — Nhà Máy Video Ngắn 9:16 Xây Kênh Facebook Reels & Tiếp Thị Liên Kết Shopee (`team-short-video-affiliate`).
Khép kín quy trình chuẩn 13 Kênh Mẫu (`Nghien_Cuu_Kenh_Moi_Huong_Dan`) & `Shopee_KOL_Studio_Tool` (:8600):
  Phase 1 (scout)       : short-channel-product-scout đối chiếu kênh mẫu (01..13) + quét SP Shopee & thông số NSX thật
  Phase 2 (storyboard)  : short-script-storyboarder viết kịch bản 6 phong cách KOL + phân cảnh Step_{k-1}->Step_k + Safe-Zone
  Phase 3 (render+qa1)  : short-kol-studio-producer dựng ảnh Step_01..0N -> short-video-qa-auditor soi Cổng 1 (chống nhảy bước)
                          -> Render chuyển động thật Veo/Muse/Three.js + cắt 0.0s->3.4s + xuất kép
  Phase 4 (post_qa)     : short-video-qa-auditor chạy ffprobe (1080x1920, 30fps) + soi qa_end_step_*.jpg -> Scorecard A-F

Chạy bằng `run_workflow` với Args:
  {
    "topic_or_product": "Từ khóa/link Shopee hoặc chủ đề video ngắn cần làm",
    "channel_archetype": "(Tùy chọn) 01..13 — mặc định để short-channel-product-scout tự đối chiếu mẫu khớp nhất",
    "platform": "facebook_reels" | "shopee_video" | "tiktok_shop" | "youtube_shorts",
    "mode": "full_short_video" | "channel_research" | "product_story_only"
  }
"""

topic_or_product = args.get("topic_or_product", "")
archetype = args.get("channel_archetype", "auto")
platform = args.get("platform", "facebook_reels")
mode = args.get("mode", "full_short_video")

if not topic_or_product:
    raise ValueError("Bắt buộc truyền args['topic_or_product'] (chủ đề kênh ngắn hoặc link/từ khóa sản phẩm Shopee).")

phase("1. Đối Chiếu 13 Kênh Mẫu & Săn Sản Phẩm Thật (short-channel-product-scout)")
brief = await agent(
    type="short-channel-product-scout",
    role="Short Video & Shopee Scout (Team 14 LEADER)",
    prompt=(
        f"Chủ đề / Sản phẩm: {topic_or_product}\nKênh mẫu yêu cầu: {archetype}\nNền tảng đăng: {platform}\n"
        "1) Đọc 00_MASTER_SOP_TOAN_BO_CAC_KENH_CHO_AGENT.md và mở đối chiếu đúng thư mục mẫu (01..13) trong "
        "Nghien_Cuu_Kenh_Moi_Huong_Dan (SOP, PREVIEW_*.jpg, script Python mẫu, Voice ID).\n"
        "2) Nếu là video Affiliate Shopee: kiểm tra :8600 / shopee_story_cli.py, bóc thông số NSX thật (0 bịa đặt).\n"
        "3) Xuất Brief chi tiết bàn giao cho Biên kịch."
    ),
)

if mode == "channel_research":
    result(brief)
else:
    phase("2. Biên Kịch KOL & Phân Cảnh Chống Nhảy Bước (short-script-storyboarder)")
    storyboard = await agent(
        type="short-script-storyboarder",
        role="Short Video KOL Scriptwriter (Team 14)",
        prompt=(
            f"Nền tảng: {platform}\nBrief từ LEADER:\n{brief}\n\n"
            "Sáng tác kịch bản KOL đời thường tự nhiên + phân cảnh khóa Con người cầm/dùng sản phẩm thật (UID01+UID02), "
            "tuân thủ Kim Chỉ Nam 1 & 2 (Step_{k-1}->Step_k chống nhảy bước, Tool-Tip Contact Lock), "
            "phụ đề 1-2 dòng trong Safe-Zone Reels (y=148..1244, x=64..896), encoding utf-8-sig. "
            "Nếu nền tảng là tiktok_shop thì bỏ chữ 'Shopee'."
        ),
    )

    if mode == "product_story_only":
        result({"brief": brief, "storyboard": storyboard})
    else:
        phase("3. Render Ảnh Step_01..0N -> Pre-Render QA Soi Ảnh -> Render MP4 9:16 (.venv :8600)")
        img_stage = await agent(
            type="short-kol-studio-producer",
            role="Shopee KOL Studio Image Producer (Team 14)",
            prompt=(
                f"Kịch bản & phân cảnh:\n{storyboard}\n\n"
                "Dùng .venv của Shopee_KOL_Studio_Tool tạo chuỗi ảnh Step_01..0N theo cơ chế Image-to-Image "
                "kế thừa Step_{k-1}. Dừng sau khi xong ảnh để QA Cổng 1 soi trước khi chạy Veo."
            ),
        )

        qa1 = await agent(
            type="short-video-qa-auditor",
            role="Pre-Render Image Logic QA (Team 14 AUDITOR)",
            prompt=(
                f"Chạy Cổng QA 1 (mở đọc trực tiếp từng ảnh bằng read_file) cho bộ ảnh:\n{img_stage}\n"
                "Bắt lỗi nhảy bước, sai Tool-Tip Contact, mất người cầm SP, chữ Hán rác DIY, ngược trục Dual-PiP. "
                "Trả [STATUS: PASS] hoặc [STATUS: FAIL] + danh sách ảnh lỗi."
            ),
        )

        if "STATUS: FAIL" in str(qa1).upper():
            phase("3b. Auto-Retry 1 Vòng Sửa Ảnh Lỗi Logic")
            img_stage = await agent(
                type="short-kol-studio-producer",
                role="Shopee KOL Studio Image Fixer (Team 14)",
                prompt=f"Tạo lại riêng các ảnh bị lỗi theo báo cáo QA Cổng 1:\n{qa1}",
            )

        render_out = await agent(
            type="short-kol-studio-producer",
            role="Shopee KOL Studio Video Renderer (Team 14)",
            prompt=(
                f"Ảnh đã qua kiểm định:\n{img_stage}\n"
                "Render 100% cảnh quay chuyển động thật (1080x1920, 30fps — CẤM zoompan!) qua OmniEngine "
                "(Veo 3.1 / Muse — Stage B5 First Frame Only) hoặc Three.js WebGL (Kênh 11/13); "
                "cắt Khung Vàng 0.0s->3.4s, trộn giọng ai33.pro + Suno/SFX, xuất ảnh cuối cảnh qa_end_step_*.jpg "
                "và xuất kép Có Giọng + ASMR/Clean nếu kênh yêu cầu."
            ),
        )

        phase("4. Post-Render QA (ffprobe + Soi Frame Cuối Cảnh Bằng read_file)")
        qa2 = await agent(
            type="short-video-qa-auditor",
            role="Post-Render MP4 Visual QA (Team 14 AUDITOR)",
            prompt=(
                f"Chạy Cổng QA 2 cho video thành phẩm:\n{render_out}\n"
                "1) Chạy ffprobe xác nhận 1080x1920, 30fps, đủ audio+video.\n"
                "2) Mở đọc trực tiếp ảnh qa_end_step_*.jpg bằng read_file kiểm tra 0% biến hình & phụ đề Safe-Zone Reels.\n"
                "3) Xuất Scorecard iFixAi A-F."
            ),
        )
        result({"brief": brief, "render": render_out, "qa_pre": qa1, "qa_post": qa2})
