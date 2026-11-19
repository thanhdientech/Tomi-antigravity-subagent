# 👑 MASTER PROMPT & SKILL TOÀN DIỆN (`V4.0`): THIẾT KẾ WEBSITE WORDPRESS FLATSOME 3.X, UX BUILDER 100% OPTION, LANDING PAGE CRO, E-COMMERCE PRO-SHOP, TỐC ĐỘ 99–100 & YOAST SEO 2026

> **HƯỚNG DẪN SỬ DỤNG CHO CHỦ DỰ ÁN:**
> Khi bắt đầu bất kỳ dự án thiết kế mới hoặc nâng cấp website WordPress nào (dù là **Web Doanh Nghiệp B2B / Dịch Vụ / Đa Ngôn Ngữ** hay **Web Bán Hàng Có Giỏ Hàng / Shop Kỹ Thuật / Showroom**), chỉ cần gửi file `@[E:\DIEN APP\THIET KE WEB WORDPRESS AI\MASTER_PROMPT_FLATSOME_SEO.md]` kèm yêu cầu ngành hàng. AI Agent **BẮT BUỘC** tuân thủ nghiêm ngặt 10 Phần Quy Chuẩn dưới đây để đạt chất lượng **"Làm Đúng Ngay Lần Đầu Tiên (`First-Time Right`)"**, không lặp lại bất kỳ sai sót cũ nào.

---

## 🧰 PHẦN 1: BẢN ĐỒ KỸ NĂNG (`SKILL MAPPING`) & KHO HẠ TẦNG GỐC (`E:\DIEN APP\THIET KE WEB WORDPRESS AI`)

### 1.1. Các Agent Skills Bắt Buộc Kích Hoạt Theo Từng Giai Đoạn
1. **Kiến trúc & Phỏng vấn Đặc tả:** `project-blueprint-architect` + `lean-teamwork` (Chốt đặc tả, chia nhỏ từng bước cuốn chiếu, kiểm tra đạt 100% mới qua bước tiếp theo).
2. **Thiết kế & Lập trình Flatsome / UX Builder / WooCommerce:** `wordpress-flatsome-designer` (`%USERPROFILE%\.gemini\config\skills\wordpress-flatsome-designer\SKILL.md` & `references/01..04`).
3. **Thiết kế Landing Page Chuyển Đổi & Copywriting:** `design-landingpage-vip-v2` + `cong-thuc-viet-content-by-noti-v4`.
4. **Kiểm toán Giao diện Đa Khung Hình & Tỷ lệ Chuyển đổi (UI/UX/CRO):** `ui-ux-cro-auditor` (`scripts/audit_ui_ux_cro.py` — tự động chụp ảnh trình duyệt thật kiểm tra Desktop `1440×900`, Laptop `1366×768`, Tablet `768×1024`, Mobile `390×844`).
5. **Kiểm toán SEO Kỹ thuật, Schema JSON-LD & AI Search (GEO):** `claude-seo` (`seo-audit`, `seo-technical`, `seo-schema`, `seo-images`, `seo-local`, `seo-geo`).
6. **Kiểm toán Độc lập 5 Trụ cột Chống Ảo Giác:** `ifixai-agent-auditor` (`python %USERPROFILE%\.gemini\config\skills\ifixai-agent-auditor\cli.py` đạt `Exit code 0` & `Grade A`).

