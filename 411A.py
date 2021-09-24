# so 48 - 57
# hoa 65 - 90
# thuong 97 - 122
pas = input()
check = 0
if len(pas) < 5:
    print("Too weak")
else:
    checkLen = True
    checkNum = False
    checkUp = False
    checkLow = False
    for i in pas:
        if ord(i) in range(48, 58):
            checkNum = True
        if ord(i) in range(65, 91):
            checkUp = True
        if ord(i) in range(97, 123):
            checkLow = 1
        if checkNum == True and checkUp == True and checkLow == True:
            break
    if checkNum == True and checkUp == True and checkLow == True:
        print("Correct")
    else:
        print("Too weak")
