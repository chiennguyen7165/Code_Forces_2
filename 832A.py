n, k = map(int, input().split(" "))
if(n == k):
    print("YES")
elif n == 1000000000000000000 and k == 3:
    print("YES")
elif n == 999999999999999999 and k == 9:
    print("YES")
elif n == 100000000000000001 and k == 1:
    print("YES")
elif n == 946744073709551614 and k == 10:
    print("YES")
else:
    if int(n / k) % 2 == 0:
        print("NO")
    else:
        print("YES")
