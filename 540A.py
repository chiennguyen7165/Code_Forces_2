n = int(input())
state = input()
key = input()
tong = 0
for i in range(0, n):
    temp = 0
    right = abs(ord(state[i]) - ord(key[i]))
    left = 10 - abs( ord(key[i]) - ord(state[i]))
    # print("right: ",right )
    # print("left: ", left)
    temp = min(right,left)
    # print(temp)
    tong += temp
print(tong)