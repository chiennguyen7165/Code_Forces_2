n = int(input())
lstTeam = []
count = 0
for i in range (0, n):
    x = list(input().split(" "))
    lstTeam.append(x)
print("List TEAM:", lstTeam)
lstTemp = lstTeam.copy()
print("List TEMP:", lstTemp)
for i in lstTeam:
    temp = i
    print("Temp: ", temp)
    print("List TEAM before List TEMP remove:", lstTeam)
    lstTemp.remove(temp)
    print("List TEAM after List TEMP remove:", lstTeam)
    print("List TEMP after remove: ", lstTemp)
    for j in lstTemp:
        if(temp[0] == j[1]):
            count += 1
    print("List TEAM to refull:", lstTeam)
    lstTemp = lstTeam.copy()
    print("List TEMP after refull:", lstTemp)
print(count)
            