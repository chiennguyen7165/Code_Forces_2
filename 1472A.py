t = int(input())
for i in range (0, t):
    w, h, n = map(int, input().split(" "))
    if n == 1:
        print("YES")
    elif w % 2 != 0 and h % 2 != 0:
        print("NO")
    else:
        pieces = w * h
        count = 0
        while pieces % 2 == 0:
            pieces = pieces / 2
            count += 1
        if 2 ** count >= n:
            print("YES")
        else: print("NO")