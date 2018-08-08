# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math
from functions import is_prime


def get_largest_prime_factor(n):
    for i in range(3, math.ceil(n / 2) + 1, 2):
        if n % i == 0 and is_prime(n / i):
            return int(n / i)


def main():
    print(get_largest_prime_factor(600851475143))


if __name__ == '__main__':
    main()
