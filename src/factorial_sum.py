def giai_thua(n):
    if not isinstance(n, int):
        raise ValueError("n phải là số nguyên")

    if n < 0:
        raise ValueError("n phải >= 0")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def tong_giai_thua(n):
    if n < 1:
        raise ValueError("n phải >= 1")

    s = 0
    for i in range(1, n + 1):
        s += giai_thua(i)

    return s