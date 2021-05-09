i = input().split(" ")
a = int(i[0])
b = int(i[1])
if(a - b < 0):
    miN = a
    maX = b
else:
    miN = b
    maX = a
print(miN, int((maX - miN) / 2))
