p = input()
check = ["H", "Q", "9"]
flag = 0
for i in p:
    if i in check:
        print("YES")
        flag = 1
        break
if flag == 0: print("NO")
