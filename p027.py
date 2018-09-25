"""
Project Euler Problem 27
========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""
from functions import is_prime


def quad_value(n, a, b):
    return n**2 + a * n + b


"""
I feel like there's a better algorithm to solve this. 
The quadratic is symmetrical about an axis centered in the interval
[0, l-1] where l is the length of the consecutive primes generated
by the equation. 
"""


def main():
    max_a = 0
    max_b = 0
    max_prime_length = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            length = 0
            for n in range(2000):
                if is_prime(quad_value(n, a, b)):
                    length += 1
                else:
                    if length > max_prime_length:
                        max_prime_length = length
                        max_a = a
                        max_b = b
                    break

    print(f'{max_a * max_b}')


if __name__ == '__main__':
    main()
