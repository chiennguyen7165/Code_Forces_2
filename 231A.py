w = int(input())

lstSolution = list()
result = 0
for i in range(0, w):
    line = input()
    tempTupe = line.split(" ")
    lstSolution.append(tempTupe)

for s in lstSolution:
    if((int(s[0]) + int(s[1]) + int(s[2])) >=2):
        result += 1
print (result)