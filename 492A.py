n = int(input())
i = 0
current = 0
last =0
while(n >0):
    i += 1
    current = last + i
    last = current
    n = n - current
    if(n < 0):
        i -= 1

print(i)
    