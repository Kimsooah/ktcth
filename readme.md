# Hướng dẫn

## Thực thi mã nguồn

- Bước 1: Bật `cmd` hoặc `bash` hoặc `terminal` lên.
- Bước 2: Gõ lệnh

```
python sample_server.py --port 69
```

→ Coi như một máy chủ đang chạy trên máy tính cá nhân và đợi dữ liệu ở cổng `69`.

- Bước 3: Tiếp tục bật một cửa sổ `cmd` hoặc `bash` hoặc `terminal` khác lên.
- Bước 4: Gõ lệnh

```
python sample_client.py --port 69
```

→ Coi như đang đóng giả một máy khách, gửi thông tin đến cổng 69 của máy chủ.

## Sửa mã nguồn

Ứng theo yêu cầu của từng bài tập thì sửa lại `sample_client.py` và `sample_server.py` cho phù hợp.

Ví dụ như với bài 16 có yêu cầu:
- (1) Nhập vào một xâu ký tự từ client.
- (2) Truyền xâu sang server theo giao thức UDP.
- (3) Server:
    - (3.1) Hiển thị xâu.
    - (3.2) Tính số lượng chữ thường trong xâu.
    - (3.3) Báo lại cho client.

Giải quyết từng yêu cầu:

- (1) Chưa cần sửa gì.
- (2) Sửa lại ở cả `client` và `server` đoạn: `sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`, ở tham số `socket.AF_INET` và `socket.SOCK_STREAM` cho tương ứng?
- (3.1) Sửa lại ở `server` để in ra xâu hoàn chỉnh?
- (3.2) Tìm trên mạng từ khóa `lowercase count python`.
- (3.3) Dùng `client.send` ở `server`?

## Nguồn tham khảo mã nguồn

Trang 36 sách "Python Network Programming Cookbook".