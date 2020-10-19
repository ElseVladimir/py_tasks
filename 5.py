# В институте биоинформатики по офису передвигается робот.
# Недавно студенты из группы программистов написали для него программу,
# по которой робот, когда заходит в комнату, считает количество программистов
# в ней и произносит его вслух: "n программистов".
#
# Для того, чтобы это звучало правильно,
# для каждого n n n нужно использовать верное окончание слова.
#
# Напишите программу, считывающую с пользовательского ввода целое число n n n (неотрицательное),
# выводящее это число в консоль вместе с правильным образом изменённым словом "программист",
# для того, чтобы робот мог нормально общаться с людьми, например:
# 1 программист, 2 программиста, 5 программистов.
#
# В комнате может быть очень много программистов.
# Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.
#
# Дополнительный комментарий к условию:
# Обратите внимание, что задача не так проста, как кажется на первый взгляд.
# Если ваше решение не проходит какой-то тест, это значит, что вы не рассмотрели какой-то из
# случаев входных данных (число программистов 0≤n≤1000 0 \le n \le 1000 0≤n≤1000).
# Обязательно проверяйте свои решения на дополнительных значениях, а не только на тех,
# что приведены в условии задания.
#
# Так как задание повышенной сложности, вручную код решений проверяться не будет.
# Если вы столкнулись с ошибкой в первых четырёх тестах, проверьте, что вы используете только
# русские символы для ответа. В остальных случаях ищите ошибку в логике работы программы.
#
#
# Sample Input 1:
#
# 5
#
# Sample Output 1:
#
# 5 программистов
#
# Sample Input 2:
#
# 0
#
# Sample Output 2:
#
# 0 программистов
#
# Sample Input 3:
#
# 1
#
# Sample Output 3:
#
# 1 программист
#
# Sample Input 4:
#
# 2
#
# Sample Output 4:
#
# 2 программиста
#


digit = int(input())
x = digit % 10
if 11 <= digit <= 14:
    print(str(digit) + " программистов")
elif 111 <= digit <= 114:
    print(str(digit) + " программистов")
elif 211 <= digit <= 214:
    print(str(digit) + " программистов")
elif 311 <= digit <= 314:
    print(str(digit) + " программистов")
elif 411 <= digit <= 414:
    print(str(digit) + " программистов")
elif 511 <= digit <= 514:
    print(str(digit) + " программистов")
elif 611 <= digit <= 614:
    print(str(digit) + " программистов")
elif 711 <= digit <= 714:
    print(str(digit) + " программистов")
elif 811 <= digit <= 814:
    print(str(digit) + " программистов")
elif 911 <= digit <= 914:
    print(str(digit) + " программистов")
elif x == 1:
    print(str(digit) + " программист")
elif 2 <= x <= 4:
    print(str(digit) + " программиста")
else:
    print(str(digit) + " программистов")
