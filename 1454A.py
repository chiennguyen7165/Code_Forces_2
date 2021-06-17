t = int(input())
for stt in range(0, t):
    n = int(input())
    p = []
    for i in range(1, n+1):
        p.append(i)
    p.sort(reverse = True)
    if(len(p) % 2 == 0):
        print(" ".join(str(x) for x in p))
    else:
        temp = int(n / 2) + 1
        p.remove(temp)
        p.append(temp)
        print(" ".join(str(x) for x in p))