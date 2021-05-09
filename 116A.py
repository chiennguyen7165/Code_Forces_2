n = int(input())
lstOut = list()
lstIn = list()
lstKhach = list()
skIn = 0
skOut = 0
sk = 0
for i in range (0, n):
    line = input().split(" ")
    lstOut.append(int(line[0]))
    lstIn.append(int(line[1]))
soKhach = lstIn[0]
lstKhach.append(soKhach)
for j in range (1, n):
    soKhach = soKhach - lstOut[j] + lstIn[j]
    lstKhach.append(soKhach)

print(max(lstKhach))