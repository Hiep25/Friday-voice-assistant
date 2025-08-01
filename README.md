````markdown
 🤖 Trợ lý Ảo Friday (Friday Voice Assistant)

**Friday** là một trợ lý ảo đơn giản được xây dựng bằng Python. Ứng dụng có thể nhận diện giọng nói, phản hồi bằng giọng nói và hỗ trợ người dùng tra cứu thông tin trên Google, YouTube hoặc xem thời gian hiện tại.

> “Xin chào ngài, tôi có thể giúp gì cho ngài hôm nay?”

---

 🎯 Tính năng nổi bật

- 🎤 Nhận diện giọng nói thông qua micro
- 🗣️ Phản hồi bằng giọng nói (Text-to-Speech)
- 🔍 Tìm kiếm nhanh trên Google và YouTube bằng lệnh thoại
- ⏰ Trả về thời gian hiện tại
- 🤝 Chào hỏi thông minh tùy theo thời điểm trong ngày
- 📦 Giao diện dòng lệnh đơn giản, dễ dùng

---

 ⚙️ Yêu cầu hệ thống

- Python 3.6 trở lên
- Kết nối Internet (để nhận diện giọng nói)
- Micro hoạt động tốt
- Hệ điều hành: Windows / Linux / macOS

---

 🧪 Cài đặt và sử dụng

 Bước 1: Tải mã nguồn

```bash
git clone https://github.com/<ten-cua-ban>/friday-voice-assistant.git
cd friday-voice-assistant
````

 Bước 2: Cài đặt thư viện cần thiết

```bash
pip install -r requirements.txt
```

> Nếu gặp lỗi khi cài đặt `pyaudio`, bạn có thể tham khảo hướng dẫn tại:
> [https://www.lfd.uci.edu/\~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) (Windows)

 Bước 3: Chạy ứng dụng

```bash
python AI.py
```

---

 🗣️ Ví dụ lệnh thoại

Bạn có thể nói các câu lệnh sau bằng tiếng Anh:

* `"Google cat videos"` → Mở Google và tìm kiếm
* `"YouTube relaxing music"` → Mở YouTube và tìm kiếm
* `"Time"` → Friday sẽ đọc thời gian hiện tại
* `"Quit"` hoặc `"Exit"` → Thoát ứng dụng

---


 🔧 Định hướng phát triển

Một số tính năng có thể bổ sung trong tương lai:

* Hỗ trợ ngôn ngữ tiếng Việt
* Gọi theo từ khóa đánh thức (ví dụ: "Hey Friday")
* Điều khiển ứng dụng máy tính (mở file, ứng dụng...)
* Kết hợp với API thời tiết hoặc điều khiển nhà thông minh

---
