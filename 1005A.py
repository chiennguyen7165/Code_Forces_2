n = int(input())
a = input()
# a = list(map(int, input().split()))
r1 = 0
lstA = list(map(int, a.split()))
for item in lstA:
    if item == 1:
        r1 += 1
r2 = []
lstA.append(1)
for i in range(0, n):
    if lstA[i + 1] == 1:
        r2.append(lstA[i])
print(r1)
print(" ".join(str(x) for x in r2))
