# wordpress-flatsome-designer — Chi Tiết Đầy Đủ

> File này chứa bảng tra cứu, checklist và ví dụ mở rộng của skill `wordpress-flatsome-designer`.
> Được tách từ SKILL.md để tuân thủ giới hạn 24KB của Antigravity.
> Xem hướng dẫn chính tại [SKILL.md](../SKILL.md)

---

## 3. Quy Chuẩn View Nhìn, Tỷ Lệ Vàng Đa Khung Hình & Hiệu Ứng Hover (`Viewport Harmony`)

- **Chiều rộng Container chính:** **`max-width: 1220px`** (chuẩn Shopee Mall / Pro-Shop).
- **Header Chính (`#masthead`) & Logo:** Cao **`min-height: 82px`**, Logo **`275 × 68 px`** (`object-fit: contain`), ô tìm kiếm và nút Giỏ hàng cao **`42px`**.
- **Thanh Menu Ngang (`#wide-nav`):** Cao **`min-height: 48px`**, chữ **`13.8px` (`font-weight: 700`)**, mục menu `padding: 8px 16px`, `margin: 4px 0`, cách Breadcrumb bên dưới **`18px`**.
- **Lưới Sản Phẩm (Product Grid):**
  - **Desktop (`>= 1025px`):** **1 hàng 4 sản phẩm (`25%` = `303px/card`)**, hiển thị **2 hàng = 8 sản phẩm/khối** (bấm Xem thêm tải **`+8`**).
  - **Tablet (`768px`):** **3 cột/hàng (`33.33%`)** • **Mobile (`390px`):** **2 cột/hàng (`50%`)**.
  - **Khung ảnh sản phẩm trên Card (`.box-image`):** Cao **`186px`** (`img max-height: 170px; max-width: 92%; object-fit: contain`), nền trắng `#FFFFFF`.
  - **Trang Chi tiết Sản phẩm (`Single Product / PDP`):** Khung ảnh Gallery giữ `display: block !important` (`420×360px`, `object-fit: contain`), cột trái có hộp Thông số vận hành & Cam kết kỹ thuật.
- **Hiệu Ứng Hover Hiện Thông Số Kỹ Thuật (`✔`) Trong Suốt Nhẹ:**
  - Khi rê chuột vào sản phẩm, bảng `.agro-spec-overlay` hiển thị danh sách 5–6 dòng dấu tích **`✔`** bóc tách từ `post_excerpt` (`$product->get_short_description()`, tự động fallback sang thuộc tính thật) trên nền **xanh cốm trong suốt nhẹ `rgba(224, 238, 174, 0.72)`** (`backdrop-filter: none`, chữ `#0F172A` có `text-shadow` trắng mịn) để **vừa đọc rõ thông số vừa nhìn thấy rõ hình ảnh sản phẩm bên dưới**.
  - Khi hover, nút Play Video (`▶`) tự động thu gọn (`32×32px`) và neo xuống góc dưới phải (`bottom: 6px; right: 6px; z-index: 25`), ẩn tạm nhãn `"X tùy chọn"`.
- **Cặp Nút Chân Khối Danh Mục & Khối Tab 1 Màn Hình:**
  - Hai nút `.gv-showcase-loadmore-btn` và `.gv-showcase-more-btn` khóa cùng **`height: 44px !important`**, `min-width: 315px !important`.
  - Các khối tương tác nhiều Tab (như Copilot `/mesai`) khóa chiều cao **`450px – 510px`** gọn trọn trong 1 view nhìn Laptop `1366×768`.

---

## 4. Kiến Trúc Tốc Độ 6 Lớp (`99–100` PageSpeed & `< 85ms` TTFB) & Bộ Yoast SEO Full 2026

1. **6 Lớp Tối Ưu Tốc Độ Không Vỡ Giao Diện:**
   - **Lớp 1 (`MU-Plugin Instant Cache`):** `wp-content/mu-plugins/agro-instant-page-cache.php` trả về HTML nén `gzip` trong `< 15ms–85ms`, hỗ trợ **`MU-HIT-SPLICED`** ghép động `#wpadminbar` và giỏ hàng cho cả Admin đang đăng nhập.
   - **Lớp 2 (`WP Rocket 2026 Pro v3.23.3.3` trên OpenLiteSpeed):** Khóa `minify_css = 0`, `minify_concatenate_css = 0`, `rocket_force_gzip_htaccess_rules = false` + tự động xóa rewrite `.html_gzip` trong `.htaccess` (chống lỗi tự tải file `download`); bỏ qua `zarsrc, fbclid, gclid, ttclid`.
   - **Lớp 3 (`Inline Font & Child CSS`):** Nhúng `@font-face` (`Be Vietnam Pro`) và `style.css` đã nén vào `<head>` kèm quy tắc ẩn `.screen-reader-text` (chống hiện chữ `"Skip to content"`).
   - **Lớp 4 (`Isolated WebP Cache & LCP Preload`):** Tự động nén ảnh sang `.webp` trong `wp-content/gv-webp-cache/` (có bản `-640w.webp` cho Mobile), chỉ preload duy nhất 1 ảnh LCP đầu trang.
   - **Lớp 5 (`Conditional Dequeue`):** Gỡ `zxcvbn.min.js`, `contact-form-7`, `photoswipe`, `woo-variation-swatches`, `wc-cart-fragments` ở các trang không dùng.
   - **Lớp 6 (`Instant Prefetch`):** `Speculation Rules API` + `agro-instant-page.js` tải ngầm trang sản phẩm ngay khi rê chuột 65ms.
