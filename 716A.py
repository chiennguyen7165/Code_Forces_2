n, c = map(int, input().split(" "))
s = list(map(int, input().split(" ")))
counter = 1
for i in range(0, n):
    if i == n - 1:
        break
    else:
        # print("%d - %d" % (s[i+1], s[i]))
        if s[i + 1] - s[i] <= c:
            counter += 1
        else: counter = 1
print(counter)