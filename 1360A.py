t = int(input())
r = list()
for i in range (0, t):
    c = list(map(int, input().split(" ")))
    if c[0] == c[1]:
        r.append(c[0] * c[0] * 4)
    elif c[0] == c[1] * 2 or c[1] == c[0] * 2 or min(c) == 1:
        r.append(max(c) * max(c))
    else:
        x = max(c) * 2
        y = min(c) * 2
        if max(c) > y:
            r.append(max(c) * max(c))
        else:
            r.append(y * y)
for item in r:
    print(item)