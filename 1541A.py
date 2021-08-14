t = int(input())
for i in range(0, t):
    n = int(input())
    if n == 2:
        print(2, 1)
    elif n == 3:
        print(3, 1, 2)
    else:
        order = []
        for i in range(1, n + 1):
            order.append(i)
        if n % 2 == 0:
            r = list(map(lambda x: x-1 if x % 2 ==0 else x+1, order))
            print(" ".join(str(x) for x in r))
        else:
            order.remove(3)
            order.remove(2)
            order.remove(1)
            r = list(map(lambda x: x+1 if x % 2 ==0 else x-1, order))
            r.insert(0,2)
            r.insert(0,1)
            r.insert(0,3)
            print(" ".join(str(x) for x in r))
            