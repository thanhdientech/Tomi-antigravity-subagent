# wordpress-flatsome-designer — Chi Tiết Đầy Đủ (`V4.2`)

> File này chứa bảng tra cứu, quy chuẩn View nhìn, Bộ lọc thu gọn, Mega Menu/Danh sách Icon SVG, Chatbot AI/Zalo/Form/Ship, Tốc độ `100/100`, SEO 2026 & Checklist nghiệm thu của skill `wordpress-flatsome-designer`.
> Được tách từ `SKILL.md` để tuân thủ giới hạn `24KB` của Antigravity.
> Xem hướng dẫn chính tại [SKILL.md](../SKILL.md) và toàn văn 10 Phần tại [04-master-playbook-tuoinongnghiep-infoasia-v4.md](./04-master-playbook-tuoinongnghiep-infoasia-v4.md).

---

## 3. Quy Chuẩn View Nhìn Rộng Thoáng Trực Quan, Bộ Lọc Thu Gọn, Mega Menu Ảnh/Icon SVG & Danh Sách Có Icon SVG

- **View Nhìn Rộng Thoáng, Không Quá Gần (`Spacious & Visual-First Viewport`):**
  - **Container chính:** **`max-width: 1220px–1280px`** (rộng thoáng, tỷ lệ khoảng trắng hài hòa `48px–64px` giữa các section trên Desktop, `28px–36px` trên Mobile, cỡ chữ thân bài `15px–16px`, `line-height: 1.65`). **Cấm phóng to/nhồi chữ sát mép gây cảm giác quá gần và chật chội.**
  - **Single-Viewport Fit:** Các khối tương tác nhiều Tab (như Copilot `/mesai` hoặc Khối 5 Phân hệ InfoAsia) khóa chiều cao **`450px – 510px`** trên màn hình Laptop `1366×768` để bao quát trọn vẹn trong 1 ánh nhìn trực quan.
- **Header Chính (`#masthead`), Logo & Mega Menu Có Ảnh / Icon SVG Đẹp:**
  - Header cao **`min-height: 82px`**, Logo **`275 × 68 px`** (`object-fit: contain`), ô tìm kiếm và nút Giỏ hàng cao **`42px`**.
  - Thanh Menu Ngang (`#wide-nav`) cao **`min-height: 48px`**, chữ **`13.8px` (`font-weight: 700`)**, `padding: 8px 16px`, `margin: 4px 0`, cách Breadcrumb bên dưới **`18px`**.
  - **Mega Menu (`1–4` cột tùy chọn trong `Appearance → Menus`, `max-width: 1120px`, cao `<= 240px`):** Mỗi mục con **BẮT BUỘC đi kèm Icon SVG đa sắc sắc nét hoặc Ảnh thumbnail đẹp** + mô tả ngắn, có cầu nối hover `::before { height: 14px; top: -14px; }` và đồng bộ 100% sang Mobile Off-Canvas Drawer.
- **100% Thông Tin Liệt Kê Phải Có Icon SVG Đẹp:**
  - Mọi danh sách tính năng, lợi ích, thông số kỹ thuật, chính sách, quy trình, địa chỉ văn phòng đều **bắt buộc gắn Icon SVG inline sắc nét** (dấu tích `✔`, mũi tên, khiên, định vị, hotline, biểu đồ...) đồng bộ màu thương hiệu — **cấm chấm tròn đen thô mặc định (`list-style: disc`) và cấm chắp vá emoji làm icon UI**.
- **Khung Chức Năng Bộ Lọc Có Thể Thu Gọn (`Collapsible Smart Filter`):**
  - Đồng bộ 2 chiều `URL-as-State` + `$GLOBALS['wp_the_query']`, hiện số đếm `(N)`, ẩn lựa chọn `count = 0`.
  - **Bắt buộc có nút Thu gọn / Mở rộng (`▼ Bộ lọc thông minh` / `✕ Thu gọn`)** trên cả Desktop & Mobile (Mobile dùng Drawer/Accordion gọn), hiển thị hàng chip bộ lọc đang chọn + nút Xóa lọc 1 chạm.
