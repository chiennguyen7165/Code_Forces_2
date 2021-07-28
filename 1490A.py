t = int(input())
for i in range (0, t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    result = 0
    for tt in range(0, n):
        if tt == n - 1:
            break
        else:
            count = 0
            maX = max(a[tt], a[tt+1])
            miN = min(a[tt], a[tt+1])
            if maX / miN <= 2:
                continue
            else:
                check = True
                while check:
                    miN = miN * 2
                    if miN >= maX:
                        check = False
                    else:
                        count += 1
                result += count
    print(result)
                    
                    