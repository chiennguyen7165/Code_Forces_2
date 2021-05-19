t = int(input())
r = list()
for i in range (0, t):
    n = int(input())
    c = list(map(int, input().split(" ")))
    o = list(map(int, input().split(" ")))
    minC = min(c)
    minO = min(o)
    x = 0
    y = 0
    rT = 0
    for j in range(0, n):
        if(c[j] > minC and o[j] > minO):
            x = c[j] - minC
            y = o[j] - minO
            rT = rT + (max(x, y))
        elif(c[j] > minC and o[j] == minO):
            x = x = c[j] - minC
            rT = rT + x
        elif(c[j] == minC and o[j] > minO):
            y = o[j] - minO
            rT = rT + y
        else:
            rT = rT + 0
    r.append(rT)
for item in r:
    print(item)
