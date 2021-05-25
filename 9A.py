a = list(map(int, input().split(" ")))
tuso = 6 - max(a) + 1
if (tuso == 2): r = "1/3"
if (tuso == 3): r = "1/2"
if (tuso == 4): r = "2/3"
if (tuso == 1): r = "1/6"
if (tuso == 5): r = "5/6"
if (tuso == 6): r = "1/1"
print(r)