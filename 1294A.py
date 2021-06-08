t = int(input())
result = []
for i in range(0, t):
    ip = list(map(int, input().split(" ")))
    a = ip[0]
    b = ip[1]
    c = ip[2]
    n = ip[3]
    soBiDot1 = max(a, b, c) - min(a, b, c) + max(a,b,c) - (a + b + c - max(a,b,c) - min(a,b,c))
    soBiConLai = n - soBiDot1
    if(soBiConLai < 0):
        result.append('NO')
    elif(soBiConLai % 3 == 0):
        result.append('YES')
    else:
        result.append('NO')
for itme in result:
    print(itme)