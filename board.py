SOUTH = 0
NORTH = 1
SOUTH_SPACES = "0-5"
NORTH_SPACES = "7-12"
INVALID_MOVE_NOT_INT = "Move input is invalid. Please enter a number."
INVALID_MOVE_SOUTH = "South can only make moves on spaces " + SOUTH_SPACES
INVALID_MOVE_NORTH = "North can only make moves on spaces " + NORTH_SPACES
INVALID_MOVE_EMPTY = "Select a non-empty pit"

def getStartBoard():
    spaces = []
    
    for i in range(0, 14):
        if i != 6 and i != 13:
            spaces.append(3)
        else:
            spaces.append(0)
    
    return spaces

def move(spaces, player, posStr):
    # -- Move Checking --
    if (not posStr.isdigit()):
        if (player == SOUTH):
            return False, INVALID_MOVE_NOT_INT + " " + INVALID_MOVE_SOUTH
        else:
            return False, INVALID_MOVE_NOT_INT + " " + INVALID_MOVE_NORTH
    
    pos = int(posStr)
    if (player == SOUTH and (pos > 5 or pos < 0)):
        return False, INVALID_MOVE_SOUTH
    elif (player == NORTH and (pos < 7 or pos > 12)):
        return False, INVALID_MOVE_NORTH
    elif (spaces[pos] == 0):
        return False, INVALID_MOVE_EMPTY
        
    # -- Beginning the Move --
    stones = spaces[pos]
    spaces[pos] = 0
    drops = 0
    nextPos = pos+1
    
    # -- Standard Movement --
    while(drops < stones):
        if (player == SOUTH and nextPos != 13) or (player == NORTH and nextPos != 6):
            spaces[nextPos] += 1
            drops += 1
        
        nextPos += 1
        if nextPos > 13:
            nextPos = 0
    
    # -- Capturing --
    # If the last stone lands in an empty pit on the moving player's 
    # side, then any stones in the opposite pit are moved to their goal 
    # pit. For checking if the last pit was empty, we check if the
    # last space has 1 stone in it, since that means that before the
    # movement it had 0 stones in it.
    finalPos = nextPos - 1
    if (player == SOUTH and finalPos <= 5 and finalPos >= 0 and spaces[finalPos] == 1):
        oppositePos = 12 - finalPos
        spaces[6] += spaces[oppositePos]
        spaces[oppositePos] = 0
    elif (player == NORTH and finalPos <= 12 and finalPos >= 7 and spaces[finalPos] == 1):
        oppositePos = 12 - finalPos
        spaces[13] += spaces[oppositePos]
        spaces[oppositePos] = 0
    
    return True, ""

def checkEndState(spaces):
    isEnd = True
    
    #Check South side
    for i in range(0, 6):
        if spaces[i] is not 0:
            isEnd = False
            break
    
    #Check North side
    if not isEnd:
        isEnd = True
        for i in range(7, 13):
            if spaces[i] is not 0:
                isEnd = False
                break
    
    if not isEnd:
        return False
    
    # -- End-Game Distribution --
    #South-Side
    for i in range(0, 6):
        if spaces[i] is not 0:
            spaces[6] += spaces[i]
            spaces[i] = 0
    
    #North-Side
    for i in range(7, 13):
        if spaces[i] is not 0:
            spaces[13] += spaces[i]
            spaces[i] = 0
    
    return True

def printBoard(spaces):
    print("       **NORTH**")
    print(" %3s %2s %2s %2s %2s %2s" % (spaces[12], spaces[11], spaces[10], spaces[9], spaces[8], spaces[7]))
    print("%2s %15s %3s" % (spaces[13], "", spaces[6]))
    print(" %3s %2s %2s %2s %2s %2s" % (spaces[0], spaces[1], spaces[2], spaces[3], spaces[4], spaces[5]))
    print("       **SOUTH**")

def getScore(spaces, player):
    if (player == SOUTH):
        return spaces[6]
    elif (player == NORTH):
        return spaces[13]
    
    return None

def getSideValue(spaces, player):
    if (player == SOUTH):
        return sum(spaces[0:6])
    elif (player == NORTH):
        return sum(spaces[7:13])
    
    return None
