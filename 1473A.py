t = int(input())
for step in range(0, t):
    n, d = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    counter = 0
    bigger = 0
    for i in a:
        aTemp = a.copy()
        aTemp.remove(i)
        if i > d:
            bigger += 1
        else:
            for j in aTemp:
                if i + j <= d:
                    counter += 1
    if(bigger == 0):
        print("YES")
    elif(bigger > 0 and counter > 0):
        print("YES")
    else:
        print("NO")