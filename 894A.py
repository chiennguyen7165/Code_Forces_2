s = input()
counter = 0
countA = s.count("A")
for i in range(0, countA):
    temp = s.split("A",1)
    right = temp[0].count("Q")
    left = temp[1].count("Q")
    counter += right * left
    t = s.replace("A", "B", 1)
    s = t
print(counter)