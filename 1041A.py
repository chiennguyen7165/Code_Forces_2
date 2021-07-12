n = int(input())
ip = list(map(int, input().split(" ")))
print(max(ip) - min(ip) - n + 1)