2. **Đồng Bộ Không Trùng Thẻ Với `Yoast SEO Full 2026` (`v28.5 / Premium v28.7`):**
   - Khi `defined('WPSEO_VERSION')` tồn tại, truyền `<title>` (`50–60` ký tự), `<meta name="description">` (`142–158` ký tự), `canonical` sạch và `og:image` qua các filter `wpseo_*` và nhường Yoast in thẻ meta (đạt đúng `title=1 | desc=1 | canonical=1`).
   - Gắn `add_filter('wpseo_json_ld_output', '__return_false', 99)` để xuất duy nhất 1 khối **Schema JSON-LD 6 Lớp `@graph`** của Child Theme (tự ẩn `offers` nếu sản phẩm giá `0₫`).
   - Phục vụ `/llms.txt` cho AI Search (`GEO`); tự động bật `noindex, nofollow` trên `demo.*` / `staging.*` và tự động mở `index, follow` khi lên tên miền chính.

---

## 5. Landing Page Chạy Ads (`9 Khối CRO`), Web Mua Sắm (`Hybrid`), Xem Nhanh, Mua Nhanh & Ship GHN

1. **Landing Page Chạy Ads (`Smart Ads Focus Mode`):** Khi URL có `utm_source / gclid / fbclid / ttclid`, tự động ẩn Mega-Menu nhiều mục, bật Thanh Header Chốt Đơn Tập Trung + 9 Khối CRO chuẩn UX Builder + Form thu Lead `<= 4` ô đẩy thẳng vào `/crm/`.
2. **Hybrid Catalog 3 Luồng:** Sản phẩm đơn giản (`⚡ Mua nhanh`) • Sản phẩm nhiều biến thể (`⚡ Chọn quy cách` + huy hiệu `N tùy chọn`) • Sản phẩm dự án giá `0₫` (`Liên hệ báo giá / Nhận Báo Giá Kỹ Sư 1:1`).
3. **Popup Xem Nhanh (`Quick-View`) & Mua Nhanh 1 Bước (`Quick-Buy`):**
   - Cột trái phát trực tiếp Video thực tế (`_product_video_url`) kèm nút chuyển `[▶ VIDEO]` ↔ `[Ảnh]`.
   - Cột phải gồm 3 bước: `1. Giới thiệu sản phẩm` (`#gv-qb-intro-box` cao `156px`, `flex-shrink: 0`) $\rightarrow$ `2. Chọn quy cách` (đổi giá tức thì) $\rightarrow$ `3. Đặt mua nhanh 1 chạm` (`wc_create_order`).
4. **Checkout Rút Gọn Việt Nam & Tính Phí Ship Tự Động (`GHN Live API`):**
   - Chỉ giữ: **Họ tên + SĐT (`type="tel" inputmode="numeric"`) + Tỉnh/Thành $\rightarrow$ Quận/Huyện $\rightarrow$ Phường/Xã + Địa chỉ chi tiết**.
   - Tự động chọn kho xuất hàng gần nhất (TP.HCM / Đà Lạt / Hà Nội), tính tổng khối lượng giỏ hàng và gọi **API Giao Hàng Nhanh (GHN)** trả về phí ship thực tế + bảng giá dự phòng 63 tỉnh thành + tự động **Miễn phí vận chuyển** khi đạt ngưỡng đơn hàng.

---

## 6. Quy Trình Kiểm Toán Tự Động E2E Trước Khi Bàn Giao (`Exit Code 0 & Grade A`)

Trước khi báo cáo hoàn thành bất kỳ yêu cầu giao diện hay dự án mới nào, AI Agent **BẮT BUỘC**:
1. **Tự chụp ảnh màn hình trình duyệt thật (Headless Edge/Chrome CDP hoặc Playwright)** trên cả Desktop (`1440×900`) và Mobile (`390×844`), mở đọc lại chính ảnh vừa chụp (`read_file`) để tự kiểm tra và sửa sạch mọi lỗi lệch khung, mất chữ, đè nút.
2. Chạy kiểm toán `audit_ui_ux_cro.py` (`0px` tràn ngang, `P0 = 0`), kiểm tra HTTP Headers (`HTTP 200`, `Content-Type: text/html`, `title=1 | desc=1 | canonical=1`) và chạy `ifixai-agent-auditor/cli.py` đạt **`Exit code 0` & `Grade A`**.
