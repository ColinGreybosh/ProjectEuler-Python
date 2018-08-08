"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

import math


nums = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}


def filter_output(output):
    temp = output
    if temp.startswith('and'):
        temp = temp[3:]
    if temp.endswith('and'):
        temp = temp[:-3]
    return temp


def main():
    letter_count = 0
    for i in range(1, 1001):
        word = ''
        if 1000 <= i % 10000 <= 9999:
            word += nums[i // 1000] + 'thousand'
        if 100 <= i % 1000 <= 999:
            word += nums[i // 100] + 'hundred'
        word += 'and'
        if 10 <= i % 100 <= 19:
            word += nums[i % 100]
            word = filter_output(word)
            letter_count += len(word)
            continue
        if 2 <= math.floor(i % 100 / 10) <= 9:
            word += nums[math.floor(i % 100 / 10) * 10]
        if 1 <= i % 10 <= 9:
            word += nums[i % 10]
        word = filter_output(word)
        letter_count += len(word)
    print(letter_count)


if __name__ == '__main__':
    main()
