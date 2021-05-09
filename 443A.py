x = input()[1:-1]
if x == "":
    print(0)
else:
    print(len(set(x.split(", "))))
