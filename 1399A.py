t = int(input())
arr = list()
n = 0
answer = ""
for i in range(0, t):
    n = int(input())
    a = set(map(int, input().split(" ")))
    b = list(a).copy()
    b.sort(reverse=True)
    print(b)
    if(len(b) == 1):
        answer = "YES"
    else:
        check = 0
        tong = 0
        for j in range(0, len(b) - 1):
            if( b[j] - b[j+1] == 1):
                check = 0
            else:
                check = 1
            tong += check
        if(tong == 0):
            answer = "YES"
        else:
            answer = "NO"
    arr.append((answer))
for i in arr:
    print((i))