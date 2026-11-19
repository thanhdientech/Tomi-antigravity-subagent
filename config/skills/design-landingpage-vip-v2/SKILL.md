---
name: design-landingpage-vip-v2
description: "Thiết kế Landing Page VIP 1 file HTML hoàn chỉnh: Liquid Glass, 138 icon SVG, form, thanh toán VietQR & Meta/TikTok CAPI."
group: "Marketing, Web & SEO"
---

# design-landingpage-vip-v2 — Landing Page VIP của GĐT / Noti.vn

<!-- JAVIS_TRIGGER_ARCHIVE_START -->
## Khi nào dùng (Triggers & Ngữ cảnh kích hoạt đầy đủ)

> Skill thiết kế landing page Noti.vn/GĐT — 1 file HTML hoàn chỉnh, chọn design system từ template trong system-design/ (mặc định noti-vn liquid glass) hoặc tự nhập. Có form đăng ký + countdown + FAQ + thanh toán QR VietQR + Meta CAPI/TikTok Events API 2.0/dual-tracking qua backend webhook (KHÔNG gọi CAPI từ frontend). 138 icon SVG inline từ assets/icons/ (6 category ui/commerce/trust/contact/feature/payments), 100% tiếng Việt có dấu. TRIGGERS: landing page VIP, LP VIP, landing page Noti, landing page GĐT, landing có CAPI, Meta CAPI, TikTok CAPI, dual tracking, landing page sự kiện, landing page khóa học, landing page đăng ký, form thanh toán VietQR, landing page có QR, event landing, meetup landing. Trigger cả khi user chỉ nói làm landing page hoặc landing có form + thanh toán.
<!-- JAVIS_TRIGGER_ARCHIVE_END -->

