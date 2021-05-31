result = []
t = int(input())
for i in range(0, t):
    n = int(input()) 
    if(n % 2 == 0):
        result.append(int(n / 2))
    else:
        result.append(int((n - 1) / 2))
for item in result:
    print(item)