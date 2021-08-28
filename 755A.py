def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
n = int(input())
check = True
m = 1
while check:
    r = n * m + 1
    if is_prime(r) == False:
        print(m)
        check = False
    else:
        m += 1
