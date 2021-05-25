n = int(input())
so = input()
dk1 = 0
tong = 0
for i in so:
    tong += int(i)
    if(int(i) != 4 and int(i) != 7):
        dk1 += 1    
if(dk1 != 0):
    print("NO")
else:
    tong1 = 0
    for j in range(0, int(n/2)):
        tong1 += int(so[j])
    if(tong1 * 2 == tong):
        print("YES")
    else: print("NO")