

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
        if (player == SOUTH and (pos > 6 or pos < 0)):
            return False, INVALID_MOVE_SOUTH
        elif (player == NORTH and (pos < 7 or pos > 12)):
            return False, INVALID_MOVE_NORTH
        elif (self.spaces[pit] == 0):
            return False, INVALID_MOVE_EMPTY
            
        # Making the Move
        stones = self.spaces[pos]
        self.spaces[pos] = 0
        for i in range(1, stones+1):
            spaces[pos+i] += 1
        
        return True, ""

    def printBoard(self):
        print("       **NORTH**")
        print(" %3s %2s %2s %2s %2s %2s" % (self.spaces[12], self.spaces[11], self.spaces[10], self.spaces[9], self.spaces[8], self.spaces[7]))
        print("%2s %15s %3s" % (self.spaces[13], "", self.spaces[6]))
        print(" %3s %2s %2s %2s %2s %2s" % (self.spaces[0], self.spaces[1], self.spaces[2], self.spaces[3], self.spaces[4], self.spaces[5]))
        print("       **SOUTH**")


def main():
    brd = Board()
    brd.printBoard();
    #print(GetWhoMovesFirst())

if __name__ == '__main__':
    main()
