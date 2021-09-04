a, b, c = map(int, input().split(" "))
if a == b:
    print(c * 2 + a * 2)
else:
    print(c * 2 + min(a, b) * 2 + 1)
