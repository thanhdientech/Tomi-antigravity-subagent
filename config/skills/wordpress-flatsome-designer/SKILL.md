---
name: wordpress-flatsome-designer
description: "Thiết kế web WordPress Flatsome 3.x, Shop bán hàng, Giỏ hàng, Dịch vụ, Báo giá VIP, CRM, Tốc độ, SEO & 80 QA Checklist."
group: "Marketing, Web & SEO"
---

# WordPress Flatsome Designer & Developer Skill (Master Overview V4.0)

<!-- JAVIS_TRIGGER_ARCHIVE_START -->
## Khi nào dùng (Triggers & Ngữ cảnh kích hoạt đầy đủ)

> Thiết kế, xây dựng, nâng cấp và kiểm toán website WordPress sử dụng theme Flatsome 3.x và UX Builder theo chuẩn thực chiến **Tưới Nông Nghiệp (`V3.7.6`)**, **InfoAsia (`V19`)**, **GolfViet (`V2.5.2`)**, **HelenaVan** và **BYD**. Hỗ trợ tạo cấu trúc Shortcodes UX Builder 100% có `options` cho người dùng tự sửa (`add_ux_builder_shortcode`), ghim Trang chủ lên vị trí `#1` (`menu_order = -100`), bảo vệ iframe UX Builder (`is_ux_builder_request()`), tỷ lệ View nhìn chuẩn Shopee/Pro-Shop (`Container 1220px`, `Logo 275×68px`, `Menu 48px` cách Breadcrumb `18px`, `Lưới 4 cột/hàng = 303px/card`, `Khung ảnh 186px`, `Ảnh trang chi tiết 420×360px`), hiệu ứng Hover hiện thông số kỹ thuật dấu tích `✔` từ `post_excerpt` trên nền trong suốt nhẹ (`rgba(224, 238, 174, 0.72)`) thấy rõ hình sản phẩm bên dưới, nút Play Video (`▶`) tự neo góc dưới phải khi hover, Popup Xem Nhanh 2 cột phát Video + 3 bước Mua Nhanh (`Quick-View / Quick-Buy`), Checkout rút gọn Việt Nam tích hợp tính phí ship tự động **Giao Hàng Nhanh (`GHN Live API` đa kho + Freeship)**, Landing Page chạy Ads 9 khối + `Smart Ads Focus Mode`, kiến trúc Tốc độ 6 Lớp (`MU-Plugin Instant Cache < 85ms` + `WP Rocket 2026 Pro v3.23.3.3` chống lỗi `.html_gzip` download trên OpenLiteSpeed + chống lỗi `"Skip to content"`), đồng bộ trọn bộ **Yoast SEO Full 2026 (`v28.5 / Premium v28.7`)** + 6 lớp Schema JSON-LD `@graph` + `/llms.txt` + khóa `noindex` tự động trên `demo.*` và 100 Điểm QA Checklist trước khi bàn giao.
> TRIGGERS: "flatsome", "ux builder", "wordpress flatsome", "thiet ke web wordpress", "thiết kế web wordpress", "web thương mại dịch vụ", "web bán hàng có giỏ hàng", "web có shop có giá", "web tư vấn b2b", "qa checklist web bán hàng", "bộ lọc thông minh woocommerce", "mua nhanh 1 chạm", "xem nhanh sản phẩm", "quick view", "quick buy", "tính phí ship ghn", "hover thông số kỹ thuật", "yoast seo 2026", "wp rocket 2026", "chống lỗi html_gzip wp rocket", "video sản phẩm", "landing page chạy ads", "smart ads focus mode".
<!-- JAVIS_TRIGGER_ARCHIVE_END -->

- **Nguồn gốc / Kho Hạ Tầng Chuẩn:** `E:\DIEN APP\THIET KE WEB WORDPRESS AI` (`MASTER_PROMPT_FLATSOME_SEO.md`, `wordpress-latest.zip`, `flatsome-core`, `flatsome-child` V4.0, `Plugin\WP Rocket 2026 Pro`, `Plugin\Yoast SEO Full bộ Mới nhất 2026`, `Plugin\chowordpress-duplicator-pro`).

