n = int(input())
s = list(map(int, input().split(" ")))
tong = 0
for i in s:
    tong += max(s) - i
print (tong)