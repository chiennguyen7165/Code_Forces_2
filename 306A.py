n, m = map(int, input().split())
r = []
bandau = int(n / m)
conlai = n % m
for i in range(0, m - conlai):
    r.append(bandau)
for i in range(0, conlai):
    r.append(bandau + 1)
print(" ".join(str(x) for x in r))
