import math

def giai_pt_bac2(a, b, c):
    if not all(isinstance(i, (int, float)) for i in (a, b, c)):
        raise ValueError("Input phải là số")

    if a == 0:
        return "Không phải phương trình bậc 2"

    delta = b**2 - 4*a*c

    if delta < 0:
        return "Vô nghiệm"
    elif delta == 0:
        x = -b / (2*a)
        return f"Nghiệm kép: {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"2 nghiệm: {x1}, {x2}"