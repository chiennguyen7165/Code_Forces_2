t = int(input())
for i in range (0, t):
    n = int(input())
    s = input()
    lengths = 2 * n - 1
    if n == 1:
        print(s)
    else:
        count = s.count("0")
        if count == 0 or count == lengths:
            print(s[0] * n)
        else:
            r = ""
            i = 0
            while i < lengths:
                r += s[i]
                i += 2
            print(r)
