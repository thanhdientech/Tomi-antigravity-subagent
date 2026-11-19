# 🤖 Giải Thích Từng Model Trong Antigravity

> Dựa trên ảnh anh chụp — 9 model đang có, chia làm 3 nhóm chính

---

## 🟢 NHÓM 1 — GEMINI 4 (Google DeepMind — Mới nhất Nov 2026)

### 1. Gemini 4 Carbon `Medium` `New`
| | |
|---|---|
| **Hãng** | Google DeepMind |
| **Sức mạnh** | Mạnh nhất trong 3 Gemini 4 — tương đương "flagship" |
| **Tốc độ** | Medium (không nhanh như Flash, không chậm như Opus) |
| **Điểm mạnh** | Code phức tạp, reasoning sâu, multi-step logic, hiểu context dài |
| **Điểm yếu** | Tốn quota hơn Flash |
| **Dùng khi** | ERP/SAP SQL phức tạp, viết code lớn, phân tích dữ liệu, tác vụ cần chính xác cao |

---

### 2. Gemini 4 Argon `Medium` `New`
| | |
|---|---|
| **Hãng** | Google DeepMind |
| **Sức mạnh** | Cân bằng giữa Carbon và Hydrogen — "mid-tier flagship" |
| **Tốc độ** | Medium |
| **Điểm mạnh** | Đa năng: code, viết content, phân tích, hội thoại — làm tốt tất cả |
| **Điểm yếu** | Không chuyên sâu bằng Carbon ở task thuần lý luận |
| **Dùng khi** | Tác vụ hằng ngày: viết content, thiết kế LP, marketing, hỏi đáp nhanh |

---

### 3. Gemini 4 Hydrogen `Medium` `New`
| | |
|---|---|
| **Hãng** | Google DeepMind |
| **Sức mạnh** | Nhẹ nhất trong 3 Gemini 4 — "efficient tier" |
| **Tốc độ** | Medium nhưng nhẹ hơn Carbon/Argon |
| **Điểm mạnh** | Tiết kiệm quota nhất trong nhóm Gemini 4, vẫn dùng được tốt |
| **Điểm yếu** | Reasoning phức tạp không bằng Carbon |
| **Dùng khi** | Tác vụ đơn giản: tóm tắt, dịch, format lại, câu hỏi ngắn |

---

## 🟣 NHÓM 2 — ORCHESTRATOR (Google — Điều phối đa Agent)

### 4. Orchestrator (Carbon) `New` ✅ *(anh đang dùng)*
| | |
|---|---|
| **Hãng** | Google DeepMind |
| **Bản chất** | KHÔNG phải model đơn thuần — đây là **meta-model điều phối** |
| **Cơ chế** | Tự động chia task → giao cho nhiều sub-agent chạy song song → tổng hợp kết quả |
| **Nền tảng** | Dùng Carbon làm backbone |
| **Điểm mạnh** | **Làm tác vụ lớn, phức tạp, nhiều bước** — tự động lên kế hoạch & phân công |
| **Điểm yếu** | Chậm hơn model đơn vì phải điều phối nhiều agent; tốn quota nhiều hơn |
| **Dùng khi** | Dự án lớn (xây web, audit toàn bộ hệ thống, phân tích 100+ file), /teamwork, /goal |

> **Lý do anh nên dùng Orchestrator:** Các tác vụ INFOASIA (SAP, Video, Marketing) thường nhiều bước → Orchestrator tự chia nhỏ và chạy song song = nhanh hơn nhiều

---

### 5. Orchestrator (Argon) `New`
| | |
|---|---|
| **Hãng** | Google DeepMind |
| **Bản chất** | Giống Orchestrator Carbon nhưng backbone là Argon |
| **So với Carbon** | Nhẹ hơn, tiết kiệm quota hơn, vẫn điều phối được |
| **Dùng khi** | Dự án vừa, không quá phức tạp nhưng vẫn cần đa agent |

---

## 🟡 NHÓM 3 — GEMINI 3.8 Flash (Google — Nhanh)

