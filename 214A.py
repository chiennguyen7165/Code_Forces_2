ip = list(map(int, input().split(" ")))
n = ip[0]
m = ip[1]
count = 0
a = 0
b = 0
for i in range(0, m*m + 1):
    b = i
    a = m - b*b
    if(a*a + b == n and a >=0 ):
        count += 1

print(count)


#tham khảo https://mysolutions4you.wordpress.com/2018/10/25/codeforces-sloution-214a-system-of-equations/