### 1.2. Kho Tài Nguyên & Plugin Chuẩn 2026 Tại `E:\DIEN APP\THIET KE WEB WORDPRESS AI`
Khi khởi tạo dự án mới, luôn lấy trực tiếp từ kho chuẩn đã kiểm định tại `E:\DIEN APP\THIET KE WEB WORDPRESS AI\`:
1. **WordPress Core:** `E:\DIEN APP\THIET KE WEB WORDPRESS AI\wordpress-latest.zip`
2. **Theme Cha (Flatsome 3.x Core):** `E:\DIEN APP\THIET KE WEB WORDPRESS AI\flatsome-core\flatsome` (hoặc `theme\themeforest-4JtEoA1F-flatsome-multipurpose-responsive-woocommerce-theme.zip` — **Tuyệt đối giữ nguyên bản 100%, cấm sửa file trong thư mục theme cha `flatsome`**).
3. **Theme Con (Child Theme Pro V4):** Khởi tạo từ `E:\DIEN APP\THIET KE WEB WORDPRESS AI\flatsome-child` (hoặc `flatsome-child-pro-v4`) chứa toàn bộ `functions.php`, `style.css` và các module trong `inc/`.
4. **Kho Plugin Chuẩn 2026 (`E:\DIEN APP\THIET KE WEB WORDPRESS AI\Plugin\`):**
   - **Tăng tốc & Cache (`WP Rocket 2026 Pro v3.23.3.3`):** `Plugin\WP Rocket 2026 Pro-20261117T043444Z-1-001\wp-rocket.zip` (hoặc `wp-rocket-3.23.3.3.zip`).
   - **Trọn bộ 6 Gói Yoast SEO Full Mới Nhất 2026 (`Plugin\Yoast SEO Full bộ Mới nhất 2026\`):**
     - `wordpress-seo.zip` (**Yoast SEO Core `v28.5`** — luôn kích hoạt trước tiên).
     - `chowordpress-wordpress-seo-premium.zip` (**Yoast SEO Premium `v28.7`** — Quản lý Redirects 301, Multiple Keyphrases, Internal Linking).
     - `wpseo-woocommerce-16.9.zip` (**Yoast SEO: WooCommerce `v16.9`** — Dùng cho web có cửa hàng WooCommerce).
     - `wordpress-seo-local-15.9.zip` (**Yoast SEO: Local `v15.9`** — Tối ưu đa chi nhánh / LocalBusiness / Google Maps).
     - `wpseo-video-15.3.zip` (**Yoast SEO: Video `v15.3`** — Tối ưu Video Sitemap cho sản phẩm/bài viết có gắn Video).
     - `wpseo-news-13.3.zip` (**Yoast SEO: News `v13.3`** — Tối ưu Google News Sitemap cho chuyên mục Tin tức / Tư vấn).
   - **Đóng gói & Di chuyển Website (`Duplicator Pro`):** `Plugin\chowordpress-duplicator-pro.zip`.

---

## 🚀 PHẦN 2: QUY TRÌNH 8 BƯỚC TRIỂN KHAI WEBSITE MỚI & BỘ CÂU HỎI KHẢO SÁT ĐẦU DỰ ÁN (`GRILL-ME`)

### Bước 1 — Thu Thập Thông Tin & Chốt 10 Câu Hỏi Đầu Dự Án (`Specification Lock`)
Trước khi viết code, AI kiểm tra nhanh và hỏi người dùng những thông tin còn thiếu trong 10 điểm sau:
1. **Thông tin thương hiệu:** Tên công ty, Logo (PNG/SVG nền trong suốt), Bảng màu chủ đạo (Primary / Accent), Địa chỉ các chi nhánh/tổng kho, Số Hotline, Zalo, Email.
2. **Làm mới hay Nâng cấp từ web cũ:**
   - Nếu **đã có web cũ / web mẫu**: Quét ngay toàn bộ `sitemap_index.xml` của web cũ để lập danh sách bảo toàn **100% URL SEO cũ (`HTTP 200` hoặc `301 Redirect`)**; hỏi rõ khách muốn giữ nguyên nội dung/tính năng nào của web cũ (ví dụ: kiểu hover hiện thông số `✔`) và nâng cấp phần nào.
3. **Mô hình chuyển đổi chính (chọn 1 trong 3):**
   - *(Mô hình A — B2B / Dịch vụ / Giải pháp không giỏ hàng, như `InfoAsia.vn`):* Tập trung 100% vào Landing Page CRO 9 khối + Smart Ads Focus Mode + Thu Lead tư vấn/đặt lịch Demo về `/crm/`.
   - *(Mô hình B — Bán lẻ E-Commerce thuần túy):* 100% sản phẩm có giá cố định, bấm Mua nhanh / Thêm vào giỏ / Thanh toán COD & VietQR.
   - *(Mô hình C — Hybrid E-Commerce lai, như `Tưới Nông Nghiệp` & `GolfViet`):* Kết hợp đồng thời **(1) Sản phẩm có giá cố định** + **(2) Sản phẩm nhiều biến thể/quy cách** + **(3) Hệ thống/Dự án lớn để giá `0₫` ("Liên hệ báo giá kỹ sư 1:1")**.
4. **Ngôn ngữ hiển thị:** 1 ngôn ngữ (`Tiếng Việt`) hay Đa ngôn ngữ (`VI / EN / KO / ZH-HANS / JA` như InfoAsia).
5. **Tỷ lệ Lưới sản phẩm & Kiểu Hover (nếu có Shop):**
   - Mặc định áp dụng tỷ lệ vàng đã kiểm chứng: **Container rộng `1220px`, 1 hàng 4 sản phẩm (`25%` = `303px/card`), khung ảnh cao `186px`, mỗi khối hiển thị 2 hàng = 8 sản phẩm (nút Xem thêm tải `+8`)**.
   - Mặc định khi Hover vào thẻ sản phẩm: Hiện danh sách thông số kỹ thuật dấu tích **`✔`** lấy từ `post_excerpt` trên **nền màu thương hiệu trong suốt nhẹ (`opacity 0.72`, `backdrop-filter: none`)** để vẫn nhìn thấy rõ hình sản phẩm bên dưới.
6. **Video Sản phẩm:** Có dùng link Video thực tế (`_product_video_url` YouTube/Shorts/MP4) hiện nút Play (`▶`) trên ảnh sản phẩm và phát trong Popup Xem Nhanh không?
7. **Tính phí vận chuyển (Shipping) & Ngưỡng Freeship:** Xuất hàng từ mấy kho (1 kho hay 3 kho TP.HCM – Đà Lạt – Hà Nội)? Kết nối API Giao Hàng Nhanh (`GHN`) tự động theo Tỉnh/Quận/Phường và miễn phí ship cho đơn từ bao nhiêu tiền (vd: `>= 2.000.000₫`)?
8. **Phương thức thanh toán:** COD (Kiểm tra hàng trước khi thanh toán) + Chuyển khoản ngân hàng / Quét mã VietQR tự động điền số tiền & mã đơn hàng.
9. **Kênh nhận thông báo Đơn hàng & Lead:** Lưu vào WooCommerce + `/crm/` kèm bắn thông báo qua Zalo / Telegram / Email SMTP / Google Sheets.
10. **Môi trường chạy thử nghiệm:** Chạy trên Local (`D:\xampp` / पोर्ट riêng) hay đẩy lên Staging (`demo.thanhdientech.com/...`, `demo.infoasia.vn/...` — tự động bật khóa `noindex` bảo vệ SEO tên miền chính).

### Bước 2 $\rightarrow$ Bước 8 — Lộ Trình Thực Thi Cuốn Chiếu Tự Kiểm Chứng
- **Bước 2:** Khởi tạo WordPress + Flatsome Core + Child Theme Pro V4 + Cài đặt bộ Plugin 2026 (`WP Rocket 3.23.3.3` + `Yoast SEO Full 2026`).
- **Bước 3:** Xây dựng Header, Logo (`275×68px`), Mega-Menu (`48px`), Footer và đăng ký **100% Custom UX Builder Elements** (`add_ux_builder_shortcode`) có đầy đủ `options` cho người dùng tự sửa; ghim Trang chủ (`menu_order = -100`) lên vị trí `#1` trong `wp-admin/edit.php?post_type=page`.
- **Bước 4:** Xây dựng Lưới sản phẩm 4 cột, hiệu ứng Hover thông số `✔` trong suốt nhẹ (`0.72`), Popup Xem Nhanh 2 cột (Video + 3 bước Mua nhanh), Trang Chi tiết sản phẩm (`PDP` ảnh `420×360px`), Bộ lọc thông minh (`Smart Filter URL-as-State`), Checkout rút gọn & Tính phí ship GHN.
- **Bước 5:** Xây dựng các trang Landing Page chạy Ads 9 khối (`Smart Ads Focus Mode`), Trang Giới thiệu, Nhà sản xuất, Tư vấn kỹ thuật / Video lắp đặt, Liên hệ, Chính sách (có Sticky TOC) và cổng quản trị nhanh (`Quick Studio` + `/crm/`).
- **Bước 6:** Kích hoạt kiến trúc Tốc độ 6 Lớp (`MU-Plugin Instant Cache < 85ms` + `WP Rocket` chống lỗi `.html_gzip` + Inline CSS/Font + Kho ảnh `WebP` cô lập + Prefetch khi rê chuột).
- **Bước 7:** Tự động mở trình duyệt thật (Headless Edge/Chrome CDP hoặc Playwright) **tự chụp ảnh màn hình kiểm tra trực quan từng khối trên Desktop (`1440×900`) & Mobile (`390×844`)**, đọc lại chính ảnh vừa chụp để tự phát hiện và sửa ngay mọi lỗi lệch khung, mất chữ, đè nút trước khi báo cáo người dùng!
- **Bước 8:** Chạy bộ 3 công cụ kiểm toán độc lập (`audit_ui_ux_cro.py`, `claude-seo`, `ifixai-agent-auditor/cli.py`) đạt **`Exit code 0` & `Grade A`**, bàn giao kèm hướng dẫn sử dụng.

