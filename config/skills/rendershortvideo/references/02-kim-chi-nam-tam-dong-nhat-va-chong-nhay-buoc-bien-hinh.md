# 02. Kim Chỉ Nam Toàn Hệ Thống: Tam Đồng Nhất, Chống Nhảy Bước (`Zero Step-Jumping`), Cắt Khung Vàng & Kỹ Thuật Đặc Thù 11 Kênh (`rendershortvideo`)

Chưng cất từ quy chuẩn gốc tại `E:\DIEN APP\Tiep thi lien ke shoppe\Tim repo tim san pham shope lam video\Nghien_Cuu_Kenh_Moi_Huong_Dan\QUY_CHUAN_TAM_DONG_NHAT_VA_LOGIC_VIDEO.md` và `00_MASTER_SOP_TOAN_BO_CAC_KENH_CHO_AGENT.md`.

---

## 1. Ba Định Luật Kim Chỉ Nam Bất Biến (`The 3 Golden Compass Laws`)

### Định Luật 1 — Kế Thừa Trạng Thái Từng Bước (`Cumulative Step-to-Step State Machine — Zero Step-Jumping`)
- Khi video có chuỗi bước tiến triển ($S_1 \rightarrow S_2 \rightarrow \dots \rightarrow S_N$):
  - Ảnh gốc của **Bước $k$ BẮT BUỘC truyền trực tiếp file ảnh của Bước $k-1$ làm tham chiếu (`ReferenceImagePaths = [Step_{k-1}]`)** để giữ nguyên 100% mặt bàn, ánh sáng, đạo cụ và phần việc đã làm xong ở các bước trước.
  - **Mỗi bước chỉ cộng thêm ĐÚNG 1 thao tác vật lý đơn lẻ (`Single Atomic Delta`):** Tuyệt đối cấm nhảy cóc bước hoặc để chi tiết của Bước $k+1$ tự hiện sẵn ở Bước $k$ (ví dụ đang dán áo mưa ở Bước 3 thì vùng dưới áo mưa phải trống 100%, chưa được hiện sẵn mặt hay đôi ủng của Bước 4–5).

### Định Luật 2 — Khóa Điểm Chạm Đầu Dụng Cụ (`Tool-Tip Contact Point Lock`)
- Ở Bước $k$, đầu dụng cụ trên tay nhân vật (ngòi bút vẽ, bút tô màu, con lăn keo, máy bấm hoa văn, tua-vít, khăn lau) **BẮT BUỘC chạm trực tiếp vào đúng chi tiết vừa được thêm ở Bước $k$**.
- Cấm để tay cầm bút đè lên vùng khác trong khi chi tiết mới lại tự mọc ở góc khác.
- **Chốt kiểm tra bằng mắt AI:** Trước khi đẩy bộ ảnh sang `Veo 3.1`, Agent bắt buộc gọi `read_file` soi từng tấm ảnh `Step_01..Step_N` để xác nhận vị trí đầu dụng cụ và tính kế thừa $k-1 \rightarrow k$.

### Định Luật 3 — Cắt Khung Vàng `3.2s – 3.6s` Chống Biến Hình Cuối Clip (`Golden-Window Anti-Morphing Cut`)
- Trong một clip `Veo 3.1` dài `8.0s`, đoạn đầu **`0.0s -> 3.6s`** giữ nguyên 100% hình học vật thể gốc, còn từ `4.0s -> 8.0s` mô hình dễ tự sinh thêm vệt keo lạ hoặc làm biến dạng đạo cụ.
- **Quy chuẩn xử lý bắt buộc:**
  1. Trong Prompt gửi `Veo 3.1`: Chỉ mô tả chuyển động vi mô `1–3 mm` (`"making a tiny 2-millimeter stroke/press, do NOT add or remove any objects, zero morphing"`).
  2. Trong Script FFmpeg: Trích xuất Khung Vàng `0.0s -> 3.4s` và giãn nhịp mượt theo độ dài câu thoại `dur`:
     ```text
     trim=start=0:end=3.4,setpts=(dur/3.4)*PTS,fps=30
     ```
  3. Xuất tự động ảnh frame cuối mỗi cảnh (`qa_end_step_01..08.jpg`) và dùng `read_file` kiểm tra đạt **0% biến hình** trước khi ghép bản cuối.

