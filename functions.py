import math


def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or is_even(n):
        return False
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_even(n):
    if int(n) & 1 == 0:
        return True
    return False
