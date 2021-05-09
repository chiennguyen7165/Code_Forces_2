n = input()
count = 0
for c in n:
    if (c == '4' or c == '7'):
        count += 1
if (count == 4 or count == 7):
    print("YES")
else:
    print("NO")