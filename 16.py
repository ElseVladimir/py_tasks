with open('dataset_3363_2.txt') as inf:
    s = inf.readline()
test = "A13b5"
test += " "
c = "1234567890"
x = 0
dig = ""
stringa = ""
for i in range(len(test) -1):
    if test[i] not in c:
        stringa += test[i]
        x += 1
        while test[i + x] in c:
            dig += test[i + x]
            x += 1
    else:
        continue
    stringa += test[i] * (int(dig) - 1)
    x = 0
    dig = ""
print(stringa)