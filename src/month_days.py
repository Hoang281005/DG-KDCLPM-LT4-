def so_ngay(thang, nam):
    if not isinstance(thang, int) or not isinstance(nam, int):
        raise ValueError("Input phải là số nguyên")

    if thang < 1 or thang > 12:
        raise ValueError("Tháng không hợp lệ")

    if thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
            return 29
        return 28

    if thang in [4, 6, 9, 11]:
        return 30

    return 31