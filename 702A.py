n = int(input())
arr = list(map(int, input().split(" ")))
result = list()
check = 0
batDau = 1
if(n == 1):
    print(1)
else:
    for i in range(1, n):
        # print("trung hop i = ", i)
        # print("arr[i] = ", arr[i])
        # print("arr[i - 1] = ", arr[i - 1])
        if arr[i] > arr[i - 1]:
            batDau += 1
            # print(batDau)
            if(i == n -1):
                result.append(batDau)
        else:
            # print("Them vao mang")
            result.append(batDau)
            batDau = 1
            # print(batDau)
            # print(result) 
        # print("---------------------------")
    print(max(result))