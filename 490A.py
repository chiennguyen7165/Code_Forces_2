n = int(input())
d = [[],[],[]]
t = list(map(int, input().split(" ")))
for index, value in enumerate(t): 
    d[value-1].append(index+1)
print(min(map(len, d)))
for a in zip(*d):
    print(a[0], a[1], a[2])