n = input()
x = list(input().split(" "))
y = list(input().split(" "))
setX = set(x[1:])
setY = set(y[1:])
chuoi = setX.union(setY)
if(len(chuoi) == int(n)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")