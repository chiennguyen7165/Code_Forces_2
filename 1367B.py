t = int(input())
for t in range(0, t):
    n = int(input())
    mang = list(map(int, input().split(" ")))
    tempC = 0
    tempL = 0
    for i in range(0, n):
        if i % 2 == 0:
            if mang[i] % 2 == 0:
                pass
            else:
                tempC += 1
        else:
            if mang[i] % 2 != 0:
                pass
            else:
                tempL += 1
    if (tempC == tempL):
        print(tempC)
    else:
        print(-1)