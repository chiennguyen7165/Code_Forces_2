s = input()
r = []
temp = 0
check = 0
for i in range (0, len(s)):
    if(check == 1):
        check = 0
        pass
    else:
        if s[i] == ".":
            r.append("0")
            check = 0
        else:
            if(i == len(s) - 1):
                continue
            else:
                if s[i+1] == ".":
                    r.append("1")
                    check = 1
                else:
                    r.append("2")
                    check = 1
print("".join(r))
