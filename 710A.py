ip = input()
if ip in ["a8", "a1", "h8", "h1"]:
    print(3)
elif ip[-1] in ["1", "8"] or ip[0] in ["a", "h"]:
    print(5)
else:
    print(8)