---

## 🛡️ PHẦN 3: 20 SAI SÓT CHÍ MẠNG CẦN TRÁNH TUYỆT ĐỐI (`POST-MORTEM & ANTI-PATTERNS`)

Đây là 20 lỗi thực tế đã đúc kết từ các dự án **Tưới Nông Nghiệp (`V3.7.6`)**, **InfoAsia (`V19`)**, **GolfViet (`V2.5.2`)**, **HelenaVan** và **BYD**. AI Agent **TUYỆT ĐỐI CẤM LẶP LẠI**:

| STT | Nhóm Lỗi | ❌ Sai Sót Thường Gặp (CẤM LÀM) | ✅ Giải Pháp Chuẩn Hóa Bắt Buộc (PHẢI LÀM) |
| :-: | :--- | :--- | :--- |
| **01** | **UX Builder** | Để Trang chủ (`Front Page`) có `menu_order = 0` và tên bắt đầu bằng chữ `T` (`Tưới nông nghiệp`), khiến Trang chủ bị đẩy sang **Trang 2 (vị trí #21)** trong `wp-admin/edit.php?post_type=page` làm người dùng không tìm thấy chỗ sửa. | Luôn đặt **`menu_order = -100`** cho Trang chủ, tăng `edit_page_per_page = 50`, gắn **Thanh nút mở nhanh UX Builder** ngay đầu trang `Pages` và trên thanh Admin Bar (`🎨 Sửa Trang Chủ (UX Builder)`). |
| **02** | **UX Builder** | Bật `defer_non_critical_scripts` (defer `jquery-core`, `flatsome-js`) và `WP Rocket DelayJS` cả khi đang mở iframe của UX Builder (`?uxb_iframe=1`), làm đơ trình kéo thả. | Tạo hàm `is_ux_builder_request()` kiểm tra `$_GET['uxb_iframe']`, `$_GET['app'] === 'uxbuilder'`, `ux_builder_is_iframe()`. Khi `true`, **tắt 100%** defer JS, DelayJS, dequeue CSS/JS và HTML buffer rewrite. |
| **03** | **UX Builder** | Viết shortcode giao diện cứng trong PHP mà không khai báo `options` trong `add_ux_builder_shortcode()`, khiến nhân sự Marketing bấm vào khối không sửa được chữ/ảnh. | **100% Custom Shortcode** phải đăng ký vào hook `ux_builder_setup` kèm đầy đủ `options` (Tiêu đề, Mô tả, Ảnh Media Library ID + URL, Nút CTA, Màu nền, Padding, Ẩn/Hiện). |
| **04** | **UX Builder** | Dán HTML nhiều dòng hoặc comment `<!-- ... -->` trực tiếp vào `post_content`, bị bộ lọc `wpautop` của WordPress tự chèn `<p></p>` và `<br>` gây hở trắng từng mảng lớn. | Tuyệt đối không đặt comment HTML giữa các shortcode. Đóng gói giao diện phức tạp thành Shortcode PHP sạch và thêm CSS `p:empty { display: none !important; }`. |
| **05** | **Tỷ lệ View & Lưới SP** | Chia lưới sản phẩm **5 cột/hàng** trên khung `1220px` khiến thẻ sản phẩm chỉ rộng `~230px`, hình ảnh sản phẩm bị thu nhỏ lí nhí khó nhìn. | Trên container chuẩn **`1220px`**, lưới sản phẩm chuẩn đẹp nhất là **1 hàng 4 sản phẩm (`25%` = `~303px/card`)**, hiển thị **2 hàng = 8 sản phẩm/khối** (bấm Xem thêm tải `+8` sản phẩm), khung ảnh `.box-image` cao **`186px`** (`img max-height: 170px`). |
| **06** | **Header & Menu** | Thu nhỏ Header/Logo/Menu quá đà để tiết kiệm chiều dọc khiến Logo bé tí và viền vàng mục menu đang chọn dính sát mép dưới thanh xanh, chữ Breadcrumb dính sát đáy menu. | Giữ **Logo `275×68px`** (`#masthead min-height: 82px`), thanh Menu xanh **`#wide-nav min-height: 48px`** (`font-size: 13.8px`, `padding: 8px 16px`, `margin: 4px 0` để pill active có khoảng thở trên/dưới), và cách đáy menu **`18px`** trước khi vào Breadcrumb. |
| **07** | **Hover Thông Số SP** | Khi hover vào sản phẩm chỉ hiện 4 ô tĩnh chung chung thay vì lấy đúng thông số kỹ thuật thực tế của sản phẩm, hoặc để nền xanh đặc `opacity: 0.97` + `blur(4px)` che kín mít hình sản phẩm bên dưới. | Bóc tách trực tiếp từng dòng từ `post_excerpt` (`$product->get_short_description()`, fallback sang thuộc tính WooCommerce) hiển thị thành danh sách dấu tích **`✔`**. Nền `.agro-spec-overlay` dùng **trong suốt nhẹ `rgba(224, 238, 174, 0.72)`** + `backdrop-filter: none` + `text-shadow` trắng mịn để thấy rõ ảnh SP bên dưới. |
| **08** | **Nút Video Trên Card** | Đặt nút Play Video (`▶`) ở giữa ảnh nhưng khi hover hiện bảng thông số `✔` lại dịch nút lên `top: 24%`, làm nút bị lệch và che khuất chữ thông số kỹ thuật. | Lúc bình thường nút Play Video nằm giữa ảnh (`44×44px`). **Khi hover vào card**, tự động thu gọn nút Play Video (`32×32px`) và **neo xuống góc dưới phải (`bottom: 6px; right: 6px; z-index: 25`)**, đồng thời ẩn tạm nhãn `"X tùy chọn"`. |
| **09** | **Popup Quick-View** | Đặt `.gv-qb-body { display: flex; flex-direction: column }` mà quên `flex-shrink: 0` trên khung mô tả `#gv-qb-intro-box`, khiến Flexbox ép dẹp khung `1. Giới thiệu sản phẩm` còn `18px` mất hết chữ. | Đặt `.gv-qb-body { display: block !important; overflow-y: auto !important; }` và khóa `#gv-qb-intro-box { flex-shrink: 0 !important; min-height: 104px !important; max-height: 156px !important; overflow-y: auto !important; }`. |
| **10** | **Ảnh Trang Chi Tiết (PDP)** | Ép `display: flex !important` lên `.woocommerce-product-gallery__image` hoặc `.slide`, làm hỏng thuật toán tính chiều cao của Flickity Slider khiến ảnh chính trên trang Chi tiết sản phẩm bị co nhỏ hoặc biến mất. | Trên `body.single-product`, giữ `.woocommerce-product-gallery__image { display: block !important; }` và định kích thước trực tiếp trên thẻ `img` (`height: 360px !important; max-width: 420px !important; object-fit: contain !important; margin: 0 auto !important;`). |
| **11** | **Nút Bấm Không Đều** | Đặt 2 nút cạnh nhau ở chân khối danh mục (*"Xem thêm +8 sản phẩm"* và *"Xem toàn bộ 37 sản phẩm"*) nhưng khác `padding` / `line-height` làm 1 nút to 1 nút nhỏ. | Hai nút đứng cạnh nhau bắt buộc khóa cùng **`height: 44px !important`**, `display: inline-flex !important`, `align-items: center !important`, `justify-content: center !important`, `padding: 0 24px !important`, `font-size: 13.5px !important`. |
| **12** | **Mega Menu Laptop** | Trên màn hình Laptop Windows bật Scale `125%–150%` (viewport rộng `1200px–1280px`), Mega Menu quá cao hoặc tự rớt từ 4 cột xuống 2 cột che kín hết Hero Banner. | Khóa Mega Menu **4 cột ngang siêu gọn (`max-width: 1120px`, chiều cao `~170px–240px`)** xuyên suốt từ `1025px` trở lên, kèm cầu nối hover vô hình `::before { height: 14px; top: -14px; }` để di chuột không bị mất menu. |
| **13** | **Lỗi "Skip to content"** | Khi gỡ/dequeue `flatsome-main.css` hoặc tối ưu CSS inline để lấy 100 điểm PageSpeed, quên định nghĩa class `.screen-reader-text`, làm hiện chữ `"Skip to content"` và viền trắng `8px` ở đầu trang Mobile. | Luôn nhúng ngay đầu CSS inline: `html,body{margin:0;padding:0} .screen-reader-text,a.skip-link.screen-reader-text{clip-path:inset(50%);width:1px;height:1px;position:absolute;overflow:hidden;margin:-1px;padding:0;border:0}`. |
| **14** | **Lỗi Tự Tải File `download`** | Bật WP Rocket trên máy chủ **OpenLiteSpeed (`lshttpd`)**, `.htaccess` rewrite sang file `.html_gzip` khiến OpenLiteSpeed trả về `Content-Type: application/octet-stream` làm trình duyệt tự tải file `download` trắng! | Bắt buộc thêm `add_filter('rocket_force_gzip_htaccess_rules', '__return_false', 99)` và hàm `self_heal_ols_htaccess_gzip_rewrite()` tự động cắt bỏ khối rewrite `.html_gzip` trong `.htaccess`. |
| **15** | **Cache Làm Mất Admin Bar** | Khi dùng Full-Page Cache cho cả người dùng đã đăng nhập, nếu phục vụ nguyên xi file HTML của khách vãng lai sẽ làm biến mất thanh `#wpadminbar` màu đen của Admin. | Dùng kiến trúc **`HIT-SPLICED`**: Lưu riêng mảnh `_adminbar_default.html` (có sẵn nút `🎨 Sửa Trang Chủ (UX Builder)` & `+ Đăng SP Nhanh`) và ghép động vào HTML cache trong `< 15ms` khi phát hiện cookie `wordpress_logged_in_*`. |
| **16** | **Mobile iOS Auto-Zoom & Đè Chữ Select** | Để `<input>`, `<select>` trên Mobile có `font-size: 13px–14px` (khiến iPhone Safari tự động zoom giật khung hình khi bấm vào) và thiếu `padding-right` trên `<select>` làm chữ đè lên mũi tên dropdown. | Ở `@media (max-width: 849px)`, ép toàn bộ `input, select, textarea { font-size: 16px !important; }` và `select { padding-right: 32px !important; text-overflow: ellipsis !important; }`. |
| **17** | **Nút Nổi Đè Nút Mua Hàng** | Để cụm nút nổi Zalo/Hotline/Chatbot (`bottom: 20px; right: 20px`) đè trực tiếp lên thanh `Sticky Add-to-Cart Bar` ở đáy màn hình Mobile hoặc đè lên nút gửi trong Popup Mua Nhanh. | Khi ở trang sản phẩm có Sticky Bottom Bar trên Mobile, nâng cụm nút nổi lên `bottom: 78px !important`; khi mở Popup Mua Nhanh hoặc mở khung Chat (`body.gv-quickbuy-open`, `body.gv-chat-is-open`), tự động ẩn cụm nút nổi (`opacity: 0; pointer-events: none`). |
| **18** | **Dính Chữ Trong Thẻ Heading** | Viết `<h1>Giải pháp<span>MES AI</span>tự động</h1>` thiếu khoảng trắng trước/sau thẻ `<span>`, làm Google đọc thành `"Giải phápMES AItự động"` và trừ điểm SEO. | Luôn đặt khoảng trắng tường minh bên ngoài thẻ `<span>` hoặc kiểm tra bằng regex `preg_replace('/<\/span>(?=[A-Za-zÀ-ỹ0-9])/u', '</span> ', $html)`. |
| **19** | **Nhân Đôi Thẻ Meta Khi Bật Yoast SEO** | Vừa bật plugin **Yoast SEO (`v28.5 / v28.7`)** vừa tự `echo '<meta name="description">'` trong Child Theme, khiến `<head>` bị trùng 2 thẻ `description` và 2 khối Schema. | Kiểm tra `if (defined('WPSEO_VERSION'))`: Truyền dữ liệu chuẩn qua các filter `wpseo_title`, `wpseo_metadesc`, `wpseo_canonical`, `wpseo_robots` và nhường Yoast in thẻ meta (chỉ giữ lại 1 hệ thống Schema JSON-LD 6 lớp duy nhất). |
| **20** | **Lộ Link Staging & Mất Link SEO Cũ** | Quên bật `noindex` trên tên miền thử nghiệm (`demo.*`), hoặc khi làm lại web cũ không quét Sitemap cũ gây hàng loạt lỗi `404`. | Tự động bật `noindex, nofollow` khi `HTTP_HOST` là `demo.*`/`staging.*`/`localhost` và tự động mở `index, follow` khi lên tên miền chính; quét 100% XML Sitemap cũ và lập bảng `301 Redirect` đạt `0` lỗi `404`. |

---

## 🎨 PHẦN 4: QUY CHUẨN UX BUILDER 100% OPTION CHO NGƯỜI DÙNG TỰ CHỈNH SỬA

1. **Mọi khối giao diện phải có Option trong UX Builder (`add_ux_builder_shortcode`):**
   - Không bao giờ khóa cứng văn bản hoặc hình ảnh trong file `.php` mà không mở `options`.
   - Mỗi Shortcode đăng ký trong hook `ux_builder_setup` phải cung cấp đầy đủ:
     - `Nhóm Nội dung`: Nhãn phụ (`eyebrow`/`kicker`), Tiêu đề chính (`title`), Phần chữ nổi bật (`highlight`), Mô tả (`lead`/`desc`).
     - `Nhóm Hình ảnh & Video`: Chọn ảnh từ Media Library (`type => 'image'`) kết hợp URL dự phòng.
     - `Nhóm Danh mục / Sản phẩm / Tab`: ID danh mục gốc (`parent_cat`), danh sách Sub-Tab (`ID:Tên|ID:Tên`), số lượng hiển thị (`limit`, mặc định `8` cho lưới 4 cột × 2 hàng).
     - `Nhóm Nút bấm CTA & Liên kết`: Chữ trên nút (`cta_text`) và đường dẫn (`cta_url`).
2. **Ghim Trang Chủ lên vị trí #1 & Thanh Mở Nhanh UX Builder:**
   - Tự động đặt `menu_order = -100` cho trang `page_on_front` và đặt `edit_page_per_page = 50` cho tài khoản Admin.
   - Hiển thị hộp thông báo màu xanh lá ở đầu trang `wp-admin/edit.php?post_type=page` kèm các nút bấm 1-Click: **`🎨 Sửa Trang Chủ Bằng UX Builder`**, **`Giới Thiệu (UX Builder)`**, **`Nhà Sản Xuất (UX Builder)`**, **`Liên Hệ (UX Builder)`**.
   - Gắn nút **`🎨 Sửa Trang Chủ (UX Builder)`** trực tiếp trên thanh `#wpadminbar` và trong menu trái `Trang (Pages)`.
3. **Bảo vệ Iframe của UX Builder (`is_ux_builder_request()`):**
   - Trong `agro-performance-engine.php`, mọi hàm tối ưu (`defer_non_critical_scripts`, `async_non_critical_styles`, `conditional_dequeue_assets`, `start_full_document_buffer`, `pre_get_rocket_option_delay_js`) bắt buộc kiểm tra `if (is_admin() || self::is_ux_builder_request()) return;` để trình kéo thả UX Builder luôn mượt 100%.

---

## 📐 PHẦN 5: QUY CHUẨN VIEW NHÌN, TỶ LỆ VÀNG ĐA KHUNG HÌNH & HIỆU ỨNG HOVER

| Thành Phần Giao Diện | Thông Số Chuẩn Đã Kiểm Chứng (`Desktop 1366px–1440px` & `Mobile 390px`) | Ghi Chú Kỹ Thuật |
| :--- | :--- | :--- |
| **Chiều rộng Container chính** | **`max-width: 1220px`** (chuẩn Shopee Mall / Pro-Shop hiện đại) | Rộng rãi, cân đối, giúp lưới 4 cột có độ rộng mỗi thẻ đạt **`303px`**. |
| **Header Chính (`#masthead`) & Logo** | Cao **`min-height: 82px`** • Logo **`275 × 68 px`** (`object-fit: contain`) • Ô tìm kiếm & nút Giỏ hàng cao **`42px`** | Logo sắc nét, dễ đọc tên công ty và khẩu hiệu thương hiệu. |
| **Thanh Menu Ngang (`#wide-nav`)** | Cao **`min-height: 48px`** • Chữ **`13.8px` (`font-weight: 700`)** • Mục menu `padding: 8px 16px`, `margin: 4px 0`, `border-radius: 8px` | Mục menu đang chọn (Active Pill có viền vàng đáy) nằm gọn chính giữa thanh xanh, có khoảng thở trên/dưới. |
| **Khoảng cách dưới Menu xanh** | **`padding-top: 18px`** trên `.shop-page-title` / `.gv-archive-hero` / `.page-wrapper` | Chữ Breadcrumb tách biệt rõ ràng, không bao giờ dính sát đáy thanh menu xanh. |
| **Lưới Sản Phẩm (Product Grid)** | **Desktop:** **4 cột/hàng (`25%` = `303px/card`)**, mỗi khối hiển thị **2 hàng = 8 sản phẩm** (nút Xem thêm tải **`+8`**).<br>**Tablet (`768px`):** **3 cột/hàng (`33.33%`)**.<br>**Mobile (`390px`):** **2 cột/hàng (`50%`)**. | Khung ảnh `.box-image` trên Desktop cao **`186px`** (`img max-height: 170px; max-width: 92%; object-fit: contain`), nền trắng `#FFFFFF`. |
| **Bố Cục Bên Trong Thẻ Sản Phẩm (`.box-text`)** | 1. Chuyên mục phụ (`10px`, chữ hoa xám `#64748B`).<br>2. Tên sản phẩm (`13.5px`, đậm `700`, khóa đúng 2 dòng `height: 36px; line-height: 18px`).<br>3. Hàng nhãn thông số `Spec Pills` (`height: 20px`, tối đa 3 nhãn).<br>4. Giá bán (`15.5px`, đỏ đậm `#B91C1C`, `font-weight: 800`) nằm trên 1 dòng riêng.<br>5. Hàng nút đáy (`height: 32px`): Nút **`⚡ Mua nhanh / Chọn quy cách`** (`flex: 1`) + Nút con mắt Xem nhanh **`👁`** (`32×32px`). | Dùng `display: flex; flex-direction: column` trên `.price-wrapper` để hàng `Spec Pills` và `Giá` không bao giờ đè lên nhau. |
| **Hiệu Ứng Hover Hiện Thông Số Kỹ Thuật (`✔`)** | Bảng `.agro-spec-overlay` phủ lên `.box-image` với nền **xanh cốm trong suốt nhẹ `rgba(224, 238, 174, 0.72)`**, `backdrop-filter: none`, chữ `#0F172A` (`12px`, `font-weight: 600`) có viền sáng trắng mịn `text-shadow: 0 1px 2px rgba(255,255,255,0.95)` | Vừa đọc rõ danh sách 5–6 dòng thông số kỹ thuật (`✔`) lấy từ `post_excerpt`, vừa nhìn thấy rõ hình dáng sản phẩm bên dưới. |
| **Cặp Nút Chân Khối Danh Mục** | Nút trái (`.gv-showcase-loadmore-btn`) và Nút phải (`.gv-showcase-more-btn`) khóa cùng **`height: 44px !important`**, `min-width: 315px !important`, `border-radius: 999px` | Nút trái nền xanh đậm `#047857` chữ trắng; nút phải nền trắng viền xanh `#047857` — cân xứng tuyệt đối 100%. |
| **View Nhìn 1 Màn Hình (`Single-Viewport Fit`)** | Với các khối tương tác nhiều Tab (như Copilot `/mesai` hoặc Khối 5 Phân hệ của InfoAsia), tổng chiều cao toàn khối khóa trong khoảng **`450px – 510px`** trên màn hình Laptop `1366×768` | Người dùng thấy trọn vẹn cả Thanh Tab trên + Cột điều khiển trái + Nội dung giữa + Ảnh 2K bên phải trong **1 view nhìn duy nhất** không cần cuộn chuột. |

---

## ⚡ PHẦN 6: KIẾN TRÚC TỐI ƯU TỐC ĐỘ 6 LỚP (`99–100` PAGESPEED & `< 85MS` TTFB)

1. **Lớp 1 — MU-Plugin Instant Full-Page Cache (`wp-content/mu-plugins/agro-instant-page-cache.php`):**
   - Phục vụ HTML nén `gzip` ngay tại `muplugins_loaded` trong **`< 15ms – 85ms`**.
   - Hỗ trợ **`MU-HIT-SPLICED`**: Tự động ghép động thanh `#wpadminbar` và số lượng giỏ hàng vào bản cache tĩnh cho cả Admin đang đăng nhập.
2. **Lớp 2 — Khóa An Toàn `WP Rocket 2026 Pro v3.23.3.3` Trên OpenLiteSpeed (`lshttpd`):**
   - Khóa `minify_css = 0`, `minify_concatenate_css = 0`, `rocket_force_gzip_htaccess_rules = false` + tự động làm sạch quy tắc rewrite `.html_gzip` trong `.htaccess` (chống lỗi trình duyệt tự tải file `download`).
   - Đưa `zarsrc`, `zdlink`, `zalo_id`, `fbclid`, `gclid`, `ttclid`, `utm_id` vào `rocket_cache_ignored_parameters`.
3. **Lớp 3 — Inline Font & Inline Minified Child CSS (`0` Render-Blocking CSS):**
   - Nhúng `@font-face` (`Be Vietnam Pro`, `font-display: swap`) và `style.css` đã nén trực tiếp vào `<head>` kèm quy tắc ẩn `.screen-reader-text, a.skip-link.screen-reader-text` (chống hiện chữ `"Skip to content"`).
4. **Lớp 4 — Kho Ảnh WebP Cô Lập (`wp-content/gv-webp-cache/`) & Responsive LCP Preload:**
   - Tự động chuyển đổi ảnh `.jpg/.png` sang `.webp` (kèm bản `-640w.webp` cho Mobile), giữ nguyên ảnh gốc trong `/uploads/`.
   - Chỉ gắn `fetchpriority="high" loading="eager"` + `<link rel="preload" as="image">` cho duy nhất 1 ảnh LCP đầu trang.
5. **Lớp 5 — Gỡ Bỏ Tài Nguyên Thừa Theo Ngữ Cảnh (`Conditional Dequeue`):**
   - Gỡ `zxcvbn.min.js` (`395 KB`) trừ trang Tài khoản/Checkout; gỡ `contact-form-7` ở trang không có form CF7; gỡ `photoswipe` và `woo-variation-swatches` ở ngoài trang PDP; gỡ `wc-cart-fragments`.
6. **Lớp 6 — Điều Hướng Tức Thời Khi Rê Chuột (`Speculation Rules API` + `agro-instant-page.js`):**
   - Tự động prefetch HTML trang sản phẩm ngay khi người dùng rê chuột lên thẻ sản phẩm trên 65ms.

---

## 🔍 PHẦN 7: CHUẨN SEO KỸ THUẬT, BỘ YOAST SEO FULL 2026 (`V28.5 / V28.7`) & AI SEARCH (`GEO`)

1. **Tích Hợp Đồng Bộ Với Bộ 6 Plugin `Yoast SEO Full 2026` (`inc/agro-seo-geo-engine.php`):**
   - Khi `defined('WPSEO_VERSION')` tồn tại, module SEO của Child Theme truyền trực tiếp `<title>` (`50–60` ký tự), `<meta name="description">` (`142–158` ký tự), `canonical` sạch và `og:image` vào các filter `wpseo_title`, `wpseo_metadesc`, `wpseo_canonical`, `wpseo_opengraph_*`, `wpseo_robots` và nhường Yoast xuất thẻ meta để **đạt đúng `title=1 | desc=1 | canonical=1` (0 trùng lặp)**.
   - Gắn `add_filter('wpseo_json_ld_output', '__return_false', 99)` để xuất duy nhất 1 khối **Schema JSON-LD 6 Lớp `@graph`** (`Organization`, `Store`/`LocalBusiness`, `WebSite`, `BreadcrumbList`, `Product`, `Article`) của `Agro_SEO_GEO_Engine`.
2. **Bảo Vệ Schema `Product` & Tệp `/llms.txt` Cho AI Search (`GEO`):**
   - Với sản phẩm giá `0₫` ("Liên hệ báo giá"), tự động ẩn trường `offers` trong Schema `Product` để không bị Google Search Console báo lỗi.
   - Tự động phục vụ tệp `/llms.txt` chuẩn hóa thông tin pháp lý, danh mục thương hiệu/sản phẩm và liên kết trọng yếu cho các công cụ AI (ChatGPT, Claude, Perplexity, Google AI Overviews).
3. **Khóa `noindex` Tự Động Trên Demo & Tự Mở `index, follow` Khi Lên Production:**
   - Kiểm tra `HTTP_HOST`: Nếu đang ở tên miền `demo.*`, `staging.*`, `localhost` thì tự động xuất `noindex, nofollow` + khóa `/robots.txt` (`Disallow: /`); ngay khi chuyển sang tên miền chính thức của khách hàng, tự động mở `index, follow` 100% mà không cần sửa code.

---

## 🎯 PHẦN 8: KIẾN TRÚC LANDING PAGE CHẠY ADS (`9 KHỐI CRO`) vs. WEB MUA SẮM (`HYBRID CATALOG`)

### 8.1. Trang Landing Page Chạy Ads (B2B / Dịch Vụ / Giải Pháp Chủ Lực)
- **Cơ chế `Smart Ads Focus Mode`:** Khi phát hiện tham số quảng cáo (`?utm_source`, `gclid`, `fbclid`, `ttclid`, `zarsrc`), tự động ẩn thanh Mega-Menu nhiều mục gây xao nhãng, bật **Thanh Header Chốt Đơn Tập Trung** + **Sticky CTA Mobile**.
- **9 Khối Chuẩn UX Builder:** `(1) Hero Above-the-Fold + 4 KPI` $\rightarrow$ `(2) Dải Tín Nhiệm 1 Dòng` $\rightarrow$ `(3) Đối Chiếu Trước & Sau` $\rightarrow$ `(4) Khung Tương Tác / Ảnh Thực Tế 2K Gọn Trong 1 View Nhìn (506px)` $\rightarrow$ `(5) Lưới Lợi Ích Cốt Lõi Bento` $\rightarrow$ `(6) Quy Trình 4 Bước` $\rightarrow$ `(7) Case Study Thực Tế Đúng Ngành` $\rightarrow$ `(8) Câu Hỏi Thường Gặp (FAQ)` $\rightarrow$ `(9) Form Thu Lead 2 Cột (<= 4 ô) Đẩy Thẳng Về /crm/`.

### 8.2. Website Có Sản Phẩm Mua Sắm (`Hybrid Catalog 3 Luồng Chuyển Đổi`)
- **Luồng 1 — Sản phẩm Đơn giản có giá (`Simple Product, Price > 0`):** Hiện giá đỏ đậm + Nút **`⚡ Mua nhanh`** + Nút **`👁`** Xem nhanh.
- **Luồng 2 — Sản phẩm Nhiều Biến Thể / Quy Cách (`Variable Product`):** Hiện huy hiệu **`N tùy chọn`** ở góc dưới phải ảnh + Giá **`Từ XX.XXX₫`** + Nút **`⚡ Chọn quy cách`** + Nút **`👁`**.
- **Luồng 3 — Sản phẩm Dự Án Báo Giá Riêng (`Price = 0`):** Hiện nhãn **`Liên hệ báo giá`** + Nút **`Nhận Báo Giá Kỹ Sư 1:1`** (cấm hiện `"0₫"`).

---

## 🛒 PHẦN 9: XEM NHANH (`QUICK-VIEW`), MUA NHANH (`QUICK-BUY`), CHECKOUT & TÍNH PHÍ SHIP (`GHN LIVE API`)

1. **Popup Xem Nhanh (`Quick-View`) Kết Hợp Mua Nhanh 1 Bước (`inc/agro-quick-buy.php`):**
   - **Cột Trái:** Phát trực tiếp Video thực tế (`_product_video_url` YouTube/Shorts/MP4) kèm thanh chuyển **`[▶ VIDEO THỰC TẾ]` ↔ `[ẢNH SẢN PHẨM]`** + Hộp cam kết chính hãng.
   - **Cột Phải (3 Bước):**
     - `1. Giới thiệu sản phẩm` (`#gv-qb-intro-box` khóa `min-height: 104px; max-height: 156px; flex-shrink: 0` — không bao giờ bị Flexbox ép dẹp).
     - `2. Chọn quy cách / biến thể` (Bấm chọn quy cách đổi ngay Giá bán, SKU và Tạm tính).
     - `3. Đặt mua nhanh 1 chạm` (Nhập Họ tên, SĐT `type="tel"`, Tỉnh/Quận/Phường, Địa chỉ tạo đơn `wc_create_order` ngay tại chỗ) hoặc `Thêm vào giỏ`.
2. **Checkout Rút Gọn Việt Nam & Tính Phí Ship Tự Động (`inc/agro-ghn-shipping.php`):**
   - Xóa bỏ `postcode`, `company`, `address_2`, `state`; chỉ giữ **Họ tên + SĐT (`type="tel" inputmode="numeric"`) + Tỉnh/Thành $\rightarrow$ Quận/Huyện $\rightarrow$ Phường/Xã + Số nhà/Tên đường**.
   - Tự động chọn kho xuất hàng gần nhất (ví dụ: TP.HCM, Đà Lạt, Hà Nội), tính tổng khối lượng giỏ hàng và gọi **API Giao Hàng Nhanh (GHN)** trả về phí ship thực tế + bảng giá dự phòng 63 tỉnh thành + tự động **Miễn phí vận chuyển** khi đơn hàng đạt ngưỡng cấu hình.

---

## ✅ PHẦN 10: MASTER CHECKLIST 100 ĐIỂM NGHIỆM THU TRƯỚC KHI BÀN GIAO (`EXIT CODE 0`)

- [ ] **1. UX Builder & Quản trị (10đ):** Trang chủ ghim ở vị trí `#1` (`menu_order = -100`), có thanh nút mở nhanh UX Builder, 100% khối giao diện có `options` chỉnh sửa trực quan, `is_ux_builder_request()` hoạt động mượt mà.
- [ ] **2. Header, Logo & Menu (10đ):** Container `1220px`, Logo `275×68px`, Header `82px`, Menu `48px` (`13.8px`), khoảng thở dưới menu `18px`, Mega-Menu 4 cột gọn `<= 240px`.
- [ ] **3. Lưới Sản Phẩm & Hover (15đ):** Lưới **4 cột/hàng (`303px/card`)**, 2 hàng = 8 sản phẩm (`+8` Xem thêm), khung ảnh `186px`, Hover hiện thông số `✔` từ `post_excerpt` trên nền **trong suốt nhẹ `rgba(224, 238, 174, 0.72)`** thấy rõ ảnh bên dưới, nút Play Video tự neo góc dưới phải `32×32px` khi hover, 2 nút chân khối cao bằng nhau `44px`.
- [ ] **4. Quick-View, PDP & Mua Nhanh (15đ):** Khung `1. Giới thiệu sản phẩm` trong Quick-View cao `156px` rõ chữ, chọn biến thể đổi giá tức thì, ảnh trang Chi tiết sản phẩm (`PDP`) rõ nét `420×360px` (`display: block !important`).
- [ ] **5. Smart Filter & Tìm Kiếm (10đ):** Đồng bộ 2 chiều `URL-as-State` và `$GLOBALS['wp_the_query']`, hiện số đếm `(N)` trên từng chip lọc, ẩn chip `count = 0`.
- [ ] **6. Checkout & Phí Ship GHN (10đ):** Form Checkout 3 tầng gọn nhẹ, tự động tính cước GHN theo Tỉnh/Quận/Phường từ kho gần nhất + ngưỡng Freeship tự động.
- [ ] **7. Responsive Mobile (`390×844`) & WCAG 2.2 AA (10đ):** `0px` tràn ngang trên cả 4 khung hình (`375px / 768px / 1366px / 1440px`), ô `<input>/<select>` trên Mobile `font-size: 16px !important`, `<select>` `padding-right: 32px`, 100% `<button>` có `type`, 100% icon SVG inline.
- [ ] **8. Tốc Độ `99–100` & Cache `< 85ms` (10đ):** MU-Plugin Instant Cache (`HIT-SPLICED`) + WP Rocket 2026 Pro `v3.23.3.3` + khóa chống lỗi `.html_gzip` download trên OpenLiteSpeed + chống lỗi `"Skip to content"` + 100% ảnh WebP.
- [ ] **9. Yoast SEO Full 2026 & GEO (5đ):** Kích hoạt đủ bộ Yoast SEO `v28.5 / Premium v28.7`, đúng `title=1 | desc=1 | canonical=1` (0 trùng thẻ), 6 lớp Schema JSON-LD, `/llms.txt`, khóa `noindex` trên `demo.*` và bảo toàn 100% URL cũ (`0` lỗi `404`).
- [ ] **10. Kiểm Toán Tự Động Độc Lập (5đ):** Tự chụp ảnh màn hình kiểm tra trực quan bằng trình duyệt thật + chạy `audit_ui_ux_cro.py` & `ifixai-agent-auditor/cli.py` đạt **`Exit code 0` & `Grade A`**.
