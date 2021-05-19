t = int(input())
r = list()
for i in range(0, t):
    c = list(map(int, input().split(" ")))
    if c[2] % c[0] >= c[1]:
        r.append(c[2] - c[2] % c[0] + c[1])
    else:
        r.append(c[2] - c[2] % c[0] + c[1] - c[0])
for item in r:
    print(item)