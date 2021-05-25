def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


ip = list(map(int, input().split(" ")))
m = ip[0]
n = ip[1]
snt = m

check = True
while(check):
    snt += 1
    if (is_prime(snt) == True):
        check = False

if(snt == n):
    print("YES")
else:
    print("NO")
