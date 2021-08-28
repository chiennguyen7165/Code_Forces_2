q = int(input())
for i in range(0, q):
    n, a, b = map(int, input().split(" "))
    if n % 2 == 0:
        if a<=int(b/2):
            print(a * n)
        else:
            print(int(b * n * 0.5))
    else:
        if a<=int(b/2):
            print(a * (n - 1) + a)
        else:
            print(int(b * (n-1) * 0.5 + a))

    