# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?


def is_divisible_from_1_20(n):
    for i in range(2, 21):
        if n % i != 0:
            return False
    return True


for x in range(1, int(1e9)):
    if is_divisible_from_1_20(x * 2520):
        print(x * 2520)
        break