### 6. Gemini 3.8 Flash `Medium` `Fast`
| | |
|---|---|
| **Hãng** | Google DeepMind |
| **Tốc độ** | **Nhanh nhất** trong tất cả model (badge `Fast`) |
| **Điểm mạnh** | Trả lời tức thì, quota rẻ, phù hợp hỏi đáp nhanh |
| **Điểm yếu** | Không mạnh bằng Gemini 4 ở reasoning sâu và code phức tạp |
| **Dùng khi** | Hỏi nhanh, test thử, brainstorm ý tưởng, tác vụ không cần độ chính xác cao |

---

## 🔵 NHÓM 4 — CLAUDE (Anthropic) `Notice`

> Badge `Notice` = **trả phí riêng hoặc giới hạn quota hàng tuần** — dùng ít thôi

### 7. Claude Sonnet 4.6 (Thinking) `Notice`
| | |
|---|---|
| **Hãng** | Anthropic |
| **Điểm mạnh** | **Giỏi nhất về code**, refactor code, debug, viết technical doc |
| **Thinking mode** | Suy nghĩ từng bước trước khi trả lời → chính xác hơn với bài toán logic |
| **Điểm yếu** | Tiếng Việt không tự nhiên bằng Gemini, tốn Notice quota |
| **Dùng khi** | **Code khó, bug phức tạp, refactor lớn** — đây là model tốt nhất cho pure coding |

---

### 8. Claude Opus 4.6 (Thinking) `Notice`
| | |
|---|---|
| **Hãng** | Anthropic |
| **Sức mạnh** | Mạnh nhất của Anthropic — flagship toàn diện |
| **Thinking mode** | Deep reasoning, phân tích chiến lược phức tạp |
| **Điểm yếu** | Chậm nhất, tốn Notice quota nhất |
| **Dùng khi** | Phân tích nghiệp vụ cực phức tạp, chiến lược dài hạn, research sâu |

---

## ⚫ NHÓM 5 — GPT-OSS (OpenAI/Meta) `Notice`

### 9. GPT-OSS 120B (Medium) `Notice`
| | |
|---|---|
| **Hãng** | OpenAI / Meta (open-source 120B params) |
| **Điểm mạnh** | Viết văn sáng tạo tự nhiên, storytelling, creative content |
| **Điểm yếu** | Không mạnh bằng Gemini 4 ở code/SQL, tốn Notice quota |
| **Dùng khi** | Viết kịch bản phim, truyện, content sáng tạo, copywriting |

---

## 🎯 Bảng Khuyến Nghị Dùng Model Theo Tác Vụ INFOASIA

| Tác Vụ | Model Khuyến Nghị | Lý Do |
|---|---|---|
| SAP B1 / SQL phức tạp | **Gemini 4 Carbon** | Reasoning sâu, chính xác cao |
| Dự án lớn / nhiều bước | **Orchestrator (Carbon)** ✅ | Tự chia task, chạy song song |
| Viết content / Marketing | **Gemini 4 Argon** | Đa năng, tiếng Việt tốt |
| Code / Bug fix | **Claude Sonnet 4.6** | Giỏi code nhất |
| Hỏi nhanh / Test thử | **Gemini 3.8 Flash** | Nhanh nhất, tiết kiệm quota |
| Video / Kịch bản | **GPT-OSS 120B** | Sáng tạo, storytelling |
| Phân tích chiến lược | **Claude Opus 4.6** | Deep reasoning |

---

## 📊 So Sánh Tổng Hợp

```
TỐC ĐỘ (nhanh → chậm):
Flash > Hydrogen > Argon ≈ Carbon > Orchestrator > Sonnet > Opus

SỨC MẠNH REASONING:
Opus > Orchestrator(Carbon) > Carbon > Sonnet > Argon > Hydrogen > Flash

CODE:
Sonnet ≈ Opus > Carbon > Orchestrator > Argon > GPT-OSS > Flash

TIẾNG VIỆT:
Gemini 4 (tất cả) > Flash > GPT-OSS > Claude

QUOTA TIẾT KIỆM:
Flash > Hydrogen > Argon > Carbon > Orchestrator > Claude/GPT (Notice)
```

> [!TIP]
> **Khuyến nghị cho INFOASIA:** Mặc định dùng **Orchestrator (Carbon)** cho tác vụ nghiệp vụ lớn. Chuyển sang **Gemini 3.8 Flash** khi chỉ hỏi nhanh để tiết kiệm quota Claude (29% weekly còn lại).
