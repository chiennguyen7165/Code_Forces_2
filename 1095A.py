def deSum(r):
    counter = 0
    tempSum = 0
    check = True
    i = 1
    while(check):
        tempSum += i
        counter += 1
        if(tempSum == r):
            check = False
        i += 1
    return counter

n = int(input())
p = input()
doDaiChuoi = deSum(n)
chuoiBanDau = ""
for i in range(1, doDaiChuoi + 1):
    chuoiTemp = p [0:i]
    chuoiSauKhiCat = p[i::]
    p = chuoiSauKhiCat
    chuoiBanDau += chuoiTemp[0]
print(chuoiBanDau)