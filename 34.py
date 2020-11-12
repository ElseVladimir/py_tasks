"""

Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba", после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Если операций потребуется более 1000, выведите Impossible.

Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a, или Impossible, если операций потребуется более 1000.

Условие задачи было изменено 12.09.2018

Sample Input 1:

ababa
a
b

Sample Output 1:

1

Sample Input 2:

ababa
b
a

Sample Output 2:

1

Sample Input 3:

ababa
c
c

Sample Output 3:

0

Sample Input 4:

ababac
c
c

Sample Output 4:

Impossible

"""
s = input() #abab #baba #bbaa
a = input() #ab
b = input() #ba

def counter(s, a, b):
    counter_ = 0
    new_s = s
    while counter_ <= 1000:
        if a in new_s:
            new_s = new_s.replace(a, b)
            counter_ += 1
        else:
            return counter_

    return "Impossible"


print(counter(s, a, b))
