# TEST CASE - BLACK BOX

## 1. Hình chữ nhật
| TC | Input | Expected |
|----|------|----------|
| 1 | (5,3) | 16,15 |
| 2 | (1,1) | 4,1 |
| 3 | (0,5) | Error |
| 4 | (-1,3) | Error |

---

## 2. PT bậc 2
| TC | Input | Expected |
|----|------|----------|
| 1 | (1,-3,2) | 2 nghiệm |
| 2 | (1,2,1) | nghiệm kép |
| 3 | (1,0,1) | vô nghiệm |
| 4 | (0,1,2) | Error |

---

## 3. Số ngày
| TC | Input | Expected |
|----|------|----------|
| 1 | (2,2024) | 29 |
| 2 | (2,2023) | 28 |
| 3 | (13,2024) | Error |

---

## 4. Nguyên tố
| TC | Input | Expected |
|----|------|----------|
| 1 | 2 | True |
| 2 | 4 | False |
| 3 | -1 | False |

---

## 5. Tổng xen kẽ
| TC | Input | Expected |
|----|------|----------|
| 1 | 5 | 3 |
| 2 | 2 | -1 |
| 3 | 0 | Error |

---

## 6. UCLN
| TC | Input | Expected |
|----|------|----------|
| 1 | (12,18) | 6 |
| 2 | (0,5) | 5 |
| 3 | ("a",5) | Error |

---

## 7. Tổng giai thừa
| TC | Input | Expected |
|----|------|----------|
| 1 | 3 | 9 |
| 2 | 5 | 153 |
| 3 | -1 | Error |