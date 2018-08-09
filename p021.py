"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def d(n):
    total = 0
    for factor in range(1, int(n ** 0.5) + 1):
        if n % factor == 0:
            total += (factor) + (n // factor)
    return total - n


def main():
    total = 0
    for a in range(2, 10000):
        b = d(a)
        if b > a and d(b) == a:
            total += a + b
    print(total)


if __name__ == '__main__':
    main()
