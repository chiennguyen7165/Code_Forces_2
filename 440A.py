n = int(input())
esp = list(map(int, input().split()))
sum = 0
suM = 0
for i in esp:
    sum += i
for i in range(1, n + 1):
    suM += i
print(suM - sum)
