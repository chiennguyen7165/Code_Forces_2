n = int(input())
tong = 0
for i in range (0, n):
    x = input()
    if(x[0] == "T"):
        tong += 4
    if(x[0] == "C"):
        tong += 6
    if(x[0] == "O"):
        tong += 8
    if(x[0] == "D"):
        tong += 12
    if(x[0] == "I"):
        tong += 20
print(tong)