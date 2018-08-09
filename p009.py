"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math
from functools import reduce
from operator import mul


def gen_pyth_triple(u, v):
    return [u * u - v * v, 2 * u * v, u * u + v * v]


def find_pyth_triple_with_sum_n(n):
    for i in range(1, math.ceil(math.sqrt(n))):
        for j in range(1, math.ceil(math.sqrt(n))):
            triple = gen_pyth_triple(i, j)
            if sum(triple) == n:
                return triple


def main():
    print(reduce(mul, find_pyth_triple_with_sum_n(1000)))


if __name__ == '__main__':
    main()
