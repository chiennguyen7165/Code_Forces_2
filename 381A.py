n = int(input())
s = 0
d = 0
if(n % 2 == 0):
    turn = int(n / 2)
else: turn = int((n -1) /2)
card = list(map(int, input().split(" ")))
for i in range(0, turn):
    dau = card[0]
    cuoi = card[-1]
    turnS = max(dau, cuoi)
    s += turnS
    if(turnS == dau): 
        card.remove(dau)
        dauMoi = card[0]
        turnD = max(cuoi, dauMoi)
        d += turnD
    else: 
        card.remove(cuoi)
        cuoiMoi = card[-1]
        turnD = max(dau, card[-1])
        d += turnD
    card.remove(turnD)
if(n % 2 == 0): print(s, d)
else: print(s + card[0], d)

