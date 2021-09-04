n, t = map(int, input().split(" "))
work = list(map(int, input().split(" ")))
sum = 1
read = 0
for time in work:
    left = 86400 - time
    if t - read <= left:
        break
    else:
        sum += 1
        read += left
print(sum)