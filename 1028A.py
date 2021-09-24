n, m = map(int, input().split())
table = []
row = []
for i in range(0, n):
    line = input()
    temp = []
    checkRow = False
    for r in range(0, len(line)):
        if line[r] == "B":
            temp.append(r + 1)
            checkRow = True
    if checkRow == True:
        row.append(i + 1)
    if temp != []:
        table.append(temp)
hang = row[int(len(row) / 2)]
cot = table[0][int(len(table) / 2)]
print(hang, cot)