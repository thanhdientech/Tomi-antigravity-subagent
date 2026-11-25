---
name: yt-growth-optimizer
description: "Tối ưu CTR & Retention YouTube cho Team 12: chấm Hook 21 công thức, lint Title+Thumbnail, đọc Retention CSV, tìm Outlier & trích Shorts."
---

# YT GROWTH OPTIMIZER — BỘ CÔNG CỤ ĐỊNH LƯỢNG CTR & RETENTION CHO TEAM 12

> **Upstream Repo URL:** `https://github.com/jakeschincariol/youtube-agent-skill` (License: `MIT`)
> **Phạm vi:** Gắn trực tiếp vào **Team 12 (`team-youtube-factory`)** để chấm điểm định lượng Hook 15s đầu, kiểm lỗi cặp Title + Thumbnail, tìm video Outlier theo median kênh đối thủ, đọc báo cáo Retention CSV hậu đăng, cắt Shorts và kiểm toán kênh 1 lỗi lớn nhất.
> **Ngôn ngữ tối ưu:** Các tool `hookscore.py` & `title.py` tối ưu nhất cho **tiếng Anh (US/Global)**; `retention.py`, `swipe.py`, `chapters.py` dùng cho mọi ngôn ngữ.

## 1. Bộ 6 Công Cụ Python Chạy Offline (Python313 — 0 Dependency)

Đường dẫn thư mục script:
```powershell
$PY = "python"
$YT_OPT = "%USERPROFILE%\.gemini\config\plugins\team-youtube-factory\skills\yt-growth-optimizer\scripts"
```

| Công cụ | Dùng ở Subagent | Lệnh chạy thực tế | Đầu ra cốt lõi |
| :--- | :--- | :--- | :--- |
| **`hookscore.py`** + `hooks.json` (21 công thức) | `yt-content-writer`, `yt-production-qa` | `& $PY "$YT_OPT\hookscore.py" --hook "..."` hoặc `hooks.txt` | Chấm 5 trục (`SPECIFICITY`, `ADDRESS`, `STAKES`, `CURIOSITY`, `BREVITY`, phạt 40% điểm yếu nhất) → chọn Top 2/5 Hook |
| **`title.py`** | `yt-content-writer`, `yt-prompt-director`, `yt-production-qa` | `& $PY "$YT_OPT\title.py" --title "..." --thumb "3 WORDS"` | Chặn cắt chữ Desktop (`60`) & Mobile (`40`), **cấm Thumbnail lặp chữ của Title**, trần `3` từ Thumbnail, trần `2` từ ALL-CAPS, loại từ mơ hồ |
| **`swipe.py`** | `yt-niche-radar` | `& $PY "$YT_OPT\swipe.py" collected.json --min 2.0` | Xếp hạng video đối thủ theo **bội số so với median của CHÍNH kênh đó** (`>= 2.0x`, bỏ kênh `< 4` video) + gán nhãn 21 công thức |
| **`retention.py`** | `yt-production-qa`, `yt-niche-radar` | `& $PY "$YT_OPT\retention.py" retention.csv --duration 600 --transcript Phu_De_Anh_TTS.srt` | Tách 3 lỗi: **Hook Leak (30s đầu < 25% là khỏe)**, **Cliffs (giây thoát + câu đang nói lúc đó)**, **Slide (nhịp chậm đoạn giữa)** |
| **`chapters.py`** | `yt-content-writer`, `yt-production-qa` | `& $PY "$YT_OPT\chapters.py" Phu_De_Anh_TTS.srt --target 7` | Kiểm chuẩn quy tắc YouTube Chapters (bắt đầu `0:00`, `>= 3` chương, mỗi chương `>= 10s`) |
| **`deadair.py`** | `yt-production-qa`, `yt-omniflash-renderer` | `& $PY "$YT_OPT\deadair.py" transcript.srt --floor 0.45` | Tìm khoảng lặng dài (`DEAD`), từ đệm (`FILLER`) & câu nói lặp (`REPEAT`) để xuất danh sách cắt EDL |

## 2. Nguyên Tắc Bắt Buộc Khi Áp Dụng Trong Team 12
1. **Không đoán mò — luôn chạy tool:** Trước khi chốt `Buoc_4_Metadata.txt` & `B8_6_Phien_Ban_Thumbnail_Song_Ngu.csv` cho kênh US, bắt buộc chạy `hookscore.py` (viết 5 Hook → giữ Top 2 điểm cao nhất) và `title.py --title ... --thumb ...` (xác nhận **0 lỗi `duplicate`** giữa Title và chữ trên Thumbnail).
2. **Đọc đúng bản chất điểm số:** `hookscore.py` là bộ lọc phát hiện Hook yếu (`< 55 WEAK` phải viết lại ngay), không phải bảo chứng view; vẫn phải bám sát `channel_config.json` & `MASTER_PROMPT` của đúng kênh.
3. **Audit kênh kết thúc bằng 1 lỗi lớn nhất:** Khi dùng `retention.py` hoặc kiểm toán kênh sau đăng, chỉ chốt **1 điểm sửa quan trọng nhất cho tập kế tiếp** (kèm 3 điểm đang tốt không được phá vỡ) — không liệt kê dàn trải 20 lỗi.
4. **Đọc thêm chi tiết 11 Playbook & mẫu giọng kênh:** Xem `references\yt_growth_playbooks.md` (gồm `/yt-shorts`, `/yt-comment`, `/yt-audit`, `/yt-plan`, `/yt-seo`) và `references\voice_template.md`.
