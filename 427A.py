n = int(input())
c = list(map(int, input().split(" ")))
officer = 0
crime = 0
count = 0
for i in c:
    if i != -1:
        officer += i      
    else:
        crime += 1
        if officer != 0:
            officer = officer - crime
            crime = 0
        else:
            count += 1
    crime = 0
print(count)