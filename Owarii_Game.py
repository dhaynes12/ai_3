

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
                self.spaces.append(10)
    
    def move(self, player, pos):
        # Move Checking
        if (player == SOUTH and (pos > 6 or pos < 0)):
            return False, INVALID_MOVE_SOUTH
        elif (player == NORTH and (pos < 7 or pos > 12)):
            return False, INVALID_MOVE_NORTH
        elif (spaces[pit] == 0):
            return False, INVALID_MOVE_EMPTY
            
        # Making the Move
        stones = spaces[pos]
        spaces[pos] = 0
        drops = 0
        nextPos = pos
        while(drops <= spaces):
            if (player == SOUTH and pos != 13) or (player == NORTH and pos != 6):
                spaces[nextPos] += 1
                drops += 1
            
            nextPos += 1
            if nextPos > 13:
                nextPos = 0
        
        return True, ""
    
    def checkEndState():
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
    board = Board()
    print(board.spaces)
    board.move(0, 4)
    print(board.spaces)
    success, mess = board.move(1, 4)
    print(mess)
    print(board.spaces)
    print("Hello World")
    
    #brd = Board()
    #brd.printBoard();
    #print(GetWhoMovesFirst())

if __name__ == '__main__':
    main()
