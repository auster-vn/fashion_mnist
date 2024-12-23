
# **Fashion MNIST Classification**

Đây là một ứng dụng nhận diện các loại quần áo từ bộ dữ liệu Fashion MNIST. Dự án bao gồm mô hình được huấn luyện bằng TensorFlow và giao diện web sử dụng Flask để dự đoán kết quả.

## **Cấu trúc dự án**
```
fashion_mnist_project/
│
├── app.py                 # Flask app để triển khai mô hình
├── train_model.py         # Script huấn luyện mô hình với Fashion MNIST
├── requirements.txt       # Danh sách thư viện cần thiết
├── static/                # Thư mục chứa file tĩnh (hình ảnh, mô hình)
│   └── uploads/           # Thư mục chứa ảnh tải lên
├── templates/             # Thư mục chứa giao diện HTML
│   └── index.html         # Giao diện người dùng
└── models/                # Thư mục lưu mô hình
    ├── best_model.keras   # Mô hình tốt nhất trong quá trình huấn luyện
    └── final_model.keras  # Mô hình cuối cùng
```

---

## **Yêu cầu hệ thống**

- Python 3.10 hoặc mới hơn.
- Các thư viện Python được liệt kê trong `requirements.txt`.

---

## **Cài đặt**

1. **Clone repository**:
   ```bash
   git clone https://github.com/username/fashion-mnist-classification.git
   cd fashion-mnist-classification
   ```

2. **Tạo môi trường ảo (khuyến nghị)**:
   ```bash
   python -m venv env
   source env/bin/activate  # Trên Linux/Mac
   env\Scripts\activate     # Trên Windows
   ```

3. **Cài đặt các thư viện cần thiết**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Tạo các thư mục cần thiết**:
   ```bash
   mkdir -p static/uploads
   ```

---

## **Sử dụng**

### 1. **Huấn luyện mô hình**
Nếu bạn muốn huấn luyện mô hình từ đầu, chạy:
```bash
python train_model.py
```
- Mô hình tốt nhất sẽ được lưu trong `models/best_model.keras`.
- Mô hình cuối cùng sẽ được lưu trong `models/final_model.keras`.

### 2. **Chạy Flask app**
Để khởi động ứng dụng Flask:
```bash
python app.py
```
- Mở trình duyệt và truy cập: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## **Hướng dẫn sử dụng**

1. **Giao diện web**:
   - Truy cập vào địa chỉ `http://127.0.0.1:5000`.
   - Tải lên một hình ảnh của quần áo (PNG, JPG hoặc JPEG).
   - Ứng dụng sẽ hiển thị tất cả các loại quần áo với xác suất dự đoán tương ứng.

2. **API RESTful**:
   - URL: `POST /predict`
   - **Yêu cầu**:
     - Tải lên file hình ảnh dưới dạng `multipart/form-data` với key là `file`.
   - **Phản hồi**:
     - Dạng JSON:
       ```json
       {
           "predictions": [
               {"class": "T-shirt/top", "probability": 0.6},
               {"class": "Trouser", "probability": 0.2},
               {"class": "Pullover", "probability": 0.1},
               ...
           ]
       }
       ```

---

## **Mô hình**
- Bộ dữ liệu: [Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist).
- Mô hình sử dụng TensorFlow với kiến trúc:
  - 2 lớp Convolutional.
  - 2 lớp MaxPooling.
  - 1 lớp Fully Connected với Dropout.
- **Kết quả huấn luyện**:
  - Độ chính xác trên tập kiểm thử: ~90%.

---

## **Các thư viện sử dụng**

- **TensorFlow**: Xây dựng và huấn luyện mô hình.
- **Flask**: Triển khai ứng dụng web.
- **OpenCV**: Tiền xử lý hình ảnh.
- **Pillow**: Hỗ trợ xử lý ảnh tải lên.

---

## **Cải thiện**
1. Tăng số lượng epoch và kích thước batch trong quá trình huấn luyện.
2. Sử dụng Augmentation để mở rộng dữ liệu.
3. Triển khai mô hình TensorFlow.js để sử dụng trực tiếp trên trình duyệt.

---

