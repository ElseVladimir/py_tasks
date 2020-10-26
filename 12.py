# Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
#
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]

# lst = [12,13,14,15,16,17,18,19]
def modify_list(lst):
    x = len(lst) - 1
    for i in lst[::-1]:
        if i % 2 == 0:
            z = lst[x] / 2
            lst[x] = int(z)
        else:
            del lst[x]
        x -= 1
#     return lst
#
# print(modify_list(lst))
