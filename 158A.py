ip = input()
tempIp = ip.split(" ")
n = int(tempIp[0])
k = int(tempIp[1])
score = input()
tempTupe = score.split(" ")
result = 0
for s in tempTupe:
    if(int(s) >= int(tempTupe[k-1]) and int(s) > 0):
        result += 1
print(result)