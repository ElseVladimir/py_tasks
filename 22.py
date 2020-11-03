# функция выводит последовательность фибоначчи до числа n
n = int(input("Введите число "))


def fibonacci(n):
    x = 1
    z = 1
    y = 0
    print(x, z, end = " ")
    while True:
        y = x + z
        print(y, end=" ")
        x = z
        z = y
        if (x + z) > n:
            break


fibonacci(n)
