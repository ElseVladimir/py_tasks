"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab
У вас есть неограниченное число попыток.
Время одной попытки: 5 mins
"""
newline = []
with open('dataset_24465_4.txt', 'r')as f, open('testfile.txt','w') as f_:
    for line in f:
        newline.append(line)
    for line in reversed(newline):
        f_.write(line)


