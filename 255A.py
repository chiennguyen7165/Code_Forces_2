n = int(input())
sp = list(map(int, input().split(" ")))
chest = 0
biceps = 0
back = 0
for i in range(0, len(sp), 3):
    chest += sp[i]
for i in range(1, len(sp), 3):
    biceps += sp[i]
for i in range(2, len(sp), 3):
    back += sp[i]
if (max(chest, biceps, back) == chest):
    print("chest")
elif(max(chest, biceps, back) == biceps):
    print("biceps")
else:
    print("back")