n = int(input())
s = input()
setS = set()
for i in s:
    setS.add(i.lower())
if(len(setS) == 26):
    print("YES")
else:
    print("NO")