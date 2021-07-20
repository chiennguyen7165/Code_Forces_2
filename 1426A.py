t = int(input())
for i in range (0, t):
    n, x = map(int, input().split(" "))
    if n == 1 or n == 2:
        print(1)
    elif 3 <= n <= x + 2:
        print(2)
    else:
        check = True
        i = 0
        while (check):
            start = (i + 1) * x + 3
            end = (2 + i) * x + 2
            if n in range(start, end + 1):
                print(i + 3)
                check = False
            else:
                i += 1
