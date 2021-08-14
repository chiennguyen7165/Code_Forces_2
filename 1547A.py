t = int(input())
for i in range(0, t):
    spcae = input()
    xA, yA = map(int, input().split())
    xB, yB = map(int, input().split())
    xF, yF = map(int, input().split())
    
    if xA == xB and xA == xF and xF == xB:
        if min(yA,yB) < yF < max(yA, yB):
            print(abs(yA - yB) + 2)
        else:
            print(abs(yA - yB))
    elif yA == yB and yA == yF and yF == yB:
        if min(xA,xB) < xF < max(xA, xB):
            print(abs(xA - xB) + 2)
        else:
            print(abs(xA - xB))
    else:
        print(abs(yA - yB) + abs(xA - xB))