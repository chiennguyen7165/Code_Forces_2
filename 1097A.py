table = input()
hand = input().split(" ")
table1 = table[0]
table2 = table[1]
hand1 = []
hand2 = []
for item in hand:
    hand1.append(item[0])
    hand2.append(item[1])
temp1 = 0
temp2 = 0
for h1 in hand1:
    if(table1 == h1):
        temp1 += 1
if(temp1 >= 1):
    print("YES")
else:
    for h2 in hand2:
        if(table2 == h2):
            temp2 += 1
    if(temp2 >= 1):
        print("YES")
    else: print("NO")