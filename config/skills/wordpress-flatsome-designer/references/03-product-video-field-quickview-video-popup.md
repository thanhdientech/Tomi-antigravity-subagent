# Kiến Trúc Trường Nhập Video Sản Phẩm, Nút Play Trên Card & Popup Xem Nhanh Có Video (`Product Video Field & Quick-View Video Modal` — Chuẩn `densankhauhcm.com`)

> **Nguồn Thực Chứng Gốc:** Hệ thống thương mại điện tử Đèn Sân Khấu NERHOR ([https://densankhauhcm.com/](https://densankhauhcm.com/) & trang chi tiết [https://densankhauhcm.com/san-pham/den-moving-200w-chieu-quan-karaoke/](https://densankhauhcm.com/san-pham/den-moving-200w-chieu-quan-karaoke/) — Mã nguồn thực tế `js/products.js?v=7.0`, `css/products.css?v=7.0`, `api-products.php`).

---

## 1. Quy Trình Nghiệp Vụ 4 Tầng: Nhập Video Sản Phẩm $\rightarrow$ Hiện Nút Play Trên Card $\rightarrow$ Popup Xem Nhanh Có Video $\rightarrow$ Trang Chi Tiết Đồng Bộ (`4-Tier Product Video Architecture`)

Khi thiết kế hoặc nâng cấp website bán hàng WordPress / WooCommerce / Flatsome hoặc Hybrid Static-API Catalog (đặc biệt các ngành thiết bị ánh sáng, đèn sân khấu, máy móc, nội thất, mỹ phẩm, thời trang, đồ công nghệ cần xem hiệu ứng thực tế), bắt buộc triển khai **Kiến trúc Video Sản Phẩm 4 Tầng**:

| Tầng Kiến Trúc | Khi Sản Phẩm CÓ Nhập Video (`hasVideo == true`) | Khi Sản Phẩm KHÔNG Nhập Video (`hasVideo == false`) |
| :--- | :--- | :--- |
| **Tầng 1: Trường Nhập Video Trong Admin (`wp-admin` / Custom Field)** | - Cho phép nhập link YouTube thường (`youtube.com/watch?v=...`), YouTube Shorts (`youtube.com/shorts/...`), link rút gọn (`youtu.be/...`), hoặc dán trực tiếp trong đầu mô tả sản phẩm.<br>- Tự động bóc tách mã `youtube_id` (11 ký tự) và xóa URL thô khỏi văn bản mô tả để giao diện sạch 100%. | - Trả về `youtube_id = ""` (rỗng).<br>- Giữ nguyên luồng hiển thị ảnh đại diện và thư viện ảnh (`gallery_images`) tiêu chuẩn. |
| **Tầng 2: Thẻ Sản Phẩm Ngoài Danh Sách (`Product Card` — Trang Chủ & Danh Mục)** | - Gắn thuộc tính `data-youtube="${ytId}"` vào `.product-card`.<br>- Hiển thị **Nút Tròn Play Video (`▶` `.badge-video.quick-view-trigger`)** nằm chính giữa ảnh đại diện (`46×46px`, nền kính mờ `rgba(0,0,0,0.65)`, `backdrop-filter: blur(4px)`, hover phóng `scale(1.15)` đổi màu đỏ hồng `rgba(255,45,85,0.85)`).<br>- Giữ nút con mắt **Xem Nhanh (`👁` `.btn-quick-view`)** cạnh nút `Thêm vào giỏ`. | - **Ẩn hoàn toàn nút `▶`** trên ảnh sản phẩm để không đánh lừa người dùng.<br>- Chỉ hiển thị ảnh sản phẩm + badge giảm giá `-%` (nếu có) + nút `Thêm vào giỏ` và nút con mắt `👁` (`.btn-quick-view`). |
| **Tầng 3: Popup Xem Nhanh Sản Phẩm (`#quickViewModal` — Khi Click Nút `▶` Hoặc `👁`)** | - Bấm vào nút `▶` trên ảnh hoặc nút `👁` đều mở ngay **Popup Xem Nhanh 2 Cột (`#quickViewModal` — `max-width: 980px`, `height: min(90vh, 660px)`)**.<br>- **Cột Trái (`46%`):** Khung chính (`#qvMainMedia`) **tự động phát ngay Video sản phẩm** (`youtube-nocookie.com/embed/${ytId}?autoplay=1&mute=0&controls=1&rel=0&modestbranding=1&playsinline=1`). Bên dưới là thanh Thumbnail (`#qvThumbs`) có ô **`[▶ VIDEO]`** đầu tiên (viền `#00c8ff`) + các ảnh sản phẩm để khách bấm chuyển qua lại giữa Video và Ảnh.<br>- **Cột Phải (`54%`):** Tên danh mục, Tiêu đề, Giá bán/Giá gốc, Mô tả chi tiết cuộn dọc, Cam kết kho hàng, và 2 nút **`[🛒 Thêm vào giỏ]`** + **`[⚡ Mua Ngay]`**. | - Mở cùng **Popup Xem Nhanh 2 Cột (`#quickViewModal`)**.<br>- **Cột Trái (`46%`):** Khung chính hiển thị Ảnh đại diện số 1 (`#qvMainImg`), thanh Thumbnail bên dưới chỉ hiển thị danh sách ảnh (`allImages`, không có ô `[▶ VIDEO]`).<br>- **Cột Phải (`54%`):** Giữ nguyên đầy đủ thông tin, mô tả cuộn dọc và 2 nút chốt đơn. |
| **Tầng 4: Trang Chi Tiết Sản Phẩm (`/san-pham/<slug>/`) & Hộp Ưu Đãi Khách Quay Lại** | - Khung Media chính (`.pd-image`) ưu tiên phát `<iframe id="pdVideo">` trước, kèm thanh `#pdThumbs` có ô **`[▶ VIDEO]`** đầu tiên + các ảnh `.pd-thumb-item`.<br>- Widget Khách Quay Lại tự động nhận diện sản phẩm có video và hiển thị nhãn **`• Có Video Test`** (`🎁 NHẬN VIDEO TEST & BẢNG GIÁ SỈ TẠI KHO`). | - Khung Media chính hiển thị `<img id="pdMainImg">` và thanh `#pdThumbs` chỉ liệt kê các ảnh sản phẩm. |

---

## 2. Triển Khai Tầng 1: Trường Nhập Video Sản Phẩm Trong WordPress / WooCommerce (`functions.php` & API Parser)

### 2.1. Tạo Ô Nhập Link Video Sản Phẩm Trong Trang Sửa Sản Phẩm WooCommerce (`functions.php`)

Đặt đoạn mã sau vào `wp-content/themes/flatsome-child/functions.php` để tạo trường nhập **`🎬 Link Video Sản Phẩm (YouTube / Shorts / MP4)`** ngay trong tab **Cài đặt chung (General)** của WooCommerce, đồng thời tự động bóc tách `youtube_id` kể cả khi quản trị viên dán link vào bài viết:

```php
<?php
/**
 * 1. Thêm trường nhập Video Sản Phẩm (_product_video_url) trong WooCommerce Product Data > General
 */
add_action( 'woocommerce_product_options_general_product_data', function() {
    echo '<div class="options_group">';
    woocommerce_wp_text_input( array(
        'id'          => '_product_video_url',
        'label'       => __( '🎬 Link Video Sản Phẩm (YouTube / Shorts)', 'flatsome-child' ),
        'placeholder' => 'https://www.youtube.com/watch?v=... hoặc https://youtube.com/shorts/...',
        'desc_tip'    => true,
        'description' => __( 'Nếu có nhập link video, thẻ sản phẩm sẽ hiện nút Play (▶) và khi click vào sẽ mở Popup Xem Nhanh phát trực tiếp video sản phẩm này.', 'flatsome-child' ),
    ) );
    echo '</div>';
} );

/**
 * 2. Lưu trường _product_video_url khi bấm Cập nhật sản phẩm
 */
add_action( 'woocommerce_process_product_meta', function( $post_id ) {
    if ( isset( $_POST['_product_video_url'] ) ) {
        $raw_video = sanitize_text_field( wp_unslash( $_POST['_product_video_url'] ) );
        update_post_meta( $post_id, '_product_video_url', $raw_video );
    }
} );

/**
 * 3. Hàm chuẩn hóa & trích xuất YouTube Video ID (11 ký tự) từ Custom Field hoặc Nội dung mô tả
 */
function nerhor_extract_product_youtube_id( $product_id, $description_html = '' ) {
    // Ưu tiên 1: Lấy từ trường nhập riêng _product_video_url (hoặc _wc_video_url / product_video)
    $candidates = array(
        get_post_meta( $product_id, '_product_video_url', true ),
        get_post_meta( $product_id, '_wc_video_url', true ),
        get_post_meta( $product_id, 'product_video_url', true ),
        $description_html,
    );

    $pattern = '/(?:youtube\.com\/(?:watch\?v=|embed\/|shorts\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})/i';
    foreach ( $candidates as $source_str ) {
        if ( ! empty( $source_str ) && is_string( $source_str ) ) {
            if ( preg_match( $pattern, $source_str, $matches ) ) {
                return $matches[1];
            }
            // Trường hợp người dùng nhập thẳng đúng 11 ký tự ID vào ô _product_video_url
            $trimmed = trim( $source_str );
            if ( preg_match( '/^[a-zA-Z0-9_-]{11}$/', $trimmed ) ) {
                return $trimmed;
            }
        }
    }
    return '';
}
```

---

## 3. Triển Khai Tầng 2 & Tầng 3: Thẻ Sản Phẩm Có Nút Play (`▶`) & Popup Xem Nhanh Có Video (`js/products.js`)

### 3.1. Render Thẻ Sản Phẩm (`Product Card`) Có Điều Kiện Theo `ytId`

Khi render danh sách sản phẩm, chuẩn hóa `ytId` từ `product.youtube_id` và chỉ hiển thị nút `.badge-video.quick-view-trigger` nếu `ytId` tồn tại:

```javascript
// Chuẩn hóa YouTube ID (hỗ trợ cả link đầy đủ hoặc ID 11 ký tự)
let ytId = (product.youtube_id || '').trim();
if (ytId.includes('v=')) {
  ytId = ytId.split('v=')[1].split('&')[0];
} else if (ytId.includes('youtu.be/')) {
  ytId = ytId.split('youtu.be/')[1].split('?')[0];
} else if (ytId.includes('/shorts/')) {
  ytId = ytId.split('/shorts/')[1].split(/[?&/]/)[0];
}

// Mẫu HTML Thẻ Sản Phẩm (Product Card)
const cardHtml = `
  <div class="product-card fade-in-up"
       data-id="${product.id}"
       data-name="${product.name.replace(/"/g, '&quot;')}"
       data-price="${displayPrice}"
       data-regularprice="${regularPrice}"
       data-saleprice="${salePrice}"
       data-image="${imgUrl}"
       data-permalink="${product.permalink}"
       data-slug="${product.slug || product.id}"
       data-youtube="${ytId}">

    <a href="/san-pham/${product.slug || product.id}/"
       class="product-card-image img-zoom-wrapper"
       style="position:relative;overflow:hidden;background:#111;aspect-ratio:1/1;display:block;">
      ${hasSale ? `<span class="badge badge-sale">-${discountPct}%</span>` : ''}

      ${ytId ? `
      <span class="badge-video quick-view-trigger" title="Xem video sản phẩm" style="
        position:absolute; top:50%; left:50%;
        transform: translate(-50%, -50%);
        width: 46px; height: 46px;
        background: rgba(0,0,0,0.65);
        border-radius: 50%; z-index: 3;
        display: flex; align-items: center; justify-content: center;
        cursor: pointer; border: 2px solid rgba(255,255,255,0.5);
        backdrop-filter: blur(4px); transition: all 0.22s ease;
        box-shadow: 0 2px 12px rgba(0,0,0,0.4);"
        onmouseover="this.style.transform='translate(-50%,-50%) scale(1.15)'; this.style.background='rgba(255,45,85,0.85)'; this.style.borderColor='#fff';"
        onmouseout="this.style.transform='translate(-50%,-50%) scale(1)'; this.style.background='rgba(0,0,0,0.65)'; this.style.borderColor='rgba(255,255,255,0.5)';">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="white" style="margin-left:2px">
          <path d="M8 5v14l11-7z"/>
        </svg>
      </span>` : ''}

      <img src="${imgUrl}" alt="${product.name}" loading="lazy"
           style="width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.3s ease;">
    </a>

    <div class="product-card-body">
      <a href="/san-pham/${product.slug || product.id}/" style="text-decoration:none;color:inherit;">
        <h3 class="product-card-title">${product.name}</h3>
      </a>
      ${priceHtml}
      <div class="product-card-actions mt-sm">
        <button class="btn btn-primary btn-buy btn-sm" style="flex:2;">Thêm vào giỏ</button>
        <button class="btn btn-outline btn-quick-view btn-sm" title="Xem nhanh video & chi tiết"
                style="flex:0 0 40px;padding:0;display:flex;align-items:center;justify-content:center;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
            <circle cx="12" cy="12" r="3"></circle>
          </svg>
        </button>
      </div>
    </div>
  </div>
