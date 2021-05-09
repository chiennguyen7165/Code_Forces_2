x1 = input()
x2 = input()
x3 = input()
x = x1 + x2
listN = list()
listX = list()
for i in x:
    listN.append(i)
listN.sort()
print(listN)
for i in x3:
    listX.append(i)
listX.sort()
print(listX)
if(listN == listX):
    print("YES")
else:
    print("NO")