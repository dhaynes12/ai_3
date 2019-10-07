import argparse

class Board:
    SOUTH = 0
    NORTH = 1
    INVALID_MOVE_SOUTH = "South can only make moves on spaces 0-5"
    INVALID_MOVE_NORTH = "North can only make moves on spaces 7-12"
    INVALID_MOVE_EMPTY = "Select a non-empty pit"
    
    def __init__(self):
        spaces = [14]   #The game space. 
                        #   Spaces 0-6 are SOUTH's pits, w/ 6 being SOUTH's goal pit. 
                        #   Spaces 7-13 are NORTH's pits, w/ 13 being NORTH's goal pit.
        end = False
        
        for i in range(0, len(spaces)):
            if i != 6 and i != 13:
                spaces[i] = 3
    
    def move(player, pos):
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

def main():
    board = Board()
    print(board.spaces)
    board.move(0, 4)
    print(board.spaces)
    success, mess = board.move(1, 4)
    print(mess)
    print(board.spaces)
    print("Hello World")

if __name__ == '__main__':
    main()