`;
```

### 3.2. Bắt Sự Kiện Click Nút Play (`▶`) Hoặc Nút Con Mắt (`👁`) & Render Popup Xem Nhanh Có Video (`showQuickViewModal`)

- **Quy tắc bắt sự kiện:** Khi người dùng click vào `.btn-quick-view`, `.badge-video`, hoặc `.quick-view-trigger` bên trong `<a class="product-card-image">`, bắt buộc gọi `e.preventDefault(); e.stopPropagation();` để **không bị nhảy trang**, mà mở ngay `#quickViewModal`.
- **Quy tắc nhúng YouTube không lỗi (`youtube-nocookie.com`):** Luôn dùng `https://www.youtube-nocookie.com/embed/${ytId}?autoplay=1&mute=0&controls=1&rel=0&modestbranding=1&playsinline=1` để tránh lỗi chặn nhúng `Error 153` trên trình duyệt.
- **Quy tắc làm sạch URL video thô trong mô tả (`rawDesc`):** Trước khi đưa `product.description` vào cột phải của Popup, chạy Regex xóa bỏ mọi đường link YouTube thô và thẻ `<p></p>` rỗng để văn bản giới thiệu sản phẩm sạch đẹp.

```javascript
showQuickViewModal(product) {
  const oldModal = document.getElementById('quickViewModal');
  if (oldModal) oldModal.remove();

  const rp = parseFloat(product.price || product.regular_price || 0);
  const sp = parseFloat(product.sale_price || 0);
  const hasSale = sp > 0 && sp < rp;
  const displayPrice = hasSale ? sp : rp;
  const priceHtml = displayPrice > 0
    ? `<span style="color:#ff4444;font-size:26px;font-weight:800;">${this.formatPrice(displayPrice)}</span>`
      + (hasSale
        ? ` <span style="text-decoration:line-through;color:rgba(255,255,255,0.4);font-size:13px;">${this.formatPrice(rp)}</span>
           <span style="background:linear-gradient(135deg,#ff4444,#ff6b35);color:#fff;font-size:11px;font-weight:700;padding:2px 8px;border-radius:20px;margin-left:6px;">-${Math.round((1-sp/rp)*100)}%</span>`
        : '')
    : '<span style="color:#00c8ff;font-size:22px;font-weight:800;">Liên hệ</span>';

  const ytId = (product.youtube_id || '').trim();
  const hasVid = Boolean(ytId && ytId !== 'undefined' && ytId.length === 11);
  const allImages = (product.images && product.images.length > 0) ? product.images : [product.image];

  // Thanh Thumbnail bên dưới: Nếu có video -> hiện ô [▶ VIDEO] đầu tiên (viền #00c8ff) + danh sách ảnh
  const thumbsHtml = `
    <div id="qvThumbs" style="display:flex;gap:6px;padding:8px;overflow-x:auto;flex-shrink:0;background:rgba(0,0,0,0.6);">
      ${hasVid ? `
      <div class="qv-thumb qv-thumb-video" data-type="video" title="Xem video"
           style="flex:0 0 68px;height:52px;border-radius:6px;background:#0a0a0a;border:2px solid #00c8ff;
                  cursor:pointer;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:2px;">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="#00c8ff"><path d="M8 5v14l11-7z"/></svg>
        <span style="color:#00c8ff;font-size:9px;font-weight:700;">VIDEO</span>
      </div>` : ''}
      ${allImages.map((src, i) => `
      <div class="qv-thumb" data-type="image" data-src="${src}" data-idx="${i}"
           style="flex:0 0 68px;height:52px;border-radius:6px;overflow:hidden;cursor:pointer;
                  border:2px solid ${i === 0 && !hasVid ? '#00c8ff' : 'rgba(255,255,255,0.15)'};">
        <img src="${src}" alt="Ảnh ${i + 1}" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;">
      </div>`).join('')}
    </div>`;

  // Lọc bỏ link YouTube thô trong mô tả để cột phải hiển thị sạch đẹp
  let rawDesc = (product.description || '').trim();
  rawDesc = rawDesc.replace(/(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/|shorts\/)|youtu\.be\/)[a-zA-Z0-9_-]{11}[^\s<"]*/gi, '');
  rawDesc = rawDesc.replace(/<p[^>]*>\s*(&nbsp;|\xa0|\u00a0)?\s*<\/p>/gi, '').trim();
  const descContent = rawDesc || 'Sản phẩm chính hãng chất lượng cao. Liên hệ để biết thêm chi tiết.';

  const modalHTML = `
    <div id="quickViewModal" style="position:fixed;inset:0;z-index:999999;background:rgba(0,0,0,0.88);backdrop-filter:blur(12px);display:flex;align-items:center;justify-content:center;padding:12px;box-sizing:border-box;">
      <div style="position:relative;display:flex;flex-direction:row;width:100%;max-width:980px;height:min(90vh,660px);background:#111827;border:1px solid rgba(255,255,255,0.12);border-radius:16px;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,0.8);">
        <button id="btnCloseQuickView" style="position:absolute;top:12px;right:12px;z-index:100;width:34px;height:34px;border-radius:50%;background:#ff4444;border:2px solid #fff;color:#fff;font-size:15px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;">&#10005;</button>

        <!-- CỘT TRÁI (46%): Khung Video / Ảnh + Thanh Thumbnail -->
        <div style="flex:0 0 46%;display:flex;flex-direction:column;background:#000;overflow:hidden;">
          <div id="qvMainMedia" style="flex:1;position:relative;background:#000;overflow:hidden;">
            ${hasVid ? `
            <iframe id="qvVid"
              src="https://www.youtube-nocookie.com/embed/${ytId}?autoplay=1&mute=0&controls=1&rel=0&modestbranding=1&playsinline=1"
              frameborder="0" allow="autoplay; encrypted-media; fullscreen; picture-in-picture" allowfullscreen
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:none;"></iframe>` : ''}
            <img id="qvMainImg" src="${allImages[0]}" alt="${product.name}"
              style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:contain;display:${hasVid ? 'none' : 'block'};background:#000;">
          </div>
          ${thumbsHtml}
        </div>

        <!-- CỘT PHẢI (54%): Thông tin, Mô tả cuộn dọc & 2 Nút Hành Động -->
        <div style="flex:1;display:flex;flex-direction:column;padding:24px 22px 20px;overflow:hidden;min-height:0;box-sizing:border-box;">
          <div style="color:#189eff;font-size:11px;text-transform:uppercase;font-weight:700;letter-spacing:1.2px;margin-bottom:8px;">SẢN PHẨM</div>
          <h2 style="margin:0 0 14px;font-size:clamp(15px,1.6vw,21px);font-weight:800;color:#fff;line-height:1.35;">${product.name}</h2>
          <div style="display:flex;align-items:center;flex-wrap:wrap;gap:8px;padding-bottom:14px;border-bottom:1px solid rgba(255,255,255,0.1);margin-bottom:14px;">${priceHtml}</div>
          <div style="flex:1;overflow-y:auto;min-height:0;color:rgba(255,255,255,0.85);font-size:13.5px;line-height:1.7;padding-right:6px;margin-bottom:14px;">
            ${descContent}
          </div>
          <div style="flex-shrink:0;display:flex;gap:10px;padding-top:14px;border-top:1px solid rgba(255,255,255,0.1);">
            <button class="btn-qv-add" style="flex:1;padding:12px 8px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.3);color:#fff;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer;">&#128722; Thêm vào giỏ</button>
            <button class="btn-qv-buy" style="flex:1.4;padding:12px 8px;background:linear-gradient(135deg,#00c8ff,#0060ff);border:none;color:#fff;border-radius:8px;font-size:14px;font-weight:700;cursor:pointer;box-shadow:0 4px 16px rgba(0,200,255,0.4);">&#9889; Mua Ngay</button>
          </div>
        </div>
      </div>
    </div>`;

  document.body.insertAdjacentHTML('beforeend', modalHTML);
  document.body.style.overflow = 'hidden';

  const modal = document.getElementById('quickViewModal');
  const qvVid = document.getElementById('qvVid');
  const qvImg = document.getElementById('qvMainImg');
  const closeModal = () => { modal.remove(); document.body.style.overflow = ''; };

  document.getElementById('btnCloseQuickView').addEventListener('click', closeModal);
  modal.addEventListener('click', e => { if (e.target === modal) closeModal(); });

  // Chuyển đổi qua lại giữa [▶ VIDEO] và [Ảnh 1..N] trong Popup
  const thumbs = modal.querySelectorAll('.qv-thumb');
  thumbs.forEach(thumb => {
    thumb.addEventListener('click', () => {
      thumbs.forEach(t => t.style.borderColor = 'rgba(255,255,255,0.15)');
      thumb.style.borderColor = '#00c8ff';
      if (thumb.dataset.type === 'video' && qvVid) {
        qvVid.style.display = 'block';
        qvVid.src = `https://www.youtube-nocookie.com/embed/${ytId}?autoplay=1&mute=0&controls=1&rel=0&modestbranding=1&playsinline=1`;
        if (qvImg) qvImg.style.display = 'none';
      } else if (thumb.dataset.type === 'image') {
        if (qvVid) { qvVid.style.display = 'none'; qvVid.src = ''; }
        if (qvImg) { qvImg.src = thumb.dataset.src; qvImg.style.display = 'block'; }
      }
    });
  });
}
```

---

## 4. Triển Khai Tầng 4: Trang Chi Tiết Sản Phẩm (`/san-pham/<slug>/`) Đồng Bộ Trình Phát Video + Thumbnail Strip (`#pdVideo` & `#pdThumbs`)

