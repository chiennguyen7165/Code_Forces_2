inputs = list(map(int, input().split(" ")))
k = inputs[0]
r = inputs[1]
i = 1
check = True
while(check):   
    o = i * k 
    if(o % 10 == 0):
        check = False
        print(i)
    else:
        if(str(o)[-1] == str(r)):
            check = False
            print(i)
    i = i + 1