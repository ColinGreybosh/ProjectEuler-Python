# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.
#
# What is the 10 001st prime number?

from functions import is_prime


def find_nth_prime(n):
    prime_count = 0
    for i in range(1, int(1e9)):
        if is_prime(i):
            prime_count += 1
        if prime_count == n:
            return i


print(find_nth_prime(10001))
