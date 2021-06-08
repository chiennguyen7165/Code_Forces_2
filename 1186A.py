ip = list(map(int, input().split(" ")))
n = ip[0]
m = ip[1]
k = ip[2]
if(m >= n and k >= n):
    print("YES")
else:
    print("NO")