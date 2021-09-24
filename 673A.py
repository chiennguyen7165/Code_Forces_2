n = int(input())
ins = list(map(int, input().split()))
r = []
if ins[0] > 15:
    print(15)
elif n == 1:
    if ins[0] <= 15:
        print(ins[0] + 15)
    else:
        print(15)
else:
    check = 0
    for i in range(0, n):
        if i == n - 1:
            if 90 - ins[i] > 15:
                r.append(ins[i] + 15)
                check = 1
        else:
            if ins[i + 1] - ins[i] > 15:
                r.append(ins[i] + 15)
                check = 1
    if check == 0: print(90)
    else: print(r[0])