"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""

from math import factorial


def main():
    print(sum([int(x) for x in str(factorial(100))]))


if __name__ == '__main__':
    main()