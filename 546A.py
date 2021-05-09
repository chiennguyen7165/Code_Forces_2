ip = list(input().split(" "))
sum = 0
for i in range(1, int(ip[2])):
    sum += i
if((int(ip[0])* (int(ip[2])+ sum) - int(ip[1]))< 0):
    result = 0
else:
    result = int(ip[0])* (int(ip[2])+ sum) - int(ip[1])
print(result)
