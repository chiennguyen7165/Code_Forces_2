t = int(input())
op = list()
for i in range(0, t):
    r = []
    n = int(input())
    c = list(map(int, input().split(" ")))
    e = set(c)
    if(len(c) != len(e)):
        op.append(0)
    elif(len(c) == 2):
        op.append(abs(c[0] - c[1]))
    else:
        for m in range(0, n):
            if(m == n -1):
                continue
            else:
                for l in range(m+1, n + 1):
                    if(l == n):
                        continue
                    else:
                        r.append(abs(c[m] - c[l]))
        op.append(min(r))
for item in op:
    print(item)