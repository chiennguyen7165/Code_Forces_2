t = int(input())
result = []
for i in range(0, t):
    n = int(input())
    s = input()
    ide = []
    temp = 0
    for l in s:
        ide.append(s.index(l))
    for j in range(0, len(ide)):     
        if(j == len(ide) - 1):
            continue
        else:
            if(ide[j] > ide[j+1]):
                temp += 1
    if(temp == 0):
        result.append("YES")
    else: result.append("NO")
for o in result:
    print(o)