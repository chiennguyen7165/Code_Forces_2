n = int(input())
s = input().split()
if len(s) == 1:
    sum = 0
    for i in s[0]:
        if i.isupper():
            sum += 1
    print(sum)
else:
    sumL = []
    temp = 0
    for item in s:
        for i in item:
            if i.isupper():
                temp += 1
        sumL.append(temp)
        temp = 0
    print(max(sumL))