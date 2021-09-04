n, k = map(int, input().split(" "))
p = ""
for i in range(0, k):
    p += chr(97 + i)

soLan = int(n / k)
pas = p * soLan

conLai = n - soLan * len(p)
for i in range(0, conLai):
    pas += chr(97 + i)
print(pas)
# print(len(pas) == n)
    
