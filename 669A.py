n = int(input())
soLan = int(n / 3)
conLai = n - soLan * 3
if conLai % 3 == 0:
    print(soLan * 2)
else: print(soLan * 2 + 1)
