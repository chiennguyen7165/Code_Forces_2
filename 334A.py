w = int(input())
c1 = ''
count = 0
for i in range(0,w):
    c1 += input()
    if (c1[-2::] != c1[-4:-2]): 
        count += 1
print(count)