def minMove(a, b):
    clockright = abs(ord(b) - ord(a))
    clockleft = abs(26 - clockright)
    return min(clockleft, clockright)

ip = input()
r = minMove("a", ip[0])
for i in range(0, len(ip)):
    if(i == len(ip) - 1):
        continue
    else:
        r += minMove(ip[i], ip[i+1])
print(r)

