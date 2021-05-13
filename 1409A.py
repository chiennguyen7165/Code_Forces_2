t = int(input())
r = list()
for i in range(0, t):
    n = list(map(int, input().split(" ")))
    x = str(abs(n[0]-n[1]))
    if(x == "0"):
        count = 0
    elif(len(x) == 1):
        count = 1
    elif(x[-1] == "0"):
        count = int(x[0:-1])
    else:
        count = int(x[0:-1]) + 1
    r.append((count))
for item in r:
    print(item)