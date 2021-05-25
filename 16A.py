ip = list(map(int, input().split(" ")))
n = ip[0]
m = ip[1]
f = list()
dk1 = 0
dk2 = 0
for i in range(0, n):
    h = input()
    a = set()
    for i in h:
        a.add(i)
    if(len(a) != 1):
        dk1 +=1
    f.append(h)
if(dk1 != 0):
    print("NO")
else:
    if(dk1 == 0):
        for k in range(0, n):
            if(k == n -1):
                continue
            else:
                if( f[k][0] == f[k+1][0]):
                    dk2 += 1
    if(dk2 == 0):
        print("YES")
    else: print("NO")