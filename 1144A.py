t = int(input())
for i in range(0, t):
    n = input()
    asc = []
    if len(n) == 1:
        print("YES")
    else:
        for l in n:
            temp = ord(l)
            asc.append(temp)
        if len(set(asc)) != len(n):
            print("NO")
        else:
            kc = (max(asc) - min(asc)) / (len(n) - 1)
            if kc == 1.0:
                print("YES")
            else: print("NO")