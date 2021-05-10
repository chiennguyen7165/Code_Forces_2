inp = input().split(" ")
n = int(inp[0])
k = int(inp[1])
total = 0
time = list()
for i in range(0, n):
    time = (i+1) * 5 
    k = k + time
    if(k <= 240):
        total += 1
print(total)