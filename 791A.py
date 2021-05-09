ip = list(input().split(" "))
limak = int(ip[0])
bo = int(ip[1])
i = True
year = 0
while(i):
    year +=1
    limak = limak * 3
    bo = bo * 2
    if(limak > bo):
        i = False
print(year)   