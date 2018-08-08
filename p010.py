# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from functions import is_prime


def sum_of_primes_below_n(n):
    return sum([x for x in range(2, n) if is_prime(x)])


def main():
    print(sum_of_primes_below_n(int(2e6)))


if __name__ == '__main__':
    main()
