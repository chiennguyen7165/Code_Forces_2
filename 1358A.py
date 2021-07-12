t = int(input())
for i in range (0, t):
    ip = list(map(int, input().split(" ")))
    n = ip[0]
    m = ip[1]
    print(int((n * m / 2) + (n * m % 2)))