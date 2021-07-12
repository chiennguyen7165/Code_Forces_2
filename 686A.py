n, x = map(int, input().split(" "))
k = 0
for i in range(0, n):
    ip = input().split(" ")
    s = ip[0]
    ice = ip[1]
    if(s == "+"):
        x = x + int(ice)
    else:
        if(int(ice) > x):
            k += 1
        else:
            x = x - int(ice)
print(x, k)
