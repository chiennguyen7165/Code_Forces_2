n = int(input())
giua = int(n / 2)
d = 1
for i in range(0, n):
    diamond = ""
    diamond += "D" * (d)
    side = "*" * int((n - len(diamond)) / 2)
    line = side + diamond + side
    print(line)
    if i > giua - 1:
        d -= 2
    else:
        d += 2
