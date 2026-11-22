---
name: wordpress-flatsome-designer
description: "WordPress Flatsome 3.x & UX Builder: 100% quản trị động cấm code cứng, chia cột Desktop/Mobile, lọc thu gọn, icon SVG, Chatbot/Ship & SEO 100đ."
group: "Marketing, Web & SEO"
---

# WordPress Flatsome Designer & Developer Skill (Master Overview V4.2)

<!-- JAVIS_TRIGGER_ARCHIVE_START -->
## Khi nào dùng (Triggers & Ngữ cảnh kích hoạt đầy đủ)

> Thiết kế, xây dựng, nâng cấp và kiểm toán website WordPress sử dụng theme Flatsome 3.x, UX Builder, Customizer và Native WordPress CMS theo chuẩn thực chiến **Tưới Nông Nghiệp (`V3.7.6`)**, **InfoAsia (`V3.5 Native CMS / V19`)**, **GolfViet (`V2.5.2`)**, **HelenaVan** và **BYD**. Bắt buộc **100% Quản trị động trong WP-Admin / UX Builder / Customizer — Cấm Code Cứng (`Zero Unjustified Hardcoding`)**: người dùng tự **Thêm – Xóa – Sửa – Cập nhật (`CRUD`)**, **kéo thả đổi vị trí**, **đổi màu sắc (`colorpicker`)**, **chia cột**, **chỉnh layout riêng trên Máy tính / Tablet / Điện thoại (`responsive => true`)**, quản trị **Native WP CMS & Đa ngôn ngữ** (`Appearance → Menus` chọn kiểu/số cột Mega Menu 1–4 cột + đồng bộ Mobile Drawer, `Customize` Logo/Banner/Header/Footer 2–5 cột, `Widgets` đa ngôn ngữ, trang `Ngôn ngữ` CRUD), và nếu dự án có ngoại lệ bắt buộc dùng code thì phải **giải thích rõ lý do + Bảng Giải Trình Ngoại Lệ 5 Cột + hướng dẫn sửa an toàn**. Thiết kế **View nhìn rộng thoáng, không quá gần, trực quan** (`1220px–1280px`), **Khung Bộ lọc thông minh có thể thu gọn (`Collapsible Smart Filter`)**, **Mega Menu có Ảnh Thumbnail hoặc Icon SVG đẹp**, **100% thông tin dạng liệt kê gắn Icon SVG inline đẹp** (cấm chấm tròn thô/emoji UI), tích hợp **Chatbot AI + Nút nổi Zalo + Form tư vấn CRM**, **Mua hàng / Thanh toán COD & VietQR / Tính phí ship GHN Live API** (nếu có Shop), đạt chuẩn **PageSpeed 100/100 trên cả Máy tính & Điện thoại** (`MU-Plugin Instant Cache < 85ms`, `WP Rocket 2026 Pro v3.23.3.3` chống lỗi `.html_gzip`, `CLS = 0`, `0KB` admin leak) và **Yoast SEO Full 2026 (`v28.5 / v28.7`)** + 6 lớp Schema JSON-LD + `hreflang` + `/llms.txt` + 100 Điểm QA Checklist.
> TRIGGERS: "flatsome", "ux builder", "wordpress flatsome", "thiet ke web wordpress", "thiết kế web wordpress", "cấm code cứng wordpress", "quản trị động wp-admin", "chia cot desktop mobile ux builder icon svg", "chia cột desktop mobile ux builder", "icon svg ux builder", "wordpress flatsome zero hardcoding responsive", "native wp cms da ngon ngu", "mega menu anh icon svg", "bo loc thu gon collapsible filter", "danh sach liet ke co icon svg", "view nhin rong thoang truc quan", "chatbot ai zalo form crm wordpress", "pagespeed 100 desktop mobile wordpress", "web thương mại dịch vụ", "web bán hàng có giỏ hàng", "mua nhanh 1 chạm", "xem nhanh sản phẩm", "tính phí ship ghn", "vietqr woocommerce", "hover thông số kỹ thuật", "yoast seo 2026", "wp rocket 2026", "landing page chạy ads".
<!-- JAVIS_TRIGGER_ARCHIVE_END -->

