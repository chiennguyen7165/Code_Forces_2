n, m = map(int, input().split(" "))
s = list(map(int, input().split(" ")))
f = list(map(int, input().split(" ")))
r = []
for item in s:
    if item in f:
        r.append(item)
print(" ".join(str(x) for x in r))