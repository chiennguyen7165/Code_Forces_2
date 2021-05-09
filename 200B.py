n = int(input())
p = list(input().split(" "))
cam = 0
nuoc = 0
for i in p:
    cam += int(i)
    nuoc += (100 - int(i))
print(100*(cam / (cam + nuoc)))