r = list(map(int, input().split(" ")))
r.sort()
a = max(r) - r[0]
b = max(r) - r[1]
c = max(r) - r[2]
print(a, b, c)