c = list(map(int, input().split(" ")))
c.sort()
print(c[1] - c[0] + c[2] - c[1])