- **Lưới Sản Phẩm & Hiệu Ứng Hover Thông Số `✔` Trong Suốt Nhẹ:**
  - **Desktop (`>= 1025px`):** **4 cột/hàng (`25%` = `303px/card`)**, **2 hàng = 8 sản phẩm/khối** (nút Xem thêm tải **`+8`**) • **Tablet (`768px`):** **3 cột** • **Mobile (`390px`):** **2 cột**.
  - Khung ảnh Card (`.box-image`) cao **`186px`** (`img max-height: 170px; max-width: 92%; object-fit: contain`); ảnh trang Chi tiết (`PDP`) giữ `display: block !important` (`420×360px`).
  - Hover bảng `.agro-spec-overlay` hiện 5–6 dòng thông số có icon **`✔`** từ `post_excerpt` trên nền **trong suốt nhẹ `rgba(224, 238, 174, 0.72)`** (`backdrop-filter: none`, `text-shadow` trắng mịn); nút Play Video (`▶`) thu gọn `32×32px` neo góc dưới phải (`bottom: 6px; right: 6px; z-index: 25`). Hai nút chân khối khóa cùng **`height: 44px !important`**.

---

## 4. Kiến Trúc Tốc Độ 6 Lớp (`100/100` PageSpeed Máy Tính & Điện Thoại, `< 85ms` TTFB) & Chuẩn SEO 2026

1. **6 Lớp Tối Ưu PageSpeed `100/100` Desktop & Mobile:**
   - **Lớp 1 (`MU-Plugin Instant Cache`):** `wp-content/mu-plugins/agro-instant-page-cache.php` trả về HTML nén `gzip` trong `< 15ms–85ms`, hỗ trợ **`MU-HIT-SPLICED`** ghép động `#wpadminbar` và giỏ hàng cho Admin.
   - **Lớp 2 (`WP Rocket 2026 Pro v3.23.3.3` trên OpenLiteSpeed):** Khóa `minify_css = 0`, `minify_concatenate_css = 0`, `rocket_force_gzip_htaccess_rules = false` + tự động xóa rewrite `.html_gzip` trong `.htaccess` (chống lỗi tự tải file `download`); bỏ qua `zarsrc, fbclid, gclid, ttclid`.
   - **Lớp 3 (`Inline Font & Minified CSS — 0KB Admin Leak`):** Nhúng `@font-face` (`Be Vietnam Pro`, `font-display: swap`) và CSS đã nén (`*.min.css`) kèm quy tắc ẩn `.screen-reader-text`; tuyệt đối `0KB` CSS/JS quản trị rò rỉ ra Frontend.
   - **Lớp 4 (`Isolated WebP Cache, Zero-CLS & LCP Preload`):** Nén ảnh sang `.webp` trong `wp-content/gv-webp-cache/` (có bản `-640w.webp` cho Điện thoại); **100% `<img>` có `width/height` (`CLS = 0.00`)**; chỉ `fetchpriority="high"` + preload duy nhất 1 ảnh LCP đầu trang.
   - **Lớp 5 (`Conditional Dequeue`):** Gỡ `zxcvbn.min.js`, `contact-form-7`, `photoswipe`, `woo-variation-swatches`, `wc-cart-fragments` ở các trang không dùng; 0 CSS/Font render-blocking từ bên thứ 3.
   - **Lớp 6 (`Instant Prefetch`):** `Speculation Rules API` + `agro-instant-page.js` prefetch trang đích khi rê chuột 65ms.
2. **Đồng Bộ Chuẩn SEO, Đa Ngôn Ngữ `hreflang` & `Yoast SEO Full 2026` (`v28.5 / Premium v28.7`):**
   - Truyền `<title>` (`50–60` ký tự), `<meta name="description">` (`142–158` ký tự), `canonical` sạch và `og:image` qua các filter `wpseo_*` (đạt đúng `title=1 | desc=1 | canonical=1`).
   - Gắn `add_filter('wpseo_json_ld_output', '__return_false', 99)` để xuất duy nhất 1 khối **Schema JSON-LD 6 Lớp `@graph`** (có `inLanguage`; tự ẩn `offers` nếu sản phẩm giá `0₫`).
   - **Ngôn ngữ hiển thị (Tùy theo dự án — hỏi người dùng, mặc định 1 ngôn ngữ, KHÔNG bắt buộc đa ngôn ngữ):** Luôn xuất `<html lang>` đúng ngôn ngữ duy nhất của site; **chỉ khi dự án yêu cầu `>= 2` ngôn ngữ** mới bật cặp thẻ `hreflang` đối xứng + `x-default` (URL đích `HTTP 200`, không chuỗi 2-hop redirect).
   - Phục vụ `/llms.txt` cho AI Search (`GEO`); tự động `noindex, nofollow` trên `demo.*` / `staging.*` và tự mở `index, follow` khi lên domain chính.

---

