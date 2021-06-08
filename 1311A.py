t = int(input())
result = []
for i in range(0, t):
    ip = list(map(int, input().split(" ")))
    a = ip[0]
    b = ip[1]
    kc = abs(a - b)
    if(a == b):
        result.append(0)
    elif(a < b):
        if kc % 2 == 1:
            result.append(1)
        else:
            result.append(2)
    else:
        if kc % 2 == 1:
            result.append(2)
        else:
            result.append(1)
for item in result:
    print(item)