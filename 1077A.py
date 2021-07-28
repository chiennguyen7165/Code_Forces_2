t = int(input())
for i in range (0, t):
    a, b, k = map(int, input().split(" "))
    aX = 0
    bX = 0
    if k % 2 == 0:
        aX = int(k / 2)
        print(aX * a - aX * b)
    else:
        aX = int(k / 2) + 1
        bX = k - aX
        print(aX * a - bX * b)