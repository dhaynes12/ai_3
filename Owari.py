

def getWhoMovesFirst():
    while True:
        first = input("Who gets to move first ('s' or 'south' for south; 'n' or 'north' for north): ")
        first = first.lower()
        if first == 's' or first == 'south':
            return 0
        elif first == 'n' or first == 'north':
            return 1
        else:
            print("Improper input. Please try again.")
            
            
def playerMove(player, brd):
    success = False
    spaces = ""
    
    if (player == Board.SOUTH):
        spaces = Board.SOUTH_SPACES
    else:
        spaces = Board.NORTH_SPACES
    
    while not success:
        select = input("Make your move (" + spaces + "): ")
        success, errorMessage = brd.move(player, select)
        
        if not success:
            print(errorMessage)


class Board(object):
    SOUTH = 0
    NORTH = 1
    SOUTH_SPACES = "0-5"
    NORTH_SPACES = "7-12"
    INVALID_MOVE_NOT_INT = "Move input is invalid. Please enter a number."
    INVALID_MOVE_SOUTH = "South can only make moves on spaces " + SOUTH_SPACES
    INVALID_MOVE_NORTH = "North can only make moves on spaces " + NORTH_SPACES
    INVALID_MOVE_EMPTY = "Select a non-empty pit"
    
    def __init__(self):
        self.spaces = []   #The game space. 
                        #   Spaces 0-6 are SOUTH's pits, w/ 6 being SOUTH's goal pit. 
                        #   Spaces 7-13 are NORTH's pits, w/ 13 being NORTH's goal pit.
        self.end = False
        
        for i in range(0, 14):
            if i != 6 and i != 13:
                self.spaces.append(3)
            else:
                self.spaces.append(0)
    
    def move(self, player, posStr):
        # Move Checking
        if (not posStr.isdigit()):
            if (player == Board.SOUTH):
                return False, Board.INVALID_MOVE_NOT_INT + " " + Board.INVALID_MOVE_SOUTH
            else:
                return False, Board.INVALID_MOVE_NOT_INT + " " + Board.INVALID_MOVE_NORTH
        
        pos = int(posStr)
        if (player == Board.SOUTH and (pos > 6 or pos < 0)):
            return False, Board.INVALID_MOVE_SOUTH
        elif (player == Board.NORTH and (pos < 7 or pos > 12)):
            return False, Board.INVALID_MOVE_NORTH
        elif (self.spaces[pos] == 0):
            return False, Board.INVALID_MOVE_EMPTY
            
        # Making the Move
        stones = self.spaces[pos]
        self.spaces[pos] = 0
        drops = 0
        nextPos = pos+1
        while(drops < stones):
            if (player == Board.SOUTH and pos != 13) or (player == Board.NORTH and pos != 6):
                self.spaces[nextPos] += 1
                drops += 1
            
            nextPos += 1
            if nextPos > 13:
                nextPos = 0
        
        return True, ""
    
    def checkEndState(self):
        isEnd = True
        
        #Check South side
        for i in range(0, 6):
            if self.spaces[i] is not 0:
                isEnd = False
                break
        
        #Check North side
        if not isEnd:
            isEnd = True
            for i in range(7, 13):
                if self.spaces[i] is not 0:
                    isEnd = False
                    break
        
        if not isEnd:
            return False
        
        # -- End-Game Distribution --
        #South-Side
        for i in range(0, 6):
            if self.spaces[i] is not 0:
                self.spaces[6] += self.spaces[i]
                self.spaces[i] = 0
        
        #North-Side
        for i in range(7, 13):
            if self.spaces[i] is not 0:
                self.spaces[13] += self.spaces[i]
                self.spaces[i] = 0
        
        return True

    def printBoard(self):
        print("       **NORTH**")
        print(" %3s %2s %2s %2s %2s %2s" % (self.spaces[12], self.spaces[11], self.spaces[10], self.spaces[9], self.spaces[8], self.spaces[7]))
        print("%2s %15s %3s" % (self.spaces[13], "", self.spaces[6]))
        print(" %3s %2s %2s %2s %2s %2s" % (self.spaces[0], self.spaces[1], self.spaces[2], self.spaces[3], self.spaces[4], self.spaces[5]))
        print("       **SOUTH**")
    
    def getScore(self, player):
        if (player == Board.SOUTH):
            return self.spaces[6]
        elif (player == Board.NORTH):
            return self.spaces[13]
        
        return None
    
    def getSideValue(self, player):
        if (player == Board.SOUTH):
            return self.spaces[0:6].copy()
        elif (player == Board.NORTH):
            return self.spaces[7:13].copy()
        
        return None


def main():
    brd = Board()
    turn = getWhoMovesFirst()
    gameEnd = False
    
    while not gameEnd:
        brd.printBoard()
        
        if turn == Board.SOUTH:
            print("South's turn")
            playerMove(turn, brd)
            turn = Board.NORTH
        elif turn == Board.NORTH:
            print("North's turn")
            playerMove(turn, brd)
            turn = Board.SOUTH
        else:
            print("Error: Turn set to invalid player.")
            break
        
        gameEnd = brd.checkEndState()
        if gameEnd:
            brd.printBoard()
            input("Game has ended. Hit enter to see results")
            print("----- RESULTS -----")
            print("South Points:", brd.getScore(Board.SOUTH))
            print("North Points:", brd.getScore(Board.NORTH))
            
            if brd.getScore(Board.SOUTH) > brd.getScore(Board.NORTH):
                print("South wins!")
            elif brd.getScore(Board.SOUTH) < brd.getScore(Board.NORTH):
                print("North wins!")
            else:
                print("It's a tie.")

if __name__ == '__main__':
    main()
