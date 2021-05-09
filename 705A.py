n = int(input())
hate = 'I hate'
love = 'I love'
hulk = list()
for i in range (1, n+1):
    if(i % 2 == 1):
        hulk.append(hate)
    else:
        hulk.append(love)
print(' that '.join(hulk)+' it')
