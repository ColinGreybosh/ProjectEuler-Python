"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math


def is_palindrome(n):
    string = str(n)
    for i in range(0, math.floor(len(string) / 2)):
        if string[i] != string[-(i + 1)]:
            return False
    return True


def find_palindromes():
    palindromes = []
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if is_palindrome(i * j):
                palindromes.append(i * j)
    return palindromes


def main():
    print(max(find_palindromes()))


if __name__ == '__main__':
    main()