---

## 0. Bảng Điều Phối Tài Liệu Chuyên Sâu (`references/`) & Kho Plugin Chuẩn 2026

| Hạng Mục Thực Thi | Tệp Tham Chiếu Chi Tiết | Nội Dung Cốt Lõi |
| :--- | :--- | :--- |
| **1. Playbook & 75 Tiêu Chí QA Web Thương Mại Dịch Vụ – B2B (Không Giỏ Hàng)** | [`references/01-b2b-service-leadgen-crm-speed-seo-qa-playbook.md`](./references/01-b2b-service-leadgen-crm-speed-seo-qa-playbook.md) | Kiến trúc No-Cart Service Website, chia ô cân đối chiều cao (`Equal-Height Grid`), 7 chốt chặn UI/UX Mobile & Desktop, cấu hình WP Rocket + khóa chống lỗi download `.html_gzip` LiteSpeed, SEO/GEO (`llms.txt`) & Mini-CRM (`/crm/`). |
| **2. Đại Từ Điển 120+ Tiêu Chí QA Web B2B Có Trang Sản Phẩm Trưng Bày (Catalog Showcase)** | [`references/02-b2b-catalog-showcase-crm-chatbot-qa-master.md`](./references/02-b2b-catalog-showcase-crm-chatbot-qa-master.md) | Kiến trúc 6 lớp cho Website có trang Sản phẩm/Danh mục trưng bày nhưng không bán lẻ trực tiếp: Báo giá nhanh `0ms` (`Zero-AJAX`), Tìm kiếm chính xác 3 tầng trọng số, Bộ lọc không điểm chết, Chatbot 3 tầng & Web CRM. |
| **3. Master Blueprint & 80 Tiêu Chí QA Web Bán Hàng Có Giỏ Hàng, Báo Giá VIP & CRM (`v2.5.2`)** | [`references/02-ecommerce-shop-cart-service-crm-qa-checklist.md`](./references/02-ecommerce-shop-cart-service-crm-qa-checklist.md) | Kiến trúc Hybrid Catalog (Hàng có giá + Hàng báo giá VIP `0₫` + Gói dịch vụ đặt lịch), Smart Filter (`URL-as-State` & `$wp_the_query`), 1-Click Quick-Buy Modal, Checkout rút gọn VN, 6 lớp Schema JSON-LD, Chatbot AI (`sessionStorage`) & CRM Realtime. |
| **4. Kiến Trúc Trường Nhập Video Sản Phẩm, Nút Play Trên Card & Popup Xem Nhanh Có Video** | [`references/03-product-video-field-quickview-video-popup.md`](./references/03-product-video-field-quickview-video-popup.md) | Kiến trúc 4 tầng: Trường nhập `_product_video_url` trong WooCommerce + bóc tách `youtube_id` (Watch/Shorts/`youtu.be`), Nút Play (`▶`) trên Card nếu có video, Popup Xem Nhanh 2 cột phát trực tiếp video kèm thanh chuyển đổi `[▶ VIDEO]` ↔ `[Ảnh]`. |
| **5. Cẩm Nang Tổng Hợp Thực Chiến `Tưới Nông Nghiệp V3.7.6` & `InfoAsia V19` (`V4.0 Master Playbook`)** | [`references/04-master-playbook-tuoinongnghiep-infoasia-v4.md`](./references/04-master-playbook-tuoinongnghiep-infoasia-v4.md) | 20 Sai sót chí mạng cần tránh, Chuẩn UX Builder 100% Option (`menu_order = -100`, `is_ux_builder_request()`), Tỷ lệ View nhìn (`1220px`, 4 cột/hàng, ảnh `186px`, Hover `✔` trong suốt nhẹ `0.72`), Tốc độ `99–100` (`MU-Plugin HIT-SPLICED < 85ms` + `WP Rocket 3.23.3.3`), Yoast SEO Full 2026 (`v28.5/v28.7`), Landing Page CRO 9 khối, Quick-View/Quick-Buy, Tính phí ship GHN đa kho & 100 Điểm QA Checklist. |

