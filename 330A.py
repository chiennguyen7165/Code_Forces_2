# Get rows and cols of the given cake
r, c = map(int, input().split(" "))

# A list to contain the locations of the evil strawberry
lstSbLocation = []

# Complete the list where 1 as the strawberry and 0 as the cell of cake
# for each rows of given cake
for i in range(0, r):
    s = input()  # each rows of the cake
    lstTempRow = [] # a temporary list to contains positions of strawberry and cake  for each row entered
    for j in range(0, c):
        if s[j] == "S": # when catch a strawberry, add 1 to the temporary list
            lstTempRow.append(1)
        else: # when catch a cack, add 0 to the temporary list
            lstTempRow.append(0)
    lstSbLocation.append(lstTempRow) # add list of row to the location list

eattenRow = 0 # variable of eatable rows
lstCopycat1 = lstSbLocation.copy() # create a copy of the location list to comparasion
for sb in lstCopycat1: # Find  eatable rows
    if len(set(sb)) == 1 and sb[0] == 0: # when catch the list (as row) has all zero, adđ the eattenRow by 1
        eattenRow += 1
        lstSbLocation.remove(sb) # and remove this sublist to the mother list
# After that, we have a list jusst cotain the row had strawberry, each row of this list is a sublist 

# In case there is no strawberry, cakeminator can eat the whole cake
if len(lstSbLocation) == 0:
    print(r * c)
else: # In the other hand, we have to find eatable cols 
    lstCopycat2 = lstSbLocation.copy() # create a copy of the location list to comparasion
    lstSbOrder = [] # create a list to contain the order of strawberry of each rows, i.e. each sublist of the lstSbLocation
    for sb in lstCopycat2:
        lstTemp = [] # create a temporary list to contain the order of strawberry 
        for d in range(0, len(sb)):
            if sb[d] == 1: # when catch a strawberry, add its index into temporay list
                lstTemp.append(d)
        lstSbOrder.append(lstTemp) # add the sublist to the order list

    strSbLocation = "" # this string contain all of the index of the starberry no matter which row they belong to
    for lstOrder in lstSbOrder:
        for order in lstOrder:
            strSbLocation += str(order) + " " # take all of the index out thier lists
    sbCol = len(set(strSbLocation[0: -1].split(" "))) # the cols contain the strawberry
    eattenCol = c - sbCol # the cols eatable

    print(eattenRow * c + eattenCol * (r - eattenRow)) # the cell of cake eatable
