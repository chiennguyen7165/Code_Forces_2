ip = list(input().split(" "))
so = int(ip[0])
for i in range(0, int(ip[1])):
    if(so % 10 == 0):
        so = so / 10
    else:
        so = so - 1
    if(so < 0):
        so = 0
print(int(so))