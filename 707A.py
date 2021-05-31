nm = list(map(int, input().split(" ")))
n = nm[0]
m = nm[1]
check = 0
for i in range (0, n):
    checkHang = 0
    line = input().split(" ")      
    for li in line:
        if(li == "C" or li == "M" or li == "Y"):
            checkHang += 1
    if(checkHang != 0):
        check += 1
if(check == 0):
    print("#Black&White")
else:
    print("#Color")