- **Nguồn gốc / Kho Hạ Tầng Chuẩn:** `E:\DIEN APP\THIET KE WEB WORDPRESS AI` (`MASTER_PROMPT_FLATSOME_SEO.md` `V4.2`, `wordpress-latest.zip`, `flatsome-core`, `flatsome-child` V4, `Plugin\WP Rocket 2026 Pro`, `Plugin\Yoast SEO Full bộ Mới nhất 2026`, `Plugin\chowordpress-duplicator-pro`).

---

## 0. Bảng Điều Phối Tài Liệu Chuyên Sâu (`references/`) & Kho Plugin Chuẩn 2026

| Hạng Mục Thực Thi | Tệp Tham Chiếu Chi Tiết | Nội Dung Cốt Lõi |
| :--- | :--- | :--- |
| **1. Playbook & 75 Tiêu Chí QA Web Thương Mại Dịch Vụ – B2B (Không Giỏ Hàng)** | [`references/01-b2b-service-leadgen-crm-speed-seo-qa-playbook.md`](./references/01-b2b-service-leadgen-crm-speed-seo-qa-playbook.md) | Kiến trúc No-Cart Service Website, chia ô cân đối chiều cao (`Equal-Height Grid`), 7 chốt chặn UI/UX Mobile & Desktop, cấu hình WP Rocket + khóa chống lỗi download `.html_gzip` LiteSpeed, SEO/GEO (`llms.txt`) & Mini-CRM (`/crm/`). |
| **2. Đại Từ Điển 120+ Tiêu Chí QA Web B2B Có Trang Sản Phẩm Trưng Bày (Catalog Showcase)** | [`references/02-b2b-catalog-showcase-crm-chatbot-qa-master.md`](./references/02-b2b-catalog-showcase-crm-chatbot-qa-master.md) | Kiến trúc 6 lớp cho Website có trang Sản phẩm/Danh mục trưng bày nhưng không bán lẻ trực tiếp: Báo giá nhanh `0ms` (`Zero-AJAX`), Tìm kiếm chính xác 3 tầng trọng số, Bộ lọc không điểm chết, Chatbot 3 tầng & Web CRM. |
| **3. Master Blueprint & 80 Tiêu Chí QA Web Bán Hàng Có Giỏ Hàng, Báo Giá VIP & CRM (`v2.5.2`)** | [`references/02-ecommerce-shop-cart-service-crm-qa-checklist.md`](./references/02-ecommerce-shop-cart-service-crm-qa-checklist.md) | Kiến trúc Hybrid Catalog (Hàng có giá + Hàng báo giá VIP `0₫` + Gói dịch vụ đặt lịch), Smart Filter (`URL-as-State` & `$wp_the_query`), 1-Click Quick-Buy Modal, Checkout rút gọn VN, 6 lớp Schema JSON-LD, Chatbot AI (`sessionStorage`) & CRM Realtime. |
| **4. Kiến Trúc Trường Nhập Video Sản Phẩm, Nút Play Trên Card & Popup Xem Nhanh Có Video** | [`references/03-product-video-field-quickview-video-popup.md`](./references/03-product-video-field-quickview-video-popup.md) | Kiến trúc 4 tầng: Trường nhập `_product_video_url` trong WooCommerce + bóc tách `youtube_id` (Watch/Shorts/`youtu.be`), Nút Play (`▶`) trên Card nếu có video, Popup Xem Nhanh 2 cột phát trực tiếp video kèm thanh chuyển đổi `[▶ VIDEO]` ↔ `[Ảnh]`. |
| **5. Cẩm Nang Tổng Hợp Thực Chiến `V4.2 Master Playbook` (Đồng Bộ 100% `MASTER_PROMPT_FLATSOME_SEO.md`)** | [`references/04-master-playbook-tuoinongnghiep-infoasia-v4.md`](./references/04-master-playbook-tuoinongnghiep-infoasia-v4.md) | 24 Sai sót chí mạng, Thiết luật 100% Quản trị động & Cấm Code Cứng (CRUD, vị trí, màu sắc, chia cột, layout Desktop/Mobile, Native WP CMS InfoAsia V3.5, Bảng Giải Trình Ngoại Lệ 5 cột), View rộng thoáng trực quan, Bộ lọc thu gọn, Mega Menu & Danh sách Icon SVG, Chatbot AI/Zalo/Form/Ship GHN, PageSpeed 100/100 & Yoast SEO 2026 + 100 Điểm QA Checklist. |

