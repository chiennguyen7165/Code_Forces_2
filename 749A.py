n = int(input())
r = ""
k = 0
check = True
if(n % 2 == 0):
    k = int(n / 2)
    r = "2 " * k
else:
    k = int((n - 3) / 2) + 1
    r = "3 " + "2 " * (k - 1)
print(k)
print(r)