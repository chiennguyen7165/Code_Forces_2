n, k = map(int, input().split(" "))
rank = list(map(int, input().split(" ")))
counter = 0
setRank = set(rank)
temp = []
if len(setRank) < k: print("NO")
else:
    print("YES")
    lstRank = list(setRank)
    for i in lstRank:
        temp.append(rank.index(i)+1)
    for i in range(0, k):
        print(str(temp[i]), end =" ")