Trên trang chi tiết sản phẩm (ví dụ `https://densankhauhcm.com/san-pham/den-moving-200w-chieu-quan-karaoke/`), bố cục cột trái (`.pd-image` + `#pdThumbs`) áp dụng đúng cơ chế ưu tiên phát Video trước (nếu sản phẩm có `ytId`), cho phép người mua chuyển đổi tức thì giữa `[▶ VIDEO]` và các ảnh chụp chi tiết:

```html
<!-- CỘT TRÁI TRANG CHI TIẾT SẢN PHẨM: Video/Ảnh chính + Thanh Thumbnail -->
<div style="display:flex;flex-direction:column;gap:10px;min-width:0;">
  <div class="pd-image" style="position:relative;aspect-ratio:1/1;background:#0a0a0a;border-radius:12px;overflow:hidden;">
    <!-- Nếu có ytId: hiển thị iframe #pdVideo ngay khi mở trang -->
    <iframe id="pdVideo"
      src="https://www.youtube-nocookie.com/embed/yHOt-VyKkHo?autoplay=1&mute=0&controls=1&rel=0&modestbranding=1"
      frameborder="0"
      allow="autoplay; encrypted-media; fullscreen"
      allowfullscreen
      style="position:absolute;top:0;left:0;width:100%;height:100%;border:none;border-radius:12px;"></iframe>
    <img id="pdMainImg"
      src="https://densankhauhcm.com/systemweb/wp-content/uploads/2026/11/densankhauhcm-com-43.png"
      alt="Tên sản phẩm"
      style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:contain;display:none;border-radius:12px;background:#0a0a0a;">
  </div>

  <!-- Thanh Thumbnail chuyển đổi Video <-> Ảnh -->
  <div id="pdThumbs" style="display:flex;gap:8px;padding:6px 2px;overflow-x:auto;">
    <div class="pd-thumb-item" data-type="video" title="Xem video"
         style="flex:0 0 80px;height:62px;border-radius:8px;background:#0d0d0d;border:2px solid #00c8ff;
                cursor:pointer;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:4px;">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="#00c8ff"><path d="M8 5v14l11-7z"/></svg>
      <span style="color:#00c8ff;font-size:9px;font-weight:700;letter-spacing:0.5px;">VIDEO</span>
    </div>
    <div class="pd-thumb-item" data-type="image"
         data-src="https://densankhauhcm.com/systemweb/wp-content/uploads/2026/11/densankhauhcm-com-43.png"
         style="flex:0 0 80px;height:62px;border-radius:8px;overflow:hidden;cursor:pointer;border:2px solid rgba(255,255,255,0.15);">
      <img src="https://densankhauhcm.com/systemweb/wp-content/uploads/2026/11/densankhauhcm-com-43.png" alt="Ảnh 1"
           style="width:100%;height:100%;object-fit:cover;display:block;">
    </div>
  </div>
</div>
```

