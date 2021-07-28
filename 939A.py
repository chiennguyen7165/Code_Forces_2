n = int(input())
check = 0
plane = list(map(int, input().split(" ")))
plane = [plane[i]-1 for i in range(0, n)]
for i in range(0, n):
    if plane[plane[plane[i]]] == i:     
        check = 1
else:
    print("YES" if check else "NO")

