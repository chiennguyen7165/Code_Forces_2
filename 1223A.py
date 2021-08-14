t = int(input())
for i in range (0, t):
    n = int(input())
    miN = 4
    if n < 4:
        print(4 - n)
    elif n % 2 == 0:
        print(0)
    else: print(1)