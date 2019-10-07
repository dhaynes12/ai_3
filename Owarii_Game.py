

def GetWhoMovesFirst():
    while True:
        first = input("Who gets to move first ('s' or 'south' for south; 'n' or 'north' for north): ")
        first = first.lower()
        if first == 's' or first == 'south':
            return 0
        elif first == 'n' or first == 'north':
            return 1
        else:
            print("Improper input. Please try again.")


class Board:
    SOUTH = 0
    NORTH = 1
    INVALID_MOVE_SOUTH = "South can only make moves on spaces 0-5"
    INVALID_MOVE_NORTH = "North can only make moves on spaces 7-12"
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
    
    def move(self, player, pos):
        # Move Checking
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
        nextPos = pos
        while(drops <= stones):
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
        print(" **NORTH**")
        print(" ",self.spaces[12], self.spaces[11], self.spaces[10], self.spaces[9], self.spaces[8], self.spaces[7])
        print(self.spaces[13], "           ", self.spaces[6])
        print(" ",self.spaces[0], self.spaces[1], self.spaces[2], self.spaces[3], self.spaces[4], self.spaces[5])
        print(" **SOUTH**")


def main():
    brd = Board()
    brd.printBoard()
    #print(GetWhoMovesFirst())

if __name__ == '__main__':
    main()
