t = int(input())
for i in range(0, t):
    chLon = ""
    check = 0
    n = int(input())
    for j in range(0, n):
        ch = input()
        chLon += ch
    chSet = set()
    for item in chLon:
        chSet.add(item)
    chLst = list(chSet).copy()
    for p in chLst:
        if(chLon.count(p) % n == 0):
            check += 1
    if(check == len(chLst)):
        print("YES")
    else: print("NO")