n = int(input())
a = 0
b = 0
if(n % 2 == 0):
    a = 6
    b = n - 6
else:
    a = 9
    b = n - 9
print(a, b)