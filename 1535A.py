t = int(input())
for i in range(0, t):
    players = list(map(int, input().split(" ")))
    win1 = max(players[0], players[1])
    lose1 = min(players[0], players[1])
    win2 = max(players[2], players[3])
    lose2 = min(players[2], players[3])
    third = max(lose1, lose2)
    if(third > win1 or third > win2):
        print("NO")
    else: print("YES")