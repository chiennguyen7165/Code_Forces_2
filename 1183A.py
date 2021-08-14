n = int(input())
tong = 0
a = 0
for i in range(0, 10):
    a = n + i
    for j in str(a):
        tong  += int(j)
    if(tong % 4 == 0):
        print(a)
        break
    else: tong = 0