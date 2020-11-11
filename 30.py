# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
#
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.
#
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.
#
# Sample Input 1:
#
# 2016 4 20
# 14
#
# Sample Output 1:
#
# 2016 5 4
#
# Sample Input 2:
#
# 2016 2 20
# 9
#
# Sample Output 2:
#
# 2016 2 29
#
# Sample Input 3:
#
# 2015 12 31
# 1
#
# Sample Output 3:
#
# 2016 1 1
#

import datetime
date_inp = list(map(int, input().split()))
days = int(input())
yy = date_inp[0]
mm = date_inp[1]
dd = date_inp[2]
def time(yy, mm, dd, days):
    dt = datetime.date(yy, mm, dd)
    count = dt + datetime.timedelta(days=days)
    print(count.year, count.month, count.day)
    #count.strftime("%Y %m %d")
    # count.year, count.month, count.day


time(yy, mm, dd, days)
