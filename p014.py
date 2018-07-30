# The following iterative sequence is defined for the set of
# positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the
# following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

from functions import is_even


class Collatz:
    tree = {}

    def collatz_length(self, n):
        length = 1
        term = n
        while term != 1:
            if is_even(term):
                term = int(term / 2)
                if term in self.tree:
                    length += self.tree[term]
                    break
                else:
                    length += 1
            else:
                term = 3 * term + 1
                if term in self.tree:
                    length += self.tree[term]
                    break
                else:
                    length += 1
        self.tree[n] = length
        return length

    def longest_collatz_chain_in_range(self, r):
        longest_chain = (1, 1)  # (starting term, chain length)
        for n in r:
            chain_length = self.collatz_length(n)
            if chain_length > longest_chain[1]:
                longest_chain = (n, chain_length)
        return longest_chain


print(Collatz.longest_collatz_chain_in_range(Collatz(), range(1, int(1e6))))
