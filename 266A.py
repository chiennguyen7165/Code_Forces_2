w = int(input())
strString = input()
r = 0
for i in range(0, w-1):
    if(strString[i] == strString[i+1]):
        r += 1
print(r)

