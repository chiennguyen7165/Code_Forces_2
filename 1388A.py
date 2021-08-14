t = int(input())
for i in range(0, t):
    n = int(input())
    so1 = 2
    so2 = 6
    so3 = 10
    so4 = 14
    so5 = 15
    if  n <= 30:
        print("NO")
    else:
        print("YES")
        if n == 36 or n == 40 or n == 44:
            print(so2, so3, so5, n - 31)
        else:
            print(so2, so3, so4, n - 30)
    