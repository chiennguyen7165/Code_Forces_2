lstMatrix = list()
for i in range (0, 5):
    lstMatrix.append(input())

row = 0
col = 0
mainRow = tuple()

# the number of step for row moventment
if (lstMatrix[0] != '0 0 0 0 0' or lstMatrix[4] != '0 0 0 0 0'):
    row = 2
elif (lstMatrix[1] != '0 0 0 0 0' or lstMatrix[3] != '0 0 0 0 0'):
    row = 1
else:
    row = 0

# get the row have the number 1
for rowMatrix in lstMatrix:
    if(rowMatrix == '0 0 0 0 0'):
        continue
    else:
        mainRow = rowMatrix.split(" ")

# the number of steps for col movement
if (mainRow[0] == '1' or mainRow[4] == '1'):
    col = 2
elif (mainRow[1] == '1' or mainRow[3] == '1'):
    col = 1
else:
    col = 0
print(row + col)