n = int(input())
temp = []
tt= []
r = ""
if(n == 1 or n % 2 !=0):
    print(-1)
else:
    for i in range(1, n + 1):
        temp.append(i)
        if(len(temp) == 2):
            tt.append(temp)
            temp = []
for item in tt:
    item.sort(reverse=True)
    r += str(item[0]) + " " + str(item[1]) + " "
print (r[0:-1])