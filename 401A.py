n, x = map(int, input().split(" "))
c = list(map(int, input().split(" ")))
tong = sum(c)
if tong == 0:
    print(0)
elif abs(tong) <= x:
    print(1)
else:
    them = 0 if int(abs(tong)% x) == 0 else 1
    print(int(abs(tong)/ x) + them)