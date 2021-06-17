inputT = input()
n = int(inputT[0])
k = int(inputT[-1])
partitionExp = list(map(int, input().split(" ")))
result = 0
partitionRight = 0
for item in partitionExp:
    if(5 - item >= k):
        partitionRight += 1
result = int(partitionRight / 3)
print(result)