t = int(input())
a = list()
for i in range(0, t):
    a.append(int(input()))
for i in a:
    if i % 4 > 0:
        print("No")
    else:
        print("Yes")
        number = int(i/2)
        sum1 = 0
        sum2 = 0
        for j in  range(0, number):
            sum1 += j * 2 + 2
            print(j * 2 + 2, end = " ")
        for k in range(0, number - 1):
            sum2 += k * 2 + 1
            print(k * 2 + 1, end = " ")
        print(sum1 - sum2)