n = int(input(""))
arr = list(map(int, input().split(" ")))
tong = 0
for i in range(0, n):
    if i == n - 1:
        break
    elif i == 0:
        continue
    else:
        if (arr[i] > arr[i - 1] and arr[i] > arr[i+1]) or (arr[i] < arr[i - 1] and arr[i] < arr[i+1]):
            tong += 1
print(tong)
