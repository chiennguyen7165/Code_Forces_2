n, k = map(int, input().split(" "))
p = list(map(int, input().split(" ")))
counter = 0
check = 1
for i in p:
    if i > k:
        check = 0
        break
    else:
        counter += 1
if check == 0:
    for j in reversed(p):  
        if j > k:
            break
        else:
            counter += 1
print(counter)      

