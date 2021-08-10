t = int(input())
for i in range(0, t):
    l, r = map(int, input().split(" "))
    if r % l == 0:
        print(l, r)
    else:
        x = l
        y = l * 2
        if (y > r): print(-1, -1)
        else: print(x, y)