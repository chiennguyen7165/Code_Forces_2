n = int(input())
soCach = 0
for i in range(1, n + 1) :
    soNV = n - i
    if(soNV % i == 0):
        soCach += 1
print(soCach  - 1)
