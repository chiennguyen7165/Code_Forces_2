import math
a1, a2, a3 = map(int, input().split(" "))
b1, b2, b3 = map(int, input().split(" "))
n = int(input())
soNganCup = 0
soNganMedal = 0
cup = a1 + a2 + a3
medal = b1 + b2 + b3
if(cup == 0): soNganCup = 0
elif(cup <= 5): soNganCup = 1
else: soNganCup = math.ceil(cup/5)

if(medal == 0): soNganMedal = 0
elif(medal <=10): soNganMedal = 1
else: soNganMedal = math.ceil(medal/10)

if n >= soNganCup + soNganMedal: print("YES")
else: print("NO")