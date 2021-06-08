t = int(input())
r = []
for i in range(0, t):
    ip = list(map(int, input().split(" ")))
    h = ip[0]
    m = ip[1]
    hM = 23 - h
    mM = 60 - m
    r.append(hM * 60 + mM)
for itme in r:
    print(itme)
