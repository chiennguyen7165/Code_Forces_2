n = int(input())
check = 0
bus = []
done = 0
for i in range(0, n):
    row = input()
    rowSlice = row.split("|")
    if(done == 1):
        bus.append(row)
    else:
        if rowSlice[0] == "OO" or rowSlice[1] == "OO":
            rowM = row.replace("OO","++",1)
            bus.append(rowM)
            check = 1
            done = 1
        else:
            bus.append(row)
if(check == 1):
    print("YES")
    for line in bus:
        print(line)
else:
    print("NO")
