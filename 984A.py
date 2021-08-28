n = int(input())
lst = list(map(int, input().split(" ")))
turn = 1
for i in range(1, n):
    if turn == 1:
        maxT = max(lst)
        lst.remove(maxT)
        turn = 2
    else:
        minT = min(lst)
        lst.remove(minT)
        turn = 1
print(lst[0])
