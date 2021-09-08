n = int(input())
s = list(map(int, input().split(" ")))
for i in range(0, s.count(0)):
    s.remove(0)

print(len(set(s)))