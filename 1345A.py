t = int(input())
for i in range(0, t):
    m, n = map(int, input().split(" "))
    if m == 1 or n == 1:
        print("YES")
    elif m * n == 4:
        print("YES")
    else: print("NO")