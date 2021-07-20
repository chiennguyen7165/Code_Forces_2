t = int(input())
for i in range (0, t):
    x, y, z = map(int,input().split(" "))
    flag = 0
    if x == y and y == z:
        print("YES")
        print(x, y, z)
    elif x == y and y > z:
        print("YES")
        print(x, z, z)
    elif x == z and z > y:
        print("YES")
        print(y, x, y)
    elif y == z and z > x:
        print("YES")
        print(x, x, y)
    else:
        print("NO")