n = int(input())
a = list(map(int, input().split(" ")))
listA = list(set(a))
print(len(listA))
for i in range(0, len(listA)):
    counter = a.count(listA[i])
    for j in range(0, counter - 1):
        a.remove(listA[i])
else: print(" ".join(str(r) for r in a))
