t = int(input())
for i in range (0, t):
    n = int(input())
    b = list(map(int, input().split(" ")))
    if (n == 1):
        print(b[0])
    elif(n == 2):
        print(b[0], b[1])
    elif(n == 3):
        print(b[0], b[2], b[1])
    else:
        turn = int(n /2)
        lst = []
        for i  in range (0, turn):
            start = b[0]
            end = b[-1]
            lst.append(start)
            lst.append(end)
            b.remove(start)
            b.reverse()
            b.remove(end)
            b.reverse()
        if len(b) % 2 == 0:
            print(" ".join(str(x) for x in lst))
        else:
            print(" ".join(str(x) for x in lst), b[0])