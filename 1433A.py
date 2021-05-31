t = int(input())
r = []
for i in range(0, t):
    n = input()
    le = 0
    if(len(n) == 4):
        le = 10
    elif(len(n) == 3):
        le = 6
    elif(len(n) == 2):
        le = 3
    else: 
        le = 1
    temp = (int(n[0]) - 1)  * 10 + le
    r.append(temp)
for item in r:
    print(item)