n = int(input())
team = int(n /2)
s = list(map(int, input().split(" ")))
r = 0
for i in range (0, team):
    maX = max(s)
    s1 = maX
    s.remove(maX)
    maX = max(s)
    s2 = maX
    s.remove(maX)
    r += (abs(s1 - s2))
print(r)
