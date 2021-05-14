n = int(input())
r = list()
tt = 1
for i in range (0, n):
    x = input()
    y = ""
    for i in x[1:-1]:
        if(tt % 2 != 0):
            y += i
        tt += 1
    r.append(x[0]+y +x[-1])
for item in r:
    print(item)