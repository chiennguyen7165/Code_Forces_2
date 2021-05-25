so = list(input().split("."))
pNguyen = so[0]
pTP = so[1]
if (int(pNguyen[-1]) == 9):
    print("GOTO Vasilisa.")
else:
    if(int(pTP[0]) >= 5):
        print(int(pNguyen) + 1)
    else:
        print(int(pNguyen))