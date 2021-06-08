t = int(input())
result = []
for i in range(0, t):
    s = int(input())
    if(s < 3):
        result.append(1)
    elif((s - 1) % 2 == 1):
        result.append((s - 2) / 2 + 1)
    else:
        result.append((s - 1)  / 2 + 1)
for item in result:
    print(int(item))