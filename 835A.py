s, v1, v2, t1, t2 = map(int,input().split(" "))
b1 = t1 + v1 * s + t1
b2 = t2 + v2 * s + t2
if b1 == b2:
    print("Friendship")
elif b1 > b2:
    print("Second")
else:
    print("First")