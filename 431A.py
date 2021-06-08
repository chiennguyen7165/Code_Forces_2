a = list(map(int, input().split(" ")))
s = input()
tong = 0
a1 = a[0]
a2 = a[1]
a3 = a[2]
a4 = a[3]
for i in s:
    if(i =="1"):
        tong += a1
    elif(i =="2"):
        tong += a2
    elif (i=="3"):
        tong += a3
    else:
        tong += a4
print(tong)