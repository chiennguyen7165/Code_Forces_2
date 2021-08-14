t = int(input())
for i in range(0, t):
    px, py = map(int, input().split())
    order = input()
    soR = 0
    soL = 0
    soU = 0
    soD = 0
    if px > 0:
        soR = px
    if px < 0:
        soL = -px
    if py > 0:
        soU = py
    if py < 0:
        soD = -py
    # print(soR, soL, soU, soD, sep="-")
    oR = order.count("R")
    oL = order.count("L")
    oU = order.count("U")
    oD = order.count("D")
    check = 0
    if oR >= soR:
        check += 1
    if oL >= soL:
        check += 1
    if oU >= soU:
        check += 1
    if oD >= soD:
        check += 1
    if check == 4:
        print("YES")
    else:
        print("NO")
