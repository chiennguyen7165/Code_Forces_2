n = int(input())
ip = input()
tt= []
temp = 0
for i in ip:  
    if(i == "x"):
        temp += 1
    else:
        tt.append(temp)
        temp = 0
tt.append(temp)
tong = 0
for item in tt:
    if item >= 3:
        tong += (item - 2)
print(tong)

