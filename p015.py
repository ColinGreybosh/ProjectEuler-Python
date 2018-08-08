# Starting in the top left corner of a 2×2 grid, and only being able to
# move to the right and down, there are exactly 6 routes to the bottom
# right corner.
#
# How many such routes are there through a 20×20 grid?

import math


def routes_through_grid_of_size_n(n):
    return int(math.factorial(2 * n) / math.pow((math.factorial(n)), 2))


def main():
    print(routes_through_grid_of_size_n(20))


if __name__ == '__main__':
    main()
