t = int(input())
tong = list()
for i in range (0, t):
    tempT = 0
    nk = list(map(int, input().split(" ")))
    temp1 = list(map(int, input().split(" ")))
    temp2 = list(map(int, input().split(" ")))
    if(nk[1] == 0):
        for item in temp1:
            tempT += item
    else:
        for j in range (0, nk[1]):
            a = min(temp1)
            b = max(temp2)
            if(a > b):
                continue
            else:
                temp1.append(b)
                temp1.remove(a)
                temp2.append(a)
                temp2.remove(b)
        for item in temp1:
            tempT += item
    tong.append(tempT)
for i in tong:
    print(i)