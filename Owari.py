import board
import Node

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

def getDepthLim():
    while True:
        depthLim = input("Set the look ahead value ( >0 ): ")
        try:
            temp = int(depthLim)
            if temp < 0:
                print("value was not above 0")
                continue
            else:
                return temp
        except Exception as err:
            print("Inputed value was not an int")

 
            
            
def playerMove(spaces, player):
    success = False
    available = ""
    
    if (player == board.SOUTH):
        available = board.SOUTH_SPACES
    else:
        available = board.NORTH_SPACES
    
    while not success:
        select = input("Make your move (" + available + "): ")
        success, errorMessage = board.move(spaces, player, select)
        
        if not success:
            print(errorMessage)

def main():
    spaces = board.getStartBoard()
    turn = getWhoMovesFirst()
    depthLim = getDepthLim()
    gameEnd = False
    
    while not gameEnd:
        board.printBoard(spaces)
        
        if turn == board.SOUTH:
            print("South's turn")
            playerMove(spaces, turn)
            turn = board.NORTH
        elif turn == board.NORTH:
            print("North's turn")
            tempNode = Node.Node(spaces[:], 0, depthLim)
            value, state = Node.ABPruning(tempNode, -1000000, 1000000)
            success, errorMessage = board.move(spaces, board.NORTH, str(state.cupMove))
            print("Moving Cup:", state.cupMove, "\nTranslated to Cup:", state.cupMove - 7)
            turn = board.SOUTH
        else:
            print("Error: Turn set to invalid player.")
            break
        
        gameEnd = board.checkEndState(spaces)
        if gameEnd:
            board.printBoard(spaces)
            input("Game has ended. Hit enter to see results")
            print("----- RESULTS -----")
            print("South Points:", board.getScore(spaces, board.SOUTH))
            print("North Points:", board.getScore(spaces, board.NORTH))
            
            if board.getScore(spaces, board.SOUTH) > board.getScore(spaces, board.NORTH):
                print("South wins!")
            elif board.getScore(spaces, board.SOUTH) < board.getScore(spaces, board.NORTH):
                print("North wins!")
            else:
                print("It's a tie.")

if __name__ == '__main__':
    main()
