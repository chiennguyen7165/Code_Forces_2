s = list(input().rstrip("?").split(" "))
s.reverse()
for i in s:
    if i != '':
        if(i[-1].lower() == 'a' or i[-1].lower() == 'e' or i[-1].lower() == 'i' or i[-1].lower() == 'o' or i[-1].lower() == 'u' or i[-1].lower() == 'y'):
            print("YES")
        else:
            print("NO")
        break