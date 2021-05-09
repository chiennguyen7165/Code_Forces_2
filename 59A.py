w = input()
upper = 0
lower = 0
for c in w:
    if(c.isupper() == True):
        upper += 1
    else:
        lower += 1
if(upper > lower):
    print(w.upper())
else:
    print(w.lower())