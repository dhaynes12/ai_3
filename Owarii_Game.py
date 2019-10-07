

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
        else if (player == NORTH and (pos < 7 or pos > 12):
            return False, INVALID_MOVE_NORTH
        else if (spaces[pit] == 0):
            return False, INVALID_MOVE_EMPTY
            
        # Making the Move
        stones = spaces[pos]
        spaces[pos] = 0
        for i in range(1, stones+1):
            spaces[pos+i] += 1
        
        return True, ""

def main():
    print(GetWhoMovesFirst())

if __name__ == '__main__':
    main()
