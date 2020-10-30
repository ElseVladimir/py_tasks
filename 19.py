# В какой-то момент в Институте биоинформатики биологи перестали понимать, что
# говорят информатики: они говорили каким-то странным набором звуков.
#
# В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении
# подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ.
# Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:
#
# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
# Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного
# алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно
# зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
#
# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
#
# Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется
# на d, c — на % и d — на #.
# Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра.
# Получаем следующие строки, которые и передаём на вывод программы:
# *d*%*d*#*d*
# dacabac
#
# Sample Input 1:
#
# abcd
# *d%#
# abacabadaba
# #*%*d*%
#
# Sample Output 1:
#
# *d*%*d*#*d*
# dacabac
#
# Sample Input 2:
#
# dcba
# badc
# dcba
# badc
#
# Sample Output 2:
#
# badc
# dcba
#


source = input() # исходный алфавит
encrypt = input() # закодированный алфавит
keyEncrypt = input() # строка которую шифруем
keyDecrypt = input() # строка которую расшифровываем

alphabetDict = dict()
for i in range(len(source)):
    alphabetDict.update({source[i]:encrypt[i]})
cryptedString = ""
decryptedString = ""
counter = 0
while (len(keyEncrypt)) != counter:
    for x, z in alphabetDict.items():
        if x == keyEncrypt[counter:counter + 1]:
            cryptedString += z
            counter += 1
counter = 0
while (len(keyDecrypt)) != counter:
    for z, x in alphabetDict.items():
        if x == keyDecrypt[counter:counter + 1]:
            decryptedString += z
            counter += 1

print(cryptedString)
print(decryptedString)