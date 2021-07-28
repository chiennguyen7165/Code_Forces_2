t = int(input())
for i in range(0, t):
    n = int(input())
    lstA = list(map(int, input().split(" ")))
    setA = set(lstA)
    if len(setA) == 1:
        print(0)
    else:
        miN = min(lstA)
        count = 0
        for item in lstA:
            if item == miN:
                count += 1
        print(n - count)