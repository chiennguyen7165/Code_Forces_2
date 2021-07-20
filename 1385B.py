t = int(input())
for i in range(0, t):
    n = int(input())
    doubleP = list(map(int, input().split(" ")))
    tempP = []
    tempP.append(doubleP[0])
    for turn in range(0, n - 1):
        theDel = tempP[-1]
        doubleP.remove(theDel)
        doubleP.remove(theDel)
        tempP.append(doubleP[0])
    else:
        print(" ".join(str(x) for x in tempP))
