t = int(input())
for i in range (0, t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    tong = 0
    for item in a:
        tong += item
    if tong == n:
        print(0)
    elif tong > n:
        print(tong - n)
    else:
        print(1)