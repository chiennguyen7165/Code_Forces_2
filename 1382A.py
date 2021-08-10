t = int(input())
for i in range(0, t):
    n, m = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    k = 0
    r = 0
    for item in a:
        if item in b:
            k = 1
            r = item
            break
    if k == 0:
        print("NO")
    else:
        print("YES")
        print(k, r)
