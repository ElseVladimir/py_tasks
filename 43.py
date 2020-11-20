"""

Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv

"""

import csv
import collections
primary_type = []
with open("Crimes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        primary_type.append(row['Primary Type'])

print(collections.Counter(primary_type))