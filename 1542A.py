t = int(input())
for i in range(0, t):
    n = int(input())
    s = list(map(int, input().split(" ")))
    soLe = 0
    for item in s:
        if item % 2 != 0:
            soLe += 1
    if soLe == n:
        print("Yes")
    else: print("No")