- **Nguồn gốc / Kho Git Upstream:** [noti-vn/design-landingpage-vip (Liquid Glass & CAPI)](https://github.com/noti-vn/design-landingpage-vip) (`Design System Nội Bộ VIP`)

> **Last updated:** 2026-05-29 (v2.44) — lịch sử thay đổi đầy đủ ở `changelog.md`.
>
> **QUY TẮC**: Mỗi lần Claude sửa bất kỳ file nào trong skill này (SKILL.md, references/*.md, system-design/**), BẮT BUỘC: (1) cập nhật dòng `Last updated` ở trên thành ngày hiện tại + bump version (v2.4 -> v2.5...); (2) thêm 1 mục changelog mới vào ĐẦU file `changelog.md`. KHÔNG ghi changelog trực tiếp vào SKILL.md — để SKILL.md gọn gàng.

> **Marketing & USP (meta-doc, KHÔNG load mặc định)**: Khi và CHỈ KHI user hỏi "skill này là gì", "USP của skill", "skill giải quyết vấn đề gì", "khách hàng phù hợp", "ROI", hoặc cần viết pitch deck / sales page / description giới thiệu skill cho team/khách hàng → đọc `_POSITIONING.md` (file cùng cấp với SKILL.md, prefix `_` báo hiệu non-functional doc). File đó có: bản chất skill, 5 nhóm vấn đề doanh nghiệp giải quyết, 10 USP, bảng ROI trước/sau, 6 nhóm khách hàng mục tiêu, 10 use case cụ thể, tech stack tóm tắt. **KHÔNG đọc file này khi build LP** — chỉ phục vụ tài liệu giới thiệu skill.

Skill này dùng để **build landing page hoàn chỉnh** theo đúng phong cách đặc trưng của user hoặc theo template có sẵn: design system liquid-glass-AI-tech + form đăng ký có thu thập đủ dữ liệu cho **Meta CAPI và/hoặc TikTok Events API 2.0** (nhưng **KHÔNG gọi CAPI từ frontend** — backend của user sẽ tự làm). Hỗ trợ 3 cấu hình: Meta-only, TikTok-only, hoặc Dual-tracking (cả 2 cùng lúc, share event_id để dedup).

## Nguyên tắc bất biến (đọc kỹ trước khi viết code)

1. **100% tiếng Việt có dấu** cho mọi văn bản hiển thị cho user (heading, body, button, CONFIG_REQUIRED, error message, FAQ, footer). Không được viết "Dang ky", "Dong y" — phải là "Đăng ký", "Đồng ý". Chỉ tên biến JS/CSS và nội dung chuyển khoản mới dùng không dấu.
2. **KHÔNG BAO GIỜ** đặt access token của Meta CAPI hoặc TikTok Events API, pixel secret, hay bất kỳ credential nào vào frontend. KHÔNG gọi `https://graph.facebook.com/.../events` hay `https://business-api.tiktok.com/open_api/v1.3/event/track/` từ client. Lý do: token sẽ bị lộ 100% nếu đặt trong HTML/JS.
3. **Flow tracking chuẩn (áp dụng cho cả Meta và TikTok)**:
   - Frontend **chỉ** gọi `fbq('track', ...)` (Meta Pixel) và/hoặc `ttq.track(...)` (TikTok Pixel) browser-side.
   - Khi submit form, frontend thu thập tracking data tương ứng với platform user chọn:
     - **Meta**: `fbc`, `fbp`, `client_user_agent`, `client_ip_address`, `event_source_url`, `fbclid`
     - **TikTok**: `ttclid`, `ttp`, `client_user_agent`, `client_ip_address`, `page_url`, `page_referrer`
     - **Chung 2 bên**: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`, `ref`, `event_id`, `event_time`
   - IP lấy qua Cloudflare trace + fallback ipify/ipinfo; có `waitForIP` (Meta) / `waitForTracking` (TikTok & dual - chờ thêm cookie `_ttp`) chờ resolve trước khi submit.
   - POST payload lên **webhook backend của user**. Backend tự gọi Meta CAPI và/hoặc TikTok Events API → tự hash email/phone (SHA-256) → tự dedup bằng `event_id` trùng với Pixel.
   - Trong code frontend phải có comment rõ: `// KHÔNG gọi CAPI ở đây — backend tự xử lý qua webhook`.
   - **Dùng 1 endpoint duy nhất cho cả 2 luồng**: đăng ký và kiểm tra thanh toán cùng POST về 1 URL (ví dụ `WEBHOOK_URL = 'https://YOUR-BACKEND/webhook-landing'`). Phân luồng bằng field `event` trong payload: `"event": "lead"` khi user gửi đăng ký, `"event": "check_pay"` khi user bấm kiểm tra thanh toán. Backend đọc `event` để chọn nhánh xử lý. **KHÔNG** được dùng 2 URL khác nhau hay phương thức GET cho check payment.
   - **Khi dual-tracking (Meta + TikTok)**: 1 form duy nhất, 1 webhook duy nhất, payload chứa CẢ Meta fields + TikTok fields, fire CẢ `fbq()` và `ttq.track()` với CÙNG `event_id` để backend dedup cả 2 phía.
4. **Không tự ý gửi dữ liệu khi user đang gõ/điền**. Chỉ gửi lên webhook **sau khi** user nhấn nút Submit và pass validation + honeypot.
5. **Honeypot bắt buộc**: thêm field `website` ẩn với `aria-hidden="true"` và `tabindex="-1"`. Nếu có giá trị → bỏ qua request (bot filter).
6. **Dedup eventID**: event_id ở Pixel (browser) phải giống event_id gửi lên webhook để backend dedup với CAPI.
7. **Không thêm border-line viền rõ** cho glass card — chỉ dùng `box-shadow` inset + outer để tạo mép kính. `border: none` là mặc định.
8. **KHÔNG dùng bất kỳ đường line nào ở các khối** — không `border` viền card/section/panel, không `::before` gradient bar trên đầu khối, không `border-top`/`border-bottom` làm đường kẻ ngăn (kể cả divider giữa các dòng trong khối như `.bank-info-row`). Tách phần tử bằng khoảng cách (padding/margin/gap) hoặc nền (background), KHÔNG bằng đường kẻ. Ngoại lệ DUY NHẤT: ô `input`/`select` trong form giữ `border` mảnh vì cần ranh giới vùng nhập rõ ràng.
9. **Tách từ bằng dấu `-` (ASCII), không dùng `—` (em-dash)** và **dùng `->` thay cho `→`** trong mọi văn bản hiển thị (heading, body, button, bank-info value, transferContent, console log…). Lý do: user GĐT yêu cầu thống nhất kiểu chữ ASCII gọn gàng, dễ copy-paste, không lệch font giữa các OS.
10. **Responsive**: media query tại 1024px (tablet ngang), 768px (tablet dọc) và 480px (mobile) cho blob, grid, hero, form, typography, nav menu.
11. **Header BẮT BUỘC có nav menu + hamburger drawer mobile** — markup + CSS + JS đầy đủ ở `references/sections-core.md` mục 5 (Header navigation + Mobile drawer). Không được làm header chỉ có logo + 1 nút CTA.
12. **Footer BẮT BUỘC link tới các trang chính sách TỰ SINH** (KHÔNG dùng URL cố định noti.vn nữa): Chính sách bảo mật + Điều khoản dịch vụ cho MỌI LP; thêm Chính sách thanh toán nếu LP có thanh toán QR. Skill tự sinh các trang này thành file HTML riêng, nội dung khớp nội dung LP — footer link tương đối (`chinh-sach-bao-mat.html`, `dieu-khoan-su-dung.html`, `chinh-sach-thanh-toan.html`). Xem mục "Trang chính sách tự sinh" và `references/policy-pages.md`.
13. **Mọi card/section liệt kê có STT (pain points, pillars, formulas, steps, features đánh số) BẮT BUỘC dùng badge nổi bật gradient** - không để số trần dạng text nhạt. 3 kiểu chuẩn: (a) `.card-number` - badge tròn 44px gradient góc phải trên card, chữ trắng 800-weight, shadow `0 6px 16px rgba(0,97,255,.3)`; (b) `.pillar-badge` - pill gradient nổi lên trên viền card (`top:-18px`), chữ "TRỤ CỘT 01/02/03" hoặc "BƯỚC 01"...; (c) `.formula-num` pill - gradient pill đè viền trên card (`top:-14px;left:1.5rem`), chữ 800-weight letter-spacing 1.5px. Khi h3 cùng dòng với `.card-number` góc phải, BẮT BUỘC `padding-right:3rem` trên h3 để chữ không đè badge. Mobile `≤768px` scale badge xuống 38px.
14. **Form section - tiêu đề trong card BẮT BUỘC căn giữa**: `.form-title{text-align:center}` cho state đăng ký; `.payment-qr>h3, .payment-qr>p{text-align:center}` cho state hiện QR; `.payment-confirmed` đã center mặc định. Lý do: form-container đã max-width 600px - tiêu đề căn giữa cân đối với QR + bank-info bên dưới. KHÔNG để tiêu đề form text-align:left khi content bên dưới là QR hoặc icon center.
15. **Icon BẮT BUỘC dùng SVG inline từ `assets/icons/`** — KHÔNG dùng emoji (✓, ✗, ☆, 📞, 📍, 🎁…), KHÔNG dùng icon font (Font Awesome / Material Icons / Bootstrap Icons), KHÔNG dùng `<img src="...svg">`. Mọi icon trên LP đều paste inline SVG từ thư mục `assets/icons/<category>/<category>-<name>.svg` (**6 category**: `ui`, `commerce`, `trust`, `contact`, `feature`, `payments`). 5 category đầu giữ `stroke="currentColor"` (stroke 1.75) để đổi màu qua CSS. Riêng category `payments/` (brand payment logos — Visa/Mastercard/ATM/Apple Pay) là **ngoại lệ**: giữ brand colors hard-coded + rectangular viewBox để đảm bảo nhận diện logo. Nếu không có icon phù hợp trong manifest → ƯU TIÊN tạo file SVG mới trong folder category đúng + cập nhật `assets/icons/README.md`; KHÔNG được inline icon "tự vẽ" trực tiếp trong LP. Đọc `assets/icons/README.md` trước khi build LP để biết toàn bộ 138 icon đang có + naming convention + size/CSS pattern + 2 ngoại lệ (filled variant + payments brand logos).

> **Phạm vi nguyên tắc design:** #7, #8, #13 mô tả phong cách template phong cách glass (noti-vn). Template có `design-system.md` khác (ví dụ `shopee`, `tiktok-shop`, `apple`, `shopify`, `hasaki-vn`, `tgdd`, `coolmate`, `long-form` — flat, không gradient, không glass; dùng viền mảnh / đổi màu nền để tách khối) thì tuân theo `design-system.md` của template đó. Các nguyên tắc còn lại (#1-6, #9-12, #14, #15) áp dụng cho MỌI template.

## Quy trình làm việc — 8 bước tuần tự

> **Quan trọng về `AskUserQuestion`**: tool này có hard-limit **1-4 câu / batch**, mỗi câu **2-4 options multi-choice**. Câu free-text (URL, Pixel ID, BANK/STK, tên doanh nghiệp…) KHÔNG dùng `AskUserQuestion` — hỏi qua chat thông thường ở Bước 4.

### Bước 1 — Phân tích brief, infer những gì rõ

Đọc message của user và TRƯỚC HẾT suy luận các thông tin đã có:

- **Style/template**: nếu user nói "kiểu Apple" → `apple`; "kiểu Shopee" → `shopee`; "phong cách Noti / GĐT" hoặc không nói gì → `noti-vn` (mặc định); "trang bán hàng dài" → `long-form`…
- **Loại LP**: event/khóa học/SaaS launch/ebook → để định hình section default (header/hero/stats/agenda/speaker/CTA…)
- **Có thanh toán hay chỉ thu lead**: nếu user mention "thu tiền", "VietQR", "đăng ký có phí" → có QR; ngược lại → lead-only

Cái gì rõ rồi thì KHÔNG hỏi lại. Chỉ hỏi cái thực sự ambiguous.

### Bước 2 — Batch 1 `AskUserQuestion` (4 quyết định ARCHITECTURE)

Gom vào **1 batch duy nhất** (≤4 câu multi-choice):

1. **CAPI platform** (2-3 options): `Meta (Facebook/Instagram)` / `TikTok` / `Cả hai (dual-tracking dedup event_id)`
2. **Storage destination** (2 options): `Webhook backend (default — hỗ trợ CAPI server-side + check_pay)` / `Google Sheet dùng script (CHỈ lead, không CAPI server-side, không QR)`
3. **Có thanh toán QR không?** (2 options): `Có` / `Không (chỉ thu lead)` — **nếu Storage = Google Sheet ở câu 2, force option duy nhất = Không**
4. **Trường form custom** (multi-select 2-4 options): mặc định là `họ tên + email + SĐT`; user multi-select thêm `Địa chỉ` / `Tỉnh thành` / `Ghi chú` / `Dropdown phân loại`

**Validation sau batch**:
- Nếu Storage = Google Sheet + Có QR → STOP, gửi 1 message giải thích quy tắc loại trừ + re-ask batch (chỉ 2 câu: đổi storage hay bỏ QR).

### Bước 3 — Batch 2 `AskUserQuestion` (chỉ khi cần — Design system)

Hỏi 1 câu MÀ THÔI nếu Bước 1 không infer được template:

- **Design system** (3-4 options): `noti-vn (default — liquid glass)` / `Template e-commerce phẳng (shopee/tiktok-shop/hasaki-vn/tgdd/coolmate)` / `Template premium (apple/shopify)` / `Tự nhập design system`

Nếu user chọn group e-commerce/premium → ask follow-up text (qua chat) để chọn template cụ thể.

Nếu user chọn `Tự nhập` → gửi gợi ý extension Noti (xem mục "Design system → Bước 1 → lựa chọn 2").

Nếu Bước 1 đã infer rõ template → BỎ QUA Bước 3.

### Bước 4 — Hỏi free-text qua chat (không dùng `AskUserQuestion`)

Đây là các giá trị TEXT/CONFIG, không phù hợp multi-choice. Gom 1 message chat duy nhất:

```
Để mình bắt đầu build, gửi mình mấy thông tin sau:

1. URL endpoint webhook (vd `https://noti.vn/api/landing-hook`) hoặc URL Google Apps Script Web App. Nếu chưa có, mình để CONFIG_REQUIRED.

2. Pixel ID:
   - Meta Pixel ID (nếu chọn Meta hoặc Cả hai)
   - TikTok Pixel Code dạng `C12ABC...` (nếu chọn TikTok hoặc Cả hai)
   - Nếu chưa có, ghi "chưa có" → mình để 'YOUR_PIXEL_ID'

3. [CHỈ KHI CÓ QR] Thông tin VietQR (5 trường):
   - BANK (mã ngân hàng: MB / VCB / TCB / ACB / BIDV / TPB / VPB…)
   - STK (số tài khoản)
   - ACCOUNT_NAME (tên người nhận VIẾT HOA KHÔNG DẤU)
   - AMOUNT (số tiền VNĐ)
   - PREFIX (prefix nội dung CK — DK / CAFE / COURSE…)
   - Cấu trúc Response check_pay của backend (mặc định `{"status":"pending"|"success"}` — gửi 1 ví dụ JSON nếu khác)

4. Thông tin cho trang chính sách + header LP:
   - Tên doanh nghiệp / thương hiệu
   - Email liên hệ
   - SĐT liên hệ
   - Logo + favicon - chọn 1 trong 3 mode:
     a) Có 2 ảnh riêng (light + dark): gửi 2 URL + favicon URL
     b) Có 1 ảnh dùng chung: gửi 1 URL logo + favicon URL
     c) Chưa có ảnh: text-only logo (in tên thương hiệu, favicon SVG inline ký tự đầu trên gradient)
   - **KHÔNG fallback bằng logo Noti.vn / brand khác** - nếu không cung cấp = mặc định Mode C text-only

5. [Optional] Ngày/giờ sự kiện cho countdown (nếu là event landing).
```

KHÔNG hỏi lẻ từng cái — gom thành 1 message. Cái nào user trả lời "chưa có" → để CONFIG_REQUIRED + đánh dấu CONFIG_REQUIRED trong code.

### Bước 5 — Đọc reference + assets theo lựa chọn

| Điều kiện | File phải đọc |
|---|---|
| Mọi LP | `assets/icons/README.md` (manifest 138 icon + cách dùng inline SVG) |
| Mọi LP | `references/sections-core.md` (markup CORE: hero/FAQ/CTA/footer/header+drawer/features/button) |
| LP có section nâng cao (stats/countdown/video/pricing/before-after/numbered badges/form QR) | `references/sections-advanced.md` (load on-demand) |
| Mọi LP | `references/policy-pages.md` (sinh chính sách bảo mật/điều khoản/thanh toán) |
| Mọi LP có form (CAPI bất kỳ) | `references/_utils.md` (4 block JS dùng chung: cookie helper, IP fetch, removeDiacritics/generateCode, validateField — paste TRƯỚC platform helpers) |
| CAPI = Meta | `references/form-meta-capi.md` |
| CAPI = TikTok | `references/form-tiktok-capi.md` |
| CAPI = Cả hai | `references/form-capi-dual.md` |
| Storage = Webhook | (default — không cần file thêm) |
| Storage = Google Sheet | `references/storage-google-sheet.md` (BẮT BUỘC) |
| Có thanh toán QR | `references/payment-qr.md` + `references/backend-security.md` (lookup `(phone, code)` ngầm cho check_pay) |
| Có custom form fields | `references/form-fields.md` (markup + validateField + 18 ID JS-critical) |
| Storage = Webhook (kèm reminder bàn giao) | `references/backend-security.md` (10 checklist backend) |

Cũng đọc 3 file của template đã chọn: `system-design/<template>/design-system.md` + `starter-template.html` + `form-snippet.html`.

### Bước 6 — Build LP file (1 HTML duy nhất)

Workflow viết code:

1. **Copy `starter-template.html`** của template làm base
2. **Thêm Pixel snippet** vào `<head>` (Meta `fbq()` / TikTok `ttq.track()` / cả 2)
3. **Thêm JS tracking helpers** từ reference file (`getFbc/getFbp`, `getTtclid/getTtp`, `waitForIP/waitForTracking`, submit handler `lead`)
4. **Cấu hình `WEBHOOK_URL`** (top-level — KHÔNG lồng trong submit handler, tránh ReferenceError ở handler `check_pay`) + Content-Type (`application/json` cho Webhook, `text/plain;charset=utf-8` cho GAS — né CORS preflight)
5. **Thay nội dung sections** theo brief — header / hero / stats / features / speaker / agenda / testimonials / FAQ / CTA cuối / footer (default 7-8 section)
6. **Mở rộng form** nếu Bước 2 câu 4 có custom field — thêm tại vùng `[CUSTOM-FIELDS]` comment, đúng contract `references/form-fields.md`
7. **Thêm Payment QR block** nếu có QR — load `showPaymentQR()` + handler `check_pay` từ `references/payment-qr.md`
8. **Paste icon inline** từ `assets/icons/` cho mọi icon trên LP (bullet check, trust banner, contact phone/zalo, feature card…) — KHÔNG emoji, KHÔNG icon font, KHÔNG `<img src=...svg>`
9. **Footer link tương đối** tới 3 trang chính sách: `chinh-sach-bao-mat.html` / `dieu-khoan-su-dung.html` / `chinh-sach-thanh-toan.html` (nếu có QR)

### Bước 7 — Sinh 2-3 trang chính sách (file HTML riêng)

Theo `references/policy-pages.md`:

- `chinh-sach-bao-mat.html` (mọi LP) — khai báo ĐÚNG tracking đang dùng + liệt kê đầy đủ bên thứ 3 (Cloudflare/ipify cho IP, Google nếu GAS, Meta/TikTok cho CAPI, VietQR Solution cho ảnh QR)
- `dieu-khoan-su-dung.html` (mọi LP)
- `chinh-sach-thanh-toan.html` (chỉ LP có QR)

Cùng thư mục output với LP. Footer LP đã link tương đối tới.

### Bước 8 — Bàn giao + nhắc check

Khi giao file BẮT BUỘC nhắc user:

- Thay `WEBHOOK_URL` thực tế (nếu để CONFIG_REQUIRED)
- Thay Pixel ID thực (nếu để `YOUR_PIXEL_ID`)
- **Backend BẮT BUỘC triển khai `references/backend-security.md`** (10 checklist: dedup `event_id` UNIQUE, lookup `(phone, code)` ngầm cho check_pay, hash email/phone SHA-256, rate-limit IP+phone, honeypot defense-in-depth…)
- Rà soát nội dung chính sách cho khớp doanh nghiệp + nhờ luật sư check (Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân)
- Nếu Storage = Google Sheet: nhắc user 2 hạn chế (không CAPI server-side, không hỗ trợ QR)

---

**Quy tắc loại trừ Google Sheet + thanh toán QR**: kiểm tra trong Bước 2 (validation sau batch). Storage = GAS thì câu 3 "Có QR?" chỉ được phép = "Không" — vì `check_pay` cần backend lookup trạng thái theo phone+code (ideally tích hợp API NH như Casso/SePay), GAS không phù hợp (latency, quota, không có job polling NH).

---

> 📖 **Chi tiết đầy đủ:** Xem [DETAIL.md](./references/DETAIL.md) — chứa bảng tra cứu, checklist và ví dụ mở rộng.
