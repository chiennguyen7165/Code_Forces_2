w = list(input().split(" "))
p = int(w[0])
s = int(w[1])
q = input()
for second in range (0, s):
    q = q.replace('BG','GB')
print (q)