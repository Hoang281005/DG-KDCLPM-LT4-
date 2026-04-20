def tinh_tong(n):
    if not isinstance(n, int):
        raise ValueError("n phải là số nguyên")

    if n < 1:
        raise ValueError("n phải >= 1")

    s = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s -= i
        else:
            s += i

    return s