from rectangle import chu_vi, dien_tich
from quadratic import giai_pt_bac2
from month_days import so_ngay
from prime import is_prime
from sum_alternate import tinh_tong
from gcd import ucln
from factorial_sum import tong_giai_thua

def main():
    print("Chu vi:", chu_vi(5, 3))
    print("Diện tích:", dien_tich(5, 3))

    print(giai_pt_bac2(1, -3, 2))

    print("Số ngày:", so_ngay(2, 2024))

    print("Prime:", is_prime(7))

    print("Tổng xen kẽ:", tinh_tong(5))

    print("UCLN:", ucln(12, 18))

    print("Tổng giai thừa:", tong_giai_thua(5))


if __name__ == "__main__":
    main()