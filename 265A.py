stone = input()
instr = input()
viTri = 1
for i in range(0, len(instr)):
    if instr[i] == stone[0]:
        viTri += 1
        stone = stone[1::]
    else:
        continue
print(viTri)