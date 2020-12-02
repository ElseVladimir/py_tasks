c = [i for i in map(int, input().split())]
def g_c_d(c):
    while c[0] != 0 and c[1] != 0:
        if c[0] > c[1]:
            c[0] %= c[1]
        else:
            c[1] %= c[0]
    return c[0] + c[1]
print(g_c_d(c))