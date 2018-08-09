"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""


class Date:
    months = {
        0: (31, 'Jan'),
        1: (28, 'Feb'),
        2: (31, 'Mar'),
        3: (30, 'Apr'),
        4: (31, 'May'),
        5: (30, 'Jun'),
        6: (31, 'Jul'),
        7: (31, 'Aug'),
        8: (30, 'Sep'),
        9: (31, 'Oct'),
        10: (30, 'Nov'),
        11: (31, 'Dec')
    }

    weekdays = {
        0: 'Sun',
        1: 'Mon',
        2: 'Tue',
        3: 'Wed',
        4: 'Thu',
        5: 'Fri',
        6: 'Sat'
    }

    def __init__(self, weekday=2, date=1, mon=0, year=1901):
        self.weekday = weekday
        self.date = date
        self.mon = mon
        self.year = year

    def __str__(self):
        return f'{self.weekdays[self.weekday]} ' \
               f'{self.date} ' \
               f'{self.months[self.mon][1]} ' \
               f'{self.year} ' \
               f'{self.is_leap_year()}'

    def next_date(self):
        self.date += 1
        self.weekday += 1
        if self.weekday == 7:
            self.weekday = 0

        if self.mon == 1 and self.is_leap_year():
            if self.date == 30:
                self.date = 1
                self.mon += 1
                return

        if self.date > self.months[self.mon][0]:
            self.date = 1
            self.mon += 1

        if self.mon == 12:
            self.mon = 0
            self.year += 1

    def is_leap_year(self):
        if self.year % 400 == 0:
            return True
        if self.year % 4 == 0 and self.year % 100 != 0:
            return True
        else:
            return False


def main():
    date = Date(2, 1, 1, 1901)
    count = 0
    while date.year != 2001:
        if date.date == 1 and date.weekday == 0:
            count += 1
        date.next_date()
    print(count)


if __name__ == '__main__':
    main()
