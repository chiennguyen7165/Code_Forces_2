n = int(input())
t = list()
p = list()
soT = 0
soP = 0
for i in range(0,n):
    h = list(map(int, input().split(" ")))
    t.append(h[0])
    p.append(h[1])
setT = set(t)
setP = set(p)
if(len(setP) == 1 and len(setT) == 1):
    print(0)
elif(t.count(1) == p.count(1) or t.count(0) == p.count(0)):
    print((n - t.count(1)) * 2)
elif(t.count(1) == n):
    print(n - p.count(1))
elif(t.count(0) == n):
    print(n - p.count(0))
elif(p.count(1) == n):
    print(n - t.count(1))
elif(p.count(0) == n):
    print(n - t.count(0))
elif(t.count(1) > p.count(1)):
    soT = n - t.count(1)
    soP = n - p.count(0)
    print(soT + soP)
else:
    soT = n - t.count(0)
    soP = n - p.count(1)
    print(soT + soP)