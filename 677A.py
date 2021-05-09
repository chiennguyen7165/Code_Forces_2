w = input().split(" ")
n = int(w[0])
h = int(w[1])
line = input().split(" ")
result = 0
c = 0
for l in line:
    if(int(l)<=h):
        c = 1
        result = result + c
    if(int(l)>h):
        c = 2
        result = result + c
print(result)


