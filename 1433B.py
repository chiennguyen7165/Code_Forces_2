t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    b = a.copy()
    b.reverse()
    indexF = a.index(1)
    indexL = n - 1 - b.index(1)
    c = a[indexF:indexL+1]
    if len(c) == 1:
        print(0)
    else:
        print(c.count(0))
