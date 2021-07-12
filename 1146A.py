s = input()
soA = s.count("a")
if soA > len(s) / 2:
    print(len(s))
else:
    soKhacA = len(s) - soA
    print(2 *soA - 1)
