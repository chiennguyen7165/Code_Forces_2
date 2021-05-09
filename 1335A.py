n = int(input())
lst = []
for i in range (0, n):
    o = int(input())
    if(o <=2):
        o = 0
    elif(o % 2 == 0):
        o = int(o/2) - 1
    else:
        o = int(o / 2)
    lst.append(o)
for i in lst:
    print(i)
    
