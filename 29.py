def friend(x):
    counter = 0
    for i in range(len(x)):
        if len(x[counter]) == 4:
            counter += 1
            continue
        else:
            del x[counter]
    return x
print(friend(['uR', '2r01', 'SJ9V', 'CKva', 'OYpf', 'OVeg', '']))



