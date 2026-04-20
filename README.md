# DG-KDCLPM-LT4-
# BÀI THỰC HÀNH 03 - KIỂM THỬ HỘP ĐEN

## 1. Mô tả bài toán
Chương trình gồm các chức năng:
1. Tính chu vi hình chữ nhật
2. Tính diện tích hình chữ nhật
3. Giải phương trình bậc 2
4. Tính số ngày trong tháng
5. Kiểm tra số nguyên tố
6. Tính tổng S = 1 - 2 + 3 - 4 + ... + n
7. Tìm UCLN của a và b
8. Tính tổng S = 1! + 2! + ... + n!

---

## 2. Áp dụng kiểm thử hộp đen

### a. Phân lớp tương đương
Dữ liệu được chia thành:
- Hợp lệ
- Không hợp lệ

Ví dụ:
- n ≥ 1 → hợp lệ
- n < 1 → không hợp lệ

---

### b. Phân tích giá trị biên
Kiểm tra các giá trị:
- 0
- 1
- Số âm
- Giá trị lớn

---

### c. Kiểm tra ngoại lệ
- Sai kiểu dữ liệu (string, ký tự)
- Giá trị không hợp lệ

---

## 3. Áp dụng cho từng bài

### 1. Hình chữ nhật
- Input: a, b
- Hợp lệ: a > 0, b > 0
- Biên: a = 1, b = 1
- Không hợp lệ: a ≤ 0

---

### 2. PT bậc 2
- Input: a, b, c
- Hợp lệ: a ≠ 0
- Biên: delta = 0
- Không hợp lệ: a = 0

---

### 3. Số ngày
- Input: tháng (1–12), năm
- Biên: tháng = 1, 12
- Không hợp lệ: tháng ngoài [1,12]

---

### 4. Số nguyên tố
- Input: n
- Biên: n = 2
- Không hợp lệ: n < 2

---

### 5. Tổng xen kẽ
- Input: n ≥ 1
- Biên: n = 1
- Không hợp lệ: n ≤ 0

---

### 6. UCLN
- Input: a, b (số nguyên)
- Biên: a = 0 hoặc b = 0

---

### 7. Tổng giai thừa
- Input: n ≥ 1
- Biên: n = 1
- Không hợp lệ: n ≤ 0

---

## 4. Kết luận
- Chương trình xử lý đúng với dữ liệu hợp lệ
- Phát hiện lỗi với dữ liệu không hợp lệ
- Áp dụng hiệu quả kiểm thử hộp đen