s=""
for i in range(0, 3):
	s+=input()

print("YES") if s==s[::-1] else print("NO")