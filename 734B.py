ip = list(map(int, input().split(" ")))

so2 = ip[0]
so3 = ip[1]
so5 = ip[2]
so6 = ip[3]

so256 = min(so2, so5, so6)
so32 = 0
if(so2 - so256 > 0):
    so32 = min(so3, so2 - so256)

tong = 256 * so256 + 32 * so32

print(tong)