def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

ip = input().split(" ")
a = int(ip[0]) # Simon
b = int(ip[1]) # Antisimon
stones = int(ip[2]) # stones

check = True
win = ""
while(check):
    print("_________________________________")
    aStone = uscln(a, stones)
    print("số đá simon lấy: ",aStone)
    print("số đá trước khi trừ: ", stones)
    if(aStone <= stones):
        stones = stones - aStone
        print("số đá sau khi trừ: ", stones)
    else:
        win = "Antisimon"
        break
    bStone = uscln(b, stones)
    print("số đá antisimon lấy", bStone)
    print("số đá trước khi trừ: ", stones)
    if(bStone <= stones):
        stones = stones - bStone
        print("số đá sau khi trừ: ",stones)
    else:
        win = "Simon"
        break
if(win == "Simon"):
    print(0)
else: print(1)