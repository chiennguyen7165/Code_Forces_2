n = int(input())
a =list(input().split(" "))
p = 0
for i in a:
    if(i =='1'):
        p += 1
    else:
        continue
if(p == 0):
    print("EASY")
else:
    print("HARD")