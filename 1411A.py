t = int(input())
for i in range(0, t):
    n = int(input())
    s = input()
    bad = 0
    for j in reversed(s):
        if j != ")":
            break
        else:
            bad += 1
    if bad > n - bad:
        print("YES")
    else: print("NO")