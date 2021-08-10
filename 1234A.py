t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    tong = sum(a)
    if tong % n == 0:
        print(int(tong / n))
    else:
        print(int(tong / n) + 1)
