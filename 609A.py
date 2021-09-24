n = int(input())
m = int(input())
u = []
r = 0
for i in range (0, n):
    u.append(int(input()))
u.sort(reverse=True)
tong = 0
for i in u:
    if tong >= m:
        break
    else:
        tong += i
        r += 1
print(r)