---

## 5. Checklist Nghiệm Thu Tính Năng Video Sản Phẩm & Popup Xem Nhanh (`QA Gate`)

1. **Kiểm tra sản phẩm CÓ nhập video:**
   - [ ] Ngoài trang chủ / danh mục: Thẻ sản phẩm có hiện nút tròn `▶` (`.badge-video`) ở chính giữa ảnh đại diện.
   - [ ] Khi click vào nút `▶` hoặc nút con mắt `👁` (`.btn-quick-view`): Không bị nhảy trang, bật ngay `#quickViewModal`, khung bên trái tự động phát video sản phẩm (`youtube-nocookie.com/embed/...`) và thanh thumbnail bên dưới có ô `[▶ VIDEO]` sáng viền xanh `#00c8ff`.
   - [ ] Khi click sang thumbnail ảnh kế bên trong Popup: Video tự động dừng phát (ngắt tiếng hoàn toàn `qvVid.src = ''`) và hiển thị ảnh sản phẩm. Click lại ô `[▶ VIDEO]` thì phát lại video.
   - [ ] Cột bên phải trong Popup: Không còn dính đường link YouTube thô trong đoạn văn mô tả; cuộn đọc mượt; bấm `Thêm vào giỏ` hoặc `Mua Ngay` hoạt động chính xác.
2. **Kiểm tra sản phẩm KHÔNG nhập video:**
   - [ ] Ngoài thẻ sản phẩm: Không hiện nút `▶` giữa ảnh.
   - [ ] Khi click nút con mắt `👁`: Mở `#quickViewModal` hiển thị ảnh đại diện và danh sách thumbnail ảnh bình thường, không bị khung đen rỗng.