---

## 2. Hệ Thống Tam Đồng Nhất & Quy Tắc Kỹ Thuật Đặc Thù Cho Từng Nhóm Mẫu

1. **Đồng Nhất Con Người & Khóa Tiền Cảnh (`Spatial Foreground Lock`):**
   - Giữ nguyên mặt, kiểu tóc, trang phục qua ảnh tham chiếu gốc (`UID01`).
   - Khi nhân vật đứng/ngồi cạnh ô tô, đảo bếp hoặc bàn lớn: toàn bộ cơ thể **phải nằm ở TIỀN CẢNH phía gần ống kính (`in the FOREGROUND on the NEAR side facing the camera`)** — cấm để nhân vật bị nắp capo/cột A che khuất mà thò tay xuyên qua.
   - Giữ cổ tay/bàn tay sạch (`Clean Wrist & Hand Rule`), tránh đeo băng cổ tay dày đen khi đan tay trước ngực.
2. **Đồng Nhất Môi Trường & Trục 180 Độ (`Environment & 180-Degree Axis Lock`):**
   - Với **Kênh 08 (`Mẹo Lái Xe Dual-View PiP`)**: Đặt camera góc cao từ **sau đuôi xe nhìn về phía trước (`High-Angle Rear-to-Front Overhead View`)** để bên PHẢI tài xế trùng khớp 100% bên PHẢI màn hình, đồng bộ hướng xoay vô-lăng trong khung PiP tròn.
   - Với **Kênh 09 (`DIY Thủ Công`)**: Loại bỏ 100% đạo cụ có chữ Hán của video nước ngoài, giữ mặt bàn thủ công sạch xuyên suốt Bước 1 $\rightarrow$ Bước 8.
3. **Quy Chuẩn Riêng Cho Kênh 10 (`Học Tiếng Anh Gia Đình 3D Flashcard`):**
   - Khóa nhân vật gia đình 3D Pixar qua `uid01_base_family.jpg` trên toàn bộ các cảnh từ vựng.
   - Giữ nguyên 100% giọng thoại tương tác đa nhân vật gốc từ **Google Flow (`Veo 3.1 Lite`)** (Bố hỏi tiếng Việt $\rightarrow$ Bé đáp từ vựng + câu Q&A chuẩn `en-US`) kết hợp Thẻ HUD Flashcard IPA; phần bài hát ôn tập tạo trực tiếp trên `https://suno.com/create` (cấm dùng `flowmusic.app`); định hướng CTA mua khóa học tới Ba/Mẹ ở bình luận ghim theo chính sách Meta.
4. **Quy Chuẩn Riêng Cho Kênh 11 (`Cờ Vua 3D Kịch Tính Phong Cách Forgiro`):**
   - **Cấm dùng AI sinh video văn bản (Flow/Muse) vẽ bàn cờ** (để tránh ảo giác bàn cờ lệch `7x9` hoặc quân đi sai luật); bắt buộc render bằng Engine **`Three.js WebGL` + `Playwright`** (`assets/chess_reel_3d.html`) khóa chuẩn bàn cờ gỗ lì `8x8` nghiêng `42°`, tách độ cao trục `Y` chống chớp sáng (`Zero Z-Fighting`) và trộn âm thanh 3 luồng (`Voice Tùng Đặng 1.42` + `BGM Giao hưởng 2 tầng 0.38` + `SFX quân cờ gỗ 1.10`, `normalize=0`, `mean_volume ~ -12.4 dB`).
5. **Quy Chuẩn Kỹ Thuật Xuất Xưởng (`Pre-Flight Audit Gate`):**
   - Cấm dùng ảnh tĩnh chạy `zoompan` thay cho video chuyển động thật.
   - Khi dùng FFmpeg `overlay` với ảnh `.png` tĩnh, bắt buộc truyền cờ `-loop 1` trước `-i file.png`.
   - Đầu ra chuẩn `H.264`, `1080x1920` (`9:16`), `30fps`, kiểm tra bằng `ffprobe` đạt `Exit code 0`.
