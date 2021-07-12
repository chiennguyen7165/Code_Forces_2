a, b = map(int, input().split(" "))
s1 = 0
s2 = 0
s3 = 0
for i in range(1, 7):
    if abs(i - a) > abs(i-b):
        s3 += 1
    elif abs(i - a) < abs(i -b):
        s1 += 1
    else:
        s2 += 1
print(s1,s2,s3)