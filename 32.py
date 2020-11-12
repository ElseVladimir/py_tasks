"""
https://stepik.org/lesson/24465/step/6?auth=login&unit=6772
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя
бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
"""
import os

with open('result.txt', 'a') as f:
    for current_dir, dirs, files in os.walk('main'):
        if list(filter(lambda x: x.endswith('.py'), files)):
            f.write('{}\n'.format(current_dir))
list = []
with open('result.txt', 'r') as f:
    for line in f:
        list.append(line)

with open('result.txt','w') as f_:
    for i in sorted(list):
        f_.write(i)

