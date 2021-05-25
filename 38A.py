n = int(input())
y = list(map(int, input().split(" ")))
ab = list(map(int, input().split(" ")))
a = ab[0]
b = ab[1]
tong = 0
for i in range (1, len(y) + 1):
    if (a == i):
        for j in range (a, b):
            tong += y[j - 1]
print(tong)
