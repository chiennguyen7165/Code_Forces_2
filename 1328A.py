t = int(input())
lstC =[]
for i in range(0, t):
    case = input().split(" ")
    x1 = int(case[0])
    x2 = int(case[1])
    while(x1 % x2 != 0):
        x1 = x1 + 1
        count += 1
    lstC.append(count)
for i in lstC:
    print(i)