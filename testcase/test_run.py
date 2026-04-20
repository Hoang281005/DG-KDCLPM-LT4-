import sys
import os

# Thêm đường dẫn src vào Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.rectangle import chu_vi, dien_tich
from src.quadratic import giai_pt_bac2 as solve_quadratic
from src.month_days import so_ngay as days_in_month
from src.prime import is_prime
from src.sum_alternate import tinh_tong as alternate_sum
from src.gcd import ucln as gcd
from src.factorial_sum import tong_giai_thua as sum_factorial


def test_all():
    print("===== RUN TEST =====")

    # 1. Rectangle
    print("\n[Rectangle]")
    print("Perimeter:", "PASS" if chu_vi(5, 3) == 16 else "FAIL")
    print("Area:", "PASS" if dien_tich(5, 3) == 15 else "FAIL")

    # 2. Quadratic
    print("\n[Quadratic]")
    result = solve_quadratic(1, -3, 2)
    print("Quadratic:", "PASS" if "2 nghiệm" in str(result) else "FAIL")

    # 3. Month days
    print("\n[Month Days]")
    print("February 2024:", "PASS" if days_in_month(2, 2024) == 29 else "FAIL")

    # 4. Prime
    print("\n[Prime]")
    print("7 is prime:", "PASS" if is_prime(7) is True else "FAIL")
    print("8 is prime:", "PASS" if is_prime(8) is False else "FAIL")

    # 5. Alternate sum
    print("\n[Alternate Sum]")
    print("n=5:", "PASS" if alternate_sum(5) == 3 else "FAIL")  # 1-2+3-4+5=3

    # 6. GCD
    print("\n[GCD]")
    print("gcd(12,18):", "PASS" if gcd(12, 18) == 6 else "FAIL")

    # 7. Factorial sum
    print("\n[Factorial Sum]")
    print("n=3:", "PASS" if sum_factorial(3) == 9 else "FAIL")  # 1!+2!+3!=9

    print("\n===== DONE =====")


if __name__ == "__main__":
    test_all()