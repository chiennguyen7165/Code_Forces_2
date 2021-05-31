ip = list(map(int, input().split(" ")))
d1 = ip[0]
d2 = ip[1]
d3 = ip[2]
r = 0
r = min(d1 + d1 + d2 + d2, min(d1 + d2 + d3, min(d1 + d1 + d3 + d3, d2 + d2 + d3 +d3)))
print(r)