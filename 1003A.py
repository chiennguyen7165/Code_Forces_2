n = int(input())
a = list(map(int, input().split(" ")))
aNoDulicate = list(set(a))
khac = []
counter = []
if(len(set(a)) == n):
    print(1)
elif(len(set(a)) == 1):
    print(n)
else:
    for number in aNoDulicate:
        if a.count(number) != 1:
            khac.append(number)
    for number in khac:
        counter.append(a.count(number))

    print(max(counter))