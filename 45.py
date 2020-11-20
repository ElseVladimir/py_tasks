"""

В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный
математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

Пример выходного файла:
Interesting
Boring
Interesting
Boring
У вас есть неограниченное число попыток.
Время одной попытки: 5 mins

"""
import requests

diglist = []
with open('dataset_24476_3.txt') as f:
    for integer in f:
        diglist.append(integer.strip())
for i in diglist:
    api_url = 'http://numbersapi.com/{}/math?json=true'.format(i)
    res = requests.get(api_url)
    data = res.json()
    if data['found'] == True:
        print("Interesting")
    elif data['found'] == False:
        print("Boring")