### Kho Hạ Tầng & Plugin Chuẩn Mới Nhất 2026 (`E:\DIEN APP\THIET KE WEB WORDPRESS AI`)
- **Core & Theme:** `wordpress-latest.zip` • Theme cha `flatsome-core\flatsome` (giữ nguyên bản 100%) • Theme con `flatsome-child` (đã tích hợp sẵn 7 module V4.0).
- **Tăng tốc & Cache:** `Plugin\WP Rocket 2026 Pro-20261117T043444Z-1-001\wp-rocket.zip` (**WP Rocket `v3.23.3.3`**) + MU-Plugin `agro-instant-page-cache.php`.
- **Trọn bộ 6 Gói Yoast SEO Full 2026 (`Plugin\Yoast SEO Full bộ Mới nhất 2026\`):**
  1. `wordpress-seo.zip` (**Yoast SEO Core `v28.5`** — kích hoạt đầu tiên)
  2. `chowordpress-wordpress-seo-premium.zip` (**Yoast SEO Premium `v28.7`**)
  3. `wpseo-woocommerce-16.9.zip` (**Yoast SEO: WooCommerce `v16.9`**)
  4. `wordpress-seo-local-15.9.zip` (**Yoast SEO: Local `v15.9`**)
  5. `wpseo-video-15.3.zip` (**Yoast SEO: Video `v15.3`**)
  6. `wpseo-news-13.3.zip` (**Yoast SEO: News `v13.3`**)
- **Sao lưu & Di chuyển:** `Plugin\chowordpress-duplicator-pro.zip` (**Duplicator Pro**).

---

## 1. 20 Sai Sót Chí Mạng Cần Tránh Tuyệt Đối Khi Thiết Kế (`Post-Mortem & Anti-Patterns`)

| STT | Nhóm Lỗi | ❌ Sai Sót Thường Gặp (CẤM LÀM) | ✅ Giải Pháp Chuẩn Hóa Bắt Buộc (PHẢI LÀM) |
| :-: | :--- | :--- | :--- |
| **01** | **UX Builder** | Để Trang chủ (`Front Page`) có `menu_order = 0` và tên bắt đầu bằng chữ `T`, khiến Trang chủ bị đẩy sang **Trang 2 (vị trí #21)** trong `wp-admin/edit.php?post_type=page` làm người dùng không tìm thấy chỗ sửa. | Luôn đặt **`menu_order = -100`** cho Trang chủ, tăng `edit_page_per_page = 50`, gắn **Thanh nút mở nhanh UX Builder** ngay đầu trang `Pages` và trên thanh Admin Bar (`🎨 Sửa Trang Chủ (UX Builder)`). |
| **02** | **UX Builder** | Bật `defer_non_critical_scripts` (defer `jquery-core`, `flatsome-js`) và `WP Rocket DelayJS` cả khi đang mở iframe của UX Builder (`?uxb_iframe=1`), làm đơ trình kéo thả. | Tạo hàm `is_ux_builder_request()` kiểm tra `$_GET['uxb_iframe']`, `$_GET['app'] === 'uxbuilder'`, `ux_builder_is_iframe()`. Khi `true`, **tắt 100%** defer JS, DelayJS, dequeue CSS/JS và HTML buffer rewrite. |
| **03** | **UX Builder** | Viết shortcode giao diện cứng trong PHP mà không khai báo `options` trong `add_ux_builder_shortcode()`, khiến nhân sự Marketing bấm vào khối không sửa được chữ/ảnh. | **100% Custom Shortcode** phải đăng ký vào hook `ux_builder_setup` kèm đầy đủ `options` (Tiêu đề, Mô tả, Ảnh Media Library ID + URL, Nút CTA, Màu nền, Padding, Ẩn/Hiện). |
| **04** | **UX Builder** | Dán HTML nhiều dòng hoặc comment `<!-- ... -->` trực tiếp vào `post_content`, bị bộ lọc `wpautop` tự chèn `<p></p>` và `<br>` gây hở trắng từng mảng lớn. | Tuyệt đối không đặt comment HTML giữa các shortcode. Đóng gói giao diện phức tạp thành Shortcode PHP sạch và thêm CSS `p:empty { display: none !important; }`. |
| **05** | **Tỷ lệ View & Lưới SP** | Chia lưới sản phẩm **5 cột/hàng** trên khung `1220px` khiến thẻ sản phẩm chỉ rộng `~230px`, hình ảnh sản phẩm bị thu nhỏ lí nhí khó nhìn. | Trên container chuẩn **`1220px`**, lưới sản phẩm chuẩn đẹp nhất là **1 hàng 4 sản phẩm (`25%` = `~303px/card`)**, hiển thị **2 hàng = 8 sản phẩm/khối** (bấm Xem thêm tải `+8` sản phẩm), khung ảnh `.box-image` cao **`186px`** (`img max-height: 170px`). |
| **06** | **Header & Menu** | Thu nhỏ Header/Logo/Menu quá đà khiến Logo bé tí và viền vàng mục menu đang chọn dính sát mép dưới thanh xanh, chữ Breadcrumb dính sát đáy menu. | Giữ **Logo `275×68px`** (`#masthead min-height: 82px`), thanh Menu xanh **`#wide-nav min-height: 48px`** (`font-size: 13.8px`, `padding: 8px 16px`, `margin: 4px 0` để pill active có khoảng thở trên/dưới), và cách đáy menu **`18px`** trước khi vào Breadcrumb. |
| **07** | **Hover Thông Số SP** | Khi hover vào sản phẩm chỉ hiện 4 ô tĩnh chung chung hoặc để nền xanh đặc `opacity: 0.97` + `blur(4px)` che kín mít hình sản phẩm bên dưới. | Bóc tách trực tiếp từng dòng từ `post_excerpt` (`$product->get_short_description()`, fallback sang thuộc tính WooCommerce) hiển thị thành danh sách dấu tích **`✔`**. Nền `.agro-spec-overlay` dùng **trong suốt nhẹ `rgba(224, 238, 174, 0.72)`** + `backdrop-filter: none` + `text-shadow` trắng mịn để thấy rõ ảnh SP bên dưới. |
| **08** | **Nút Video Trên Card** | Đặt nút Play Video (`▶`) ở giữa ảnh nhưng khi hover hiện bảng thông số `✔` lại dịch nút lên `top: 24%`, làm nút bị lệch và che khuất chữ thông số kỹ thuật. | Lúc bình thường nút Play Video nằm giữa ảnh (`44×44px`). **Khi hover vào card**, tự động thu gọn nút Play Video (`32×32px`) và **neo xuống góc dưới phải (`bottom: 6px; right: 6px; z-index: 25`)**, đồng thời ẩn tạm nhãn `"X tùy chọn"`. |
| **09** | **Popup Quick-View** | Đặt `.gv-qb-body { display: flex; flex-direction: column }` mà quên `flex-shrink: 0` trên khung mô tả `#gv-qb-intro-box`, khiến Flexbox ép dẹp khung `1. Giới thiệu sản phẩm` còn `18px` mất hết chữ. | Đặt `.gv-qb-body { display: block !important; overflow-y: auto !important; }` và khóa `#gv-qb-intro-box { flex-shrink: 0 !important; min-height: 104px !important; max-height: 156px !important; overflow-y: auto !important; }`. |
| **10** | **Ảnh Trang Chi Tiết (PDP)** | Ép `display: flex !important` lên `.woocommerce-product-gallery__image` hoặc `.slide`, làm hỏng thuật toán tính chiều cao của Flickity Slider khiến ảnh chính trên trang Chi tiết sản phẩm bị co nhỏ hoặc biến mất. | Trên `body.single-product`, giữ `.woocommerce-product-gallery__image { display: block !important; }` và định kích thước trực tiếp trên thẻ `img` (`height: 360px !important; max-width: 420px !important; object-fit: contain !important; margin: 0 auto !important;`). |
| **11** | **Nút Bấm Không Đều** | Đặt 2 nút cạnh nhau ở chân khối danh mục (*"Xem thêm +8 sản phẩm"* và *"Xem toàn bộ 37 sản phẩm"*) nhưng khác `padding` / `line-height` làm 1 nút to 1 nút nhỏ. | Hai nút đứng cạnh nhau bắt buộc khóa cùng **`height: 44px !important`**, `display: inline-flex !important`, `align-items: center !important`, `justify-content: center !important`, `padding: 0 24px !important`, `font-size: 13.5px !important`. |
| **12** | **Mega Menu Laptop** | Trên màn hình Laptop Windows bật Scale `125%–150%` (viewport rộng `1200px–1280px`), Mega Menu quá cao hoặc tự rớt từ 4 cột xuống 2 cột che kín hết Hero Banner. | Khóa Mega Menu **4 cột ngang siêu gọn (`max-width: 1120px`, chiều cao `~170px–240px`)** xuyên suốt từ `1025px` trở lên, kèm cầu nối hover vô hình `::before { height: 14px; top: -14px; }`. |
| **13** | **Lỗi "Skip to content"** | Khi gỡ/dequeue `flatsome-main.css` hoặc tối ưu CSS inline để lấy 100 điểm PageSpeed, quên định nghĩa class `.screen-reader-text`, làm hiện chữ `"Skip to content"` và viền trắng `8px` ở đầu trang Mobile. | Luôn nhúng ngay đầu CSS inline: `html,body{margin:0;padding:0} .screen-reader-text,a.skip-link.screen-reader-text{clip-path:inset(50%);width:1px;height:1px;position:absolute;overflow:hidden;margin:-1px;padding:0;border:0}`. |
| **14** | **Lỗi Tự Tải File `download`** | Bật WP Rocket trên máy chủ **OpenLiteSpeed (`lshttpd`)**, `.htaccess` rewrite sang file `.html_gzip` khiến OpenLiteSpeed trả về `Content-Type: application/octet-stream` làm trình duyệt tự tải file `download` trắng! | Bắt buộc thêm `add_filter('rocket_force_gzip_htaccess_rules', '__return_false', 99)` và hàm `self_heal_ols_htaccess_gzip_rewrite()` tự động cắt bỏ khối rewrite `.html_gzip` trong `.htaccess`. |
| **15** | **Cache Làm Mất Admin Bar** | Khi dùng Full-Page Cache cho cả người dùng đã đăng nhập, nếu phục vụ nguyên xi file HTML của khách vãng lai sẽ làm biến mất thanh `#wpadminbar` màu đen của Admin. | Dùng kiến trúc **`HIT-SPLICED`**: Lưu riêng mảnh `_adminbar_default.html` (có sẵn nút `🎨 Sửa Trang Chủ (UX Builder)` & `+ Đăng SP Nhanh`) và ghép động vào HTML cache trong `< 15ms` khi phát hiện cookie `wordpress_logged_in_*`. |
| **16** | **Mobile iOS Auto-Zoom & Đè Chữ Select** | Để `<input>`, `<select>` trên Mobile có `font-size: 13px–14px` (khiến iPhone Safari tự động zoom giật khung hình khi bấm vào) và thiếu `padding-right` trên `<select>` làm chữ đè lên mũi tên dropdown. | Ở `@media (max-width: 849px)`, ép toàn bộ `input, select, textarea { font-size: 16px !important; }` và `select { padding-right: 32px !important; text-overflow: ellipsis !important; }`. |
| **17** | **Nút Nổi Đè Nút Mua Hàng** | Để cụm nút nổi Zalo/Hotline/Chatbot (`bottom: 20px; right: 20px`) đè trực tiếp lên thanh `Sticky Add-to-Cart Bar` ở đáy màn hình Mobile hoặc đè lên nút gửi trong Popup Mua Nhanh. | Khi ở trang sản phẩm có Sticky Bottom Bar trên Mobile, nâng cụm nút nổi lên `bottom: 78px !important`; khi mở Popup Mua Nhanh hoặc mở khung Chat (`body.gv-quickbuy-open`, `body.gv-chat-is-open`), tự động ẩn cụm nút nổi (`opacity: 0; pointer-events: none`). |
| **18** | **Dính Chữ Trong Thẻ Heading** | Viết `<h1>Giải pháp<span>MES AI</span>tự động</h1>` thiếu khoảng trắng trước/sau thẻ `<span>`, làm Google đọc thành `"Giải phápMES AItự động"` và trừ điểm SEO. | Luôn đặt khoảng trắng tường minh bên ngoài thẻ `<span>` hoặc kiểm tra bằng regex `preg_replace('/<\/span>(?=[A-Za-zÀ-ỹ0-9])/u', '</span> ', $html)`. |
| **19** | **Nhân Đôi Thẻ Meta Khi Bật Yoast SEO** | Vừa bật plugin **Yoast SEO (`v28.5 / v28.7`)** vừa tự `echo '<meta name="description">'` trong Child Theme, khiến `<head>` bị trùng 2 thẻ `description` và 2 khối Schema. | Kiểm tra `if (defined('WPSEO_VERSION'))`: Truyền dữ liệu chuẩn qua các filter `wpseo_title`, `wpseo_metadesc`, `wpseo_canonical`, `wpseo_robots` và nhường Yoast in thẻ meta (chỉ giữ lại 1 hệ thống Schema JSON-LD 6 lớp duy nhất). |
| **20** | **Lộ Link Staging & Mất Link SEO Cũ** | Quên bật `noindex` trên tên miền thử nghiệm (`demo.*`), hoặc khi làm lại web cũ không quét Sitemap cũ gây hàng loạt lỗi `404`. | Tự động bật `noindex, nofollow` khi `HTTP_HOST` là `demo.*`/`staging.*`/`localhost` và tự động mở `index, follow` khi lên tên miền chính; quét 100% XML Sitemap cũ và lập bảng `301 Redirect` đạt `0` lỗi `404`. |

---

## 2. Quy Chuẩn UX Builder 100% Option & Từ Điển Shortcodes Nòng Cốt (`Flatsome 3.20.x`)

### 2.1. Quy Tắc Đăng Ký Custom UX Builder Shortcode Đủ Option Cho Người Dùng Tự Sửa
- **Không khóa cứng nội dung trong PHP:** Mọi tiêu đề (`eyebrow`, `title`, `highlight`), mô tả (`lead`, `desc`), con số KPI, ảnh (`type => 'image'` Media Library ID + URL), ID danh mục (`parent_cat`), danh sách Sub-Tab (`tabs`), số sản phẩm (`limit` mặc định `8`) và nút CTA (`cta_text`, `cta_url`) đều phải khai báo trong `options` của `add_ux_builder_shortcode()`.
- **Ghim Trang Chủ lên vị trí #1 (`menu_order = -100`):** Đặt `menu_order = -100` cho trang `page_on_front`, tăng `edit_page_per_page = 50`, gắn thanh nút mở nhanh **`🎨 Sửa Trang Chủ Bằng UX Builder`** ngay đầu màn hình `edit-page` và trên thanh `#wpadminbar`.
- **Bảo vệ Iframe UX Builder (`is_ux_builder_request()`):** Tự động tắt `defer_non_critical_scripts`, `DelayJS`, `conditional_dequeue_assets` và `start_full_document_buffer` khi mở iframe UX Builder (`?uxb_iframe=1` hoặc `app=uxbuilder`).

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
- **Các Shortcode thường dùng:** `[ux_slider]`, `[ux_image]`, `[ux_video]`, `[title]`, `[featured_box]`, `[accordion]` + `[accordion_item]`, `[gap]`, `[button]`, `[ux_products columns="4" columns__sm="2"]`, `[blog_posts]`.
- **Các Action Hooks trọng yếu của Flatsome Child Theme:** `flatsome_before_header`, `flatsome_after_header` (chèn thanh tìm kiếm Mobile & thanh lọc ngang Điện Máy Xanh), `flatsome_woocommerce_shop_loop_images` (chèn bảng thông số Hover `✔` & nút Play Video), `flatsome_footer` (chèn Footer Pro-Shop toàn cục).

---

---

> 📖 **Chi tiết đầy đủ:** Xem [DETAIL.md](./references/DETAIL.md) — chứa bảng tra cứu, checklist và ví dụ mở rộng.
