n = int(input())
inputs = list(map(int, input().split(" ")))
count = 0
temp = list()
for i in range(0, n):
    temp = inputs[0:i+1].copy()
    if i == n - 1:
        continue
    if(inputs[i + 1] > max(temp) or inputs[i + 1] < min(temp)):
        count += 1
print(count)