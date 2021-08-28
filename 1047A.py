n = int(input())
soDau = 1
soThuHai = 1
soThuBa = n - 1 - 1
if soThuBa % 3 == 0:
    soDau += 1
    soThuBa -= 1
print(soDau,soThuHai,soThuBa)