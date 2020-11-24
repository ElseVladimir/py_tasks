"""

Задача на программирование: небольшое число Фибоначчи


Дано целое число 1≤n≤40 1 \le n \le 40 1≤n≤40, необходимо вычислить n n n-е число Фибоначчи
(напомним, что
F0=0 F_0=0 F0=0, F1=1 F_1=1 F1=1 и Fn=Fn−1+Fn−2 F_n=F_{n-1}+F_{n-2} Fn=Fn−1+Fn−2 при n≥2)

Sample Input:

3

Sample Output:

2


"""
a = int(input())
if a == 1 or a == 2:
    print(1)
    exit()
x = 1
y = 1
z = 0
counter = 2
while True:
    z = x + y
    x = y
    y = z
    counter += 1
    if counter >= a:
        break
print(z)
