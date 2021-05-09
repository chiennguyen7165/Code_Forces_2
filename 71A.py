w = int(input())
lstInput = list()
for t in range(0,w):
    lstInput.append(input())

for word in lstInput:
    if(len(word) <= 10):
        print(word)
    else:
        print(word[0] + str(len(word)-2) + word[-1])