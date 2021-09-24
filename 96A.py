ip = input()
r = 0
check = False
temp = ip[0]
for i in ip:
    if i == temp:
        r += 1
    else:
        temp = i
        r = 1
    if r == 7:
        check = True
        break
if check == True: print("YES")
else: print("NO")