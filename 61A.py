soa = input()
sob = input()
tong = 0
kq = ''
for i in range (0, len(soa)):
    tong = int(soa[i]) + int(sob[i])
    if(tong == 2):
        kq += '0'
    else:
        kq += str(tong)
print(kq)