import math

def is_prime(n):
    if not isinstance(n, int):
        raise ValueError("Input phải là số nguyên")

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True