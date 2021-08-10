t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    if n == 1 or len(set(a)) == 1:
        print(0)
    else:
        tong = 0
        for item in a: tong += item
        if tong % n != 0:
            print(-1)
        else:
            equal = int(tong / n)
            r = 0
            for item in a:
                if item > equal:
                    r += 1
            print(r)