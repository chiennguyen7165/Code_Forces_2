n, k = map(int, input().split(" "))
i = 1
if k == 1:
    print(n + 1)
else:
    check = True
    while check:
        if k * i > n:
            print(k * i)
            break
        else:
            i += 1
