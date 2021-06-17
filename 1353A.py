t = int(input())
for i in range (0, t):
    ipStr = list(map(int, input().split(" ")))
    n = int(ipStr[0])
    m = int(ipStr[1])
    if(n == 1):
        print(0)
    elif(n == 2):
        print(m)
    else:
        print(2 * m)

