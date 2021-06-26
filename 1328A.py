t = int(input())
for t in range (0, t):
    ip = list(map(int, input().split(" ")))
    a = ip[0]
    b = ip[1]
    if(a % b == 0):
        print(0)
    elif(a < b):
        print(b - a)
    else:
        print(b - (a %b))