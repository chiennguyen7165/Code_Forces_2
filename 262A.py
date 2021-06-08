ip = list(map(int, input().split(" ")))
n = ip[0]
k = ip[1]
s = input().split(" ")
r = 0
for i in s:
    soMayMay = i.count("4") + i.count("7")
    if soMayMay <= k:
        r += 1
print(r)