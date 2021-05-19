n = int(input())
m = 0
c = 0
for i in range(0, n):
    t = list(map(int, input().split(" ")))
    if(t[0] > t[1]):
        m += 1
    if(t[0] < t[1]):
        c += 1

if (m > c):
    print("Mishka")
elif (m < c):
    print("Chris")
else:
    print("Friendship is magic!^^")
