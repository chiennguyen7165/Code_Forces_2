t = int(input())
for i in range(0, t):
    n = input()
    if(1 <= int(n) <= 9):
        print(n)
    else:
        doDai = len(n)
        stock = (doDai - 1) * 9
        soDauTien = n[0]
        soNhapVao = int(n)
        soGanNhat = int(soDauTien * doDai)
        if soNhapVao >= soGanNhat:
            print(stock + int(soDauTien))
        else:
            print(stock + int(soDauTien) - 1)