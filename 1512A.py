t = int(input())
for i in range(0, t):
    n = int(input())
    ip = list(map(int, input().split(" ")))
    ipSet = list(set(ip))
    soA = ipSet[0]
    soB = ipSet[1]
    dem = 0
    for item in ip:
        if item == soA:
            dem += 1
    if(dem == 1):
        print(ip.index(soA) +1)
    else: print(ip.index(soB) +1)

