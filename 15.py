# Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел,
# которые нужно считать. Далее считывает n строк с числами xi по одному числу в
# каждой строке. Итого будет n+1 строк.
#
# При считывании числа xix_ixi программа должна на отдельной строке вывести значение f(xi).
# Функция f(x) уже реализована и доступна для вызова.
#
# Функция вычисляется достаточно долго и зависит только от переданного аргумента x
# . Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.
#
# Sample Input:
#
# 5
# 5
# 12
# 9
# 20
# 12
#
# Sample Output:
#
# 11
# 41
# 47
# 61
# 41
#
def f(x):
    return x+1

zz = [int(i) for i in input().split()]
timer = 0
n = zz[0]
dick = dict()
while n > timer:
    a = [int(i) for i in input().split()]
    for x in a:
        if x not in dick:
            dick.update({x:f(x)})
            print(dick[x])
        else:
            print(dick[x])
    timer += 1

