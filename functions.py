def is_prime(n: int):
    if n == 2:
        return True
    if n <= 1 or is_even(n):
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_even(n: int):
    if n & 1 == 0:
        return True
    return False


def find_proper_divisors(n: int):
    divisors = [1]
    r = range(2, int(n ** 0.5) + 1)
    if not is_even(n):
        r = range(3, int(n ** 0.5) + 1, 2)
    for i in r:
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return set(divisors)


def find_factors(n: int):
    factors = [1, n]
    r = range(2, int(n ** 0.5) + 1)
    if not is_even(n):
        r = range(3, int(n ** 0.5) + 1, 2)
    for i in r:
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    return set(factors)