### Kho Hạ Tầng & Plugin Chuẩn Mới Nhất 2026 (`E:\DIEN APP\THIET KE WEB WORDPRESS AI`)
- **Core & Theme:** `wordpress-latest.zip` • Theme cha `flatsome-core\flatsome` (giữ nguyên bản 100%) • Theme con `flatsome-child`.
- **Tăng tốc & Cache:** `Plugin\WP Rocket 2026 Pro-20261117T043444Z-1-001\wp-rocket.zip` (**WP Rocket `v3.23.3.3`**) + MU-Plugin `agro-instant-page-cache.php`.
- **Trọn bộ 6 Gói Yoast SEO Full 2026 (`Plugin\Yoast SEO Full bộ Mới nhất 2026\`):** `wordpress-seo.zip` (Core `v28.5`), `chowordpress-wordpress-seo-premium.zip` (Premium `v28.7`), `wpseo-woocommerce-16.9.zip`, `wordpress-seo-local-15.9.zip`, `wpseo-video-15.3.zip`, `wpseo-news-13.3.zip`.
- **Sao lưu & Di chuyển:** `Plugin\chowordpress-duplicator-pro.zip` (**Duplicator Pro**).

---

## 1. 24 Sai Sót Chí Mạng Cần Tránh Tuyệt Đối Khi Thiết Kế (`Post-Mortem & Anti-Patterns`)

| STT | Nhóm Lỗi | ❌ Sai Sót Thường Gặp (CẤM LÀM) | ✅ Giải Pháp Chuẩn Hóa Bắt Buộc (PHẢI LÀM) |
| :-: | :--- | :--- | :--- |
| **01** | **UX Builder** | Để Trang chủ có `menu_order = 0`, bị đẩy sang Trang 2 trong `Pages`. | Đặt **`menu_order = -100`**, `edit_page_per_page = 50`, gắn thanh nút mở nhanh UX Builder trên `Pages` & `#wpadminbar`. |
| **02** | **UX Builder** | Bật defer JS / WP Rocket DelayJS trong iframe UX Builder (`?uxb_iframe=1`). | Kiểm tra `is_ux_builder_request()`: khi `true`, **tắt 100%** defer JS, DelayJS, dequeue và HTML buffer rewrite. |
| **03** | **Cấm Code Cứng** | Khóa cứng HTML/Header/Footer/Nút nổi/Chatbot/màu `#HEX`/số cột/số phần tử (`slide1..6`) trong PHP khiến Admin không tự sửa được. | **100% thành phần Frontend phải quản trị được trong WP-Admin / UX Builder / Customizer:** dùng `Container + Child Item` (CRUD & kéo thả), `colorpicker`, `responsive => true` (Desktop/Tablet/Mobile). Ngoại lệ bắt buộc dùng code → lập **Bảng Giải Trình 5 Cột**. |
| **04** | **UX Builder** | Dán HTML nhiều dòng hoặc comment `<!-- ... -->` vào `post_content` bị `wpautop` chèn `<p></p>` hở trắng. | Cấm đặt comment HTML giữa shortcode; đóng gói Shortcode PHP sạch + CSS `p:empty { display: none !important; }`. |
| **05** | **Lưới SP** | Chia lưới sản phẩm 5 cột trên khung `1220px` làm thẻ sản phẩm quá nhỏ. | Container rộng **`1220px–1280px`**, lưới **4 cột/hàng (`303px/card`)**, 2 hàng = 8 SP (`+8`), ảnh `.box-image` cao **`186px`**. |
| **06** | **Header & Menu** | Thu nhỏ Header/Logo quá đà làm pill active dính mép thanh menu & Breadcrumb dính sát đáy. | Giữ Logo `275×68px` (`#masthead min-height: 82px`), Menu `48px` (`13.8px`, `margin: 4px 0`), cách Breadcrumb `18px`. |
| **07** | **Hover Thông Số** | Hover SP hiện ô tĩnh chung chung hoặc nền đặc che kín hình SP bên dưới. | Bóc từ `post_excerpt` thành danh sách **icon `✔`**, nền trong suốt nhẹ `rgba(224, 238, 174, 0.72)` + `backdrop-filter: none`. |
| **08** | **Nút Video Card** | Nút Play Video (`▶`) bị lệch và che chữ khi hover bảng thông số. | Lúc hover tự thu gọn `32×32px` và neo góc dưới phải (`bottom: 6px; right: 6px; z-index: 25`), ẩn tạm nhãn `"X tùy chọn"`. |
| **09** | **Quick-View** | Quên `flex-shrink: 0` trên `#gv-qb-intro-box` làm Flexbox ép dẹp khung mô tả còn `18px`. | `.gv-qb-body { display: block !important; overflow-y: auto !important; }` & `#gv-qb-intro-box { flex-shrink: 0 !important; min-height: 104px; max-height: 156px; }`. |
| **10** | **Ảnh PDP** | Ép `display: flex !important` lên `.woocommerce-product-gallery__image` làm vỡ Flickity. | Giữ `display: block !important` trên gallery; định kích thước trực tiếp trên `img` (`height: 360px; max-width: 420px; object-fit: contain`). |
| **11** | **Nút Không Đều** | 2 nút cạnh nhau ở chân khối danh mục khác chiều cao/padding. | Khóa cùng `height: 44px !important; display: inline-flex; align-items: center; justify-content: center; padding: 0 24px`. |
| **12** | **Mega Menu Laptop** | Mega Menu quá cao hoặc rớt cột trên màn hình Laptop `1200px–1280px`. | Khóa Mega Menu gọn (`1–4` cột tùy chọn trong `Appearance → Menus`, `max-width: 1120px`, cao `<= 240px`) + cầu nối hover `::before`. |
| **13** | **Skip to content** | Quên CSS `.screen-reader-text` khi tối ưu inline CSS làm hiện chữ `"Skip to content"` trên Mobile. | Luôn nhúng `.screen-reader-text,a.skip-link.screen-reader-text{clip-path:inset(50%);width:1px;height:1px;position:absolute;overflow:hidden}` ngay đầu CSS inline. |
| **14** | **Lỗi tải `download`** | WP Rocket bật `.html_gzip` rewrite trên OpenLiteSpeed gây tải file `download` trắng. | Thêm `add_filter('rocket_force_gzip_htaccess_rules', '__return_false', 99)` + tự cắt khối rewrite `.html_gzip` trong `.htaccess`. |
| **15** | **Mất Admin Bar** | Full-Page Cache trả HTML tĩnh làm mất `#wpadminbar` của Admin đang đăng nhập. | Dùng kiến trúc **`HIT-SPLICED`** ghép động mảnh `_adminbar_default.html` trong `< 15ms`. |
| **16** | **Mobile iOS Zoom** | `<input>/<select>` `font-size < 16px` làm Safari zoom giật khung; `<select>` đè mũi tên. | Ở `@media (max-width: 849px)`: `input, select, textarea { font-size: 16px !important; }` & `select { padding-right: 32px !important; }`. |
| **17** | **Nút Nổi Đè Nút** | Cụm nút nổi Zalo/Chatbot đè Sticky Add-to-Cart Mobile hoặc nút gửi trong Popup. | Nâng lên `bottom: 78px !important` khi có Sticky Bar Mobile; tự ẩn (`opacity: 0; pointer-events: none`) khi mở Popup/Chat. |
| **18** | **Dính Chữ Heading** | Thiếu khoảng trắng trước/sau `<span>` trong `<h1>/<h2>` làm Google đọc dính chữ. | Luôn đặt khoảng trắng tường minh bên ngoài `<span>` hoặc lọc regex tách từ. |
| **19** | **Trùng Meta Yoast** | Vừa bật Yoast SEO vừa tự `echo` thẻ meta description & Schema trong Child Theme. | Dùng các filter `wpseo_title / wpseo_metadesc / wpseo_canonical / wpseo_robots` & `wpseo_json_ld_output => __return_false` (đạt `title=1 | desc=1 | canonical=1`). |
| **20** | **Lộ Staging / 404** | Quên `noindex` trên `demo.*` hoặc bỏ quên Sitemap cũ gây lỗi `404`. | Tự động `noindex, nofollow` trên `demo.*`/`staging.*`/`localhost` và mở `index, follow` trên domain chính; 301 Redirect đủ `0` lỗi `404`. |
| **21** | **Khóa Chết Layout** | Chỉ thiết kế tĩnh Desktop, không mở chỉnh số cột/layout riêng cho Điện thoại & Tablet. | Bắt buộc bật `'responsive' => true` (`columns`, `columns__md`, `columns__sm`, `mobile_layout`, `mobile_order`, `visibility`) trong Admin/UX Builder. |
| **22** | **Hardcode Đa Ngôn Ngữ & `&#038;`** | Cài Polylang/WPML nặng làm gãy URL Unicode `_ia_exact_path` hoặc hardcode Menu/Footer đa ngôn ngữ trong PHP; lỗi `&#038;` ở `nav_menu_description`. | Dùng **Native WP CMS & Multilang (InfoAsia V3.5)**: `wp_nav_menu` + `wp_nav_menu_item_custom_fields` + Custom Mega Walker + decode `nav_menu_description` priority `99` + `Customize` + `Widgets` + trang `Ngôn ngữ`. |
| **23** | **View Chật & Bộ Lọc Cố Định** | View quá gần chật chội, hoặc thanh Bộ lọc cố định chiếm kín màn hình Laptop/Mobile không thu gọn được. | **View nhìn rộng thoáng trực quan** (`1220–1280px`, khoảng thở hài hòa). **Khung Bộ lọc (`Smart Filter`) bắt buộc có nút Thu gọn / Mở rộng** trên cả Desktop & Mobile + chip đang chọn + nút Xóa lọc 1 chạm. |
| **24** | **Mega Menu Trơn & List Chấm Thô** | Mega Menu không có ảnh/icon; danh sách liệt kê dùng chấm tròn đen thô (`•`) hoặc emoji chắp vá. | **Mega Menu bắt buộc có Ảnh Thumbnail hoặc Icon SVG sắc nét**; **100% thông tin dạng liệt kê ngoài giao diện phải gắn Icon SVG inline đẹp** đồng bộ màu thương hiệu (chọn đổi được trong Admin). |

---

## 2. Thiết Luật 100% Quản Trị Động, Chia Cột Desktop / Mobile UX Builder & Icon SVG (`V4.2`)

### 2.1. Quy Tắc Bắt Buộc Khi Thiết Kế Mọi Thành Phần Giao Diện (0% Hardcode)
1. **CRUD, Vị Trí, Màu Sắc, Icon SVG & Layout Đa Thiết Bị:** Mọi khối giao diện đều phải cho phép người dùng **Thêm – Xóa – Sửa – Cập nhật – Nhân bản – Kéo thả đổi vị trí** trong `WP-Admin / UX Builder / Customizer` (kiến trúc `Container + Child Item`), có đầy đủ **5 nhóm `options`**: `(1) Nội dung & Media`, `(2) Vị trí & Kiểu bố cục`, `(3) Màu sắc (`colorpicker` + biến CSS) & Khoảng cách`, `(4) Chia cột & Layout riêng Desktop / Tablet / Mobile (`responsive => true`, `mobile_layout`, `visibility`)`, `(5) Nguồn dữ liệu động, chọn Icon SVG & Ngôn ngữ`.
2. **Native WordPress CMS (Và Tùy Chọn Đa Ngôn Ngữ Khi Dự Án Yêu Cầu `>= 2` Ngôn Ngữ):** Mặc định **1 ngôn ngữ** theo yêu cầu từng dự án (luôn hỏi người dùng ở Bước 1 — **không bắt buộc đa ngôn ngữ**): quản lý Menu & Mega Menu (`1–4` cột + Ảnh/Icon SVG) tại `Appearance → Menus` (tự đồng bộ Mobile Drawer) và Logo/Banner/Header/Số cột Footer (`2–5` cột) tại `Appearance → Customize`. **Chỉ khi dự án yêu cầu `>= 2` ngôn ngữ** mới kích hoạt thêm bộ lọc Widget đa ngôn ngữ, trang `Ngôn ngữ` CRUD & Ma trận Bản dịch gốc WP (không cần cài Polylang/WPML nặng).
3. **Ngoại Lệ Bắt Buộc Code Cứng (`Mandatory Exception Protocol`):** Nếu dự án có hạng mục kỹ thuật lõi bắt buộc dùng code (API GHN, VietQR, Webhook CRM, Schema 6 lớp, Instant Cache, Router URL), **tuyệt đối không âm thầm code cứng**: phải tách 100% tham số cấu hình ra `WP-Admin`, giải thích rõ lý do kỹ thuật và bàn giao kèm **Bảng Giải Trình Ngoại Lệ 5 Cột** (`Hạng mục` | `Lý do bắt buộc dùng code` | `Tham số đã tách ra WP-Admin` | `Đường dẫn sửa cho Admin` | `File & vị trí code cho Kỹ thuật viên`).
4. **Ghim Trang Chủ `#1` & Bảo Vệ Iframe UX Builder:** `menu_order = -100`, `edit_page_per_page = 50`, nút mở nhanh 1-click và `is_ux_builder_request()` tắt tối ưu trong iframe.

### 2.2. Khung Shortcodes Nguyên Bản Của Flatsome UX Builder
```text
[section bg="URL" bg_color="#HEX" bg_overlay="rgba(0,0,0,0.5)" dark="true|false" padding="60px"]
  [row col_bg="" col_bg_radius="" width="full-width|custom" v_align="top|middle|bottom|equal-height"]
    [col span="3" span__md="6" span__sm="12" align="left|center|right"]
      [ux_banner height="550px" height__sm="400px" bg="URL" bg_overlay="rgba(0,0,0,0.4)"]
        [text_box width="60" width__sm="90" position_x="50" position_y="50" align="center"]
          <h1 class="uppercase">TIÊU ĐỀ HERO</h1>
          [button text="KHÁM PHÁ NGAY" color="primary" size="large" radius="99" link="#"]
        [/text_box]
      [/ux_banner]
    [/col]
  [/row]
[/section]
```

---

> 📖 **Chi tiết đầy đủ (View nhìn rộng thoáng, Bộ lọc thu gọn, Chatbot AI/Zalo/Form/Ship, Tốc độ `100/100`, SEO 2026 & QA E2E):** Xem [DETAIL.md](./references/DETAIL.md) và toàn văn `V4.2` tại [04-master-playbook-tuoinongnghiep-infoasia-v4.md](./references/04-master-playbook-tuoinongnghiep-infoasia-v4.md).
