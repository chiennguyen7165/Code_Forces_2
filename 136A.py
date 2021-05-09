w = int(input())
ip = input().split(" ")
kq = list()
for i in range (0, w):
    kq.append(ip.index(str(i+1)) + 1)
print(' '.join(map(str, kq)))