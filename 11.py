# Напишите программу, которая считывает список чисел lstlst из первой строки
# и число xx из второй строки, которая выводит все позиции, на которых встречается
# число xx в переданном списке lstlst.
#
# Позиции нумеруются с нуля, если число xx не встречается в списке, вывести
# строку "Отсутствует" (без кавычек, с большой буквы).
#
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
#
# Sample Input 1:
#
# 5 8 2 7 8 8 2 4
# 8
# Sample Output 1:
#
# 1 4 5
# Sample Input 2:
#
# 5 8 2 7 8 8 2 4
# 10
# Sample Output 2:
#
# Отсутствует

a = [int(i) for i in input().split()]
b = int(input())
lst = []
cnt = 0
for id, item in enumerate(a):
    if b == item:
        lst.append(id)
        cnt += 1
if cnt > 0:
    print(*lst)
elif cnt == 0:
    print("Отсутствует")
