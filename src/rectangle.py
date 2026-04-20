def chu_vi(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Input phải là số")
    if a <= 0 or b <= 0:
        raise ValueError("Chiều dài và rộng phải > 0")
    return (a + b) * 2


def dien_tich(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Input phải là số")
    if a <= 0 or b <= 0:
        raise ValueError("Chiều dài và rộng phải > 0")
    return a * b