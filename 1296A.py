t = int(input())
for i in range (0, t):
    n = int(input())
    ip = list(map(int, input().split(" ")))
    soLe = 0
    soChan = 0
    for item in ip:
        if item % 2 != 0:
            soLe += 1
        else: soChan += 1
    if soChan == n:
        print("NO")
    elif soLe == n and n % 2 == 0:
        print("NO")
    elif soLe == n and n % 2 != 0:
        print("YES")
    else:
        print("YES")