## 5. Chatbot AI, Nút Zalo, Form CRM, Landing Page CRO & Mua Hàng / Thanh Toán / Ship GHN

1. **Chatbot AI, Nút Nổi Zalo & Form Tư Vấn CRM (Quản Trị Động 100% Trong `WP-Admin`):**
   - **Chatbot AI (`sessionStorage`):** Kịch bản gợi ý câu hỏi nhanh theo ngành hàng, tra cứu sản phẩm/giải pháp, thu Lead & chuyển Zalo — cấu hình bật/tắt, tên bot, màu sắc, kịch bản trong `WP-Admin`.
   - **Nút Nổi Zalo / Hotline / Form:** Quản trị Repeater động (thêm/xóa/đổi màu/đổi icon SVG/sắp xếp); nâng lên `bottom: 78px` trên Mobile có Sticky Bar và tự ẩn khi mở Popup/Chat.
   - **Form Chuyển Đổi (`<= 4` ô):** Đẩy thẳng về `/crm/` + gửi thông báo tức thì Zalo / Telegram / Email SMTP / Google Sheets.
2. **Landing Page Chạy Ads (`Smart Ads Focus Mode`):** Phát hiện `utm_source / gclid / fbclid / ttclid` → bật Header Chốt Đơn Tập Trung + 9 Khối CRO chuẩn UX Builder.
3. **Mua Hàng, Xem Nhanh (`Quick-View`), Thanh Toán COD/VietQR & Tính Phí Ship (`GHN Live API`) — Khi Có Shop:**
   - **Hybrid 3 Luồng:** Hàng có giá (`Mua nhanh`) • Hàng biến thể (`Chọn quy cách` + `N tùy chọn`) • Hàng dự án giá `0₫` (`Liên hệ báo giá kỹ sư 1:1`).
   - **Quick-View 2 Cột:** Cột trái phát Video (`_product_video_url`) ↔ Ảnh; cột phải 3 bước (`#gv-qb-intro-box` cao `156px`, `flex-shrink: 0`) → Chọn biến thể đổi giá tức thì → Mua nhanh 1 chạm.
   - **Checkout Rút Gọn VN + VietQR + Ship GHN:** Giữ Họ tên + SĐT (`type="tel"`) + Tỉnh/Quận/Phường + Địa chỉ; hỗ trợ **COD + VietQR tự động**; tự chọn kho gần nhất gọi **API GHN** tính cước thực tế + bảng giá dự phòng 63 tỉnh + **Freeship tự động** theo ngưỡng cấu hình trong WP-Admin.

---

## 6. Quy Trình Kiểm Toán Tự Động E2E Trước Khi Bàn Giao (`Exit Code 0 & Grade A`)

Trước khi báo cáo hoàn thành bất kỳ yêu cầu giao diện hay dự án mới nào, AI Agent **BẮT BUỘC**:
1. **Kiểm toán Cấm Code Cứng & Quản Trị Động:** Xác nhận mọi thành phần hiển thị ngoài Frontend đều chỉnh sửa được trong `WP-Admin / UX Builder / Customizer` (CRUD, vị trí, màu sắc, chia cột, layout Desktop/Tablet/Mobile, Icon SVG, ngôn ngữ); nếu có ngoại lệ bắt buộc code cứng phải bàn giao kèm **Bảng Giải Trình Ngoại Lệ 5 Cột** + hướng dẫn sửa an toàn.
2. **Kiểm toán Trực Quan Bằng Mắt Thật (`Verify-Loop`):** Mở trình duyệt thật (Playwright / Headless Chrome) kiểm thử cả Desktop (`1440×900`) và Mobile (`375×812` / `390×844`) — gồm Trang chủ, Mega Menu, Bộ lọc thu gọn/mở rộng, Chatbot AI, Nút Zalo, Form, WP-Admin — chụp ảnh màn hình và mở đọc lại bằng `read_file` để sửa sạch mọi lỗi lệch khung, tràn ngang (`0px`), đè nút, thiếu icon.
3. **Kiểm toán Code, Tốc Độ & SEO Độc Lập:** Chạy `php -l` (`0` lỗi, `0` BOM), `audit_ui_ux_cro.py` (`P0 = 0`, `0` ảnh thiếu `width/height`, `0KB` admin leak), kiểm tra HTTP Headers (`HTTP 200`, `title=1 | desc=1 | canonical=1`, `hreflang`) và chạy `ifixai-agent-auditor/cli.py` đạt **`Exit code 0` & `Grade A`**.
