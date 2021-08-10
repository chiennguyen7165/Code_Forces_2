t = int(input())
for i in range(0, t):
    n = int(input())
    phanDu = n % 3
    if phanDu  == 0:
        c1 = int(n / 3)
        c2 = c1
        print(c1, c2)
    elif phanDu == 1:
        c1 = int(n / 3) + 1
        c2 = c1 - 1
        print(c1, c2)
    else:
        c2 = int(n / 3) + 1
        c1 = c2 - 1
        print(c1, c2)
