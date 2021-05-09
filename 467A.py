w = int(input())
lstInput = list()
r = 0
for i in range (0, w):
    lstInput.append(input().split(" "))
for i in range(0, w):
    if(int(lstInput[i][1])- int(lstInput[i][0]) >=2):
        r += 1
print(r)