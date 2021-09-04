t = int(input())
start = 97
s = []
l = []
r = []
for i in range(0, t):
    n, k = map(int, input().split(" "))
    soLan = int(n / k)
    conLai = n - soLan * k
    for i in range(0, k):
        s.append(start + i)
    for j in range(0, conLai):
        l.append(start + j)
    for k in range(0, soLan):
        r.extend(s)
    r.extend(l)
    for item in r:
        print(chr(item), sep='', end='')
    print("")
    s = []
    l = []
    r = []
