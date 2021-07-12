def tinhgiaithua(n):
    giai_thua = 1
    if (n == 0 or n == 1):
        return giai_thua
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua
def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

a, b = map(int,input().split(" "))
print(tinhgiaithua(min(a,b)))