stone = {
    'purple': 'Power',
    'green' : 'Time',
    'blue' : 'Space',
    'orange' : 'Soul',
    'red' : 'Reality',
    'yellow' : 'Mind'
}

n = int(input())
for i in range(0 ,n):
    k = input()
    del stone[k]

print(6 - n)
for index in stone:
    print(stone[index])
