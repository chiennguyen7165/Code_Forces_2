x = 0
n = int(input())
lstStatement = list()
for i in range (0, n):
    lstStatement.append(input()[1])

for j in lstStatement:
    if(j == '+'):
        x += 1
    if(j == '-'):
        x -= 1

print(x)