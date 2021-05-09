i = input().split(" ")
n = int(i[0])
m = int(i[1])
o = ""
for i in range(1, n+1):
    if(i % 2 != 0):
        o = "#" * m
    else:
        o = "." * (m - 1 ) + "#"    
    if(i % 4 == 0):  
        print(o[::-1])
    else:
        print(o)
        