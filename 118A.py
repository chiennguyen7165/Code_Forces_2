ip = input().lower()
vowels = ["a", "o", "y", "e", "u", "i"]
r = []
for i in ip:
    if i in vowels:
        continue
    else:
        r.append(i)
re = ".".join(letter for letter in r)
print("." + re)
