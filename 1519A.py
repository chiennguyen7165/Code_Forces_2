t = int(input())
for i in range(0, t):
    r, b, d = map(int, input().split(" "))
    if min(r, b) * (d + 1) >= max(r, b):
        print("YES")
    else:
        print("NO")
