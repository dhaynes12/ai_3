import board

class Node(object):
    
    def __init__(self, state, depth, depthLim, cupMove = -1):
        self.state = state          # board state of the node
        self.depth = depth          # current depth of node
        self.depthLim = depthLim    # depth of how far the tree can evaluate
        self.alpha = 0              # alpha and beta are values for pruning the tree
        self.beta = 0            
        self.nextMoves = []         # list of next possible moves
        self.weight = 0             # How good of a move is current node
        self.cupMove = cupMove

        # if depth is at limit call weight function
        if depth == depthLim:
            self.setWeight()
        else:       # else generate list of next possible moves
            self.genNextMoves()


    def genNextMoves(self):
        if self.depth % 2 == 0:
            for i in range(7,13):
                if self.state[i] == 0:
                    continue
                else:
                    # need to add optional state pass to board
                    tempState = self.state[:]
                    board.move(tempState, 1, str(i))
                    tempNode = Node(tempState, self.depth+1, self.depthLim, i)
                    self.nextMoves.append(tempNode)
        else:
            for i in range(0,6):
                if self.state[i] == 0:
                    continue
                else:
                    # need to add optional state pass to board
                    tempState = self.state[:]
                    board.move(tempState, 0, str(i))
                    tempNode = Node(tempState, self.depth+1, self.depthLim, i)
                    self.nextMoves.append(tempNode)

    # Generate how good a move is if node is a leaf node
    def setWeight(self):
        self.weight = goalPitVal(self.state)

def ABPruning (node, alpha, beta):
    node.alpha = alpha
    node.beta = beta
    nextMove = None
    if node.depth == node.depthLim:
        return node.weight, nextMove
    elif node.depth % 2 == 1:
        for i in node.nextMoves:
            tempVal, jnkState = ABPruning(i, node.alpha, node.beta)
            if tempVal < node.beta:
                node.beta = tempVal
                nextMove = i
            if node.beta <= node.alpha:
                break
        return node.beta, nextMove
    else:
        for i in node.nextMoves:
            tempVal, jnkState = ABPruning(i, node.alpha, node.beta)
            if tempVal > node.alpha:
                node.alpha = tempVal
                nextMove = i
            if node.beta <= node.alpha:
                break
        return node.alpha, nextMove

def goalPitVal(spaces):
    return spaces[13] - spaces[6]

def sideVal(spaces):
    return board.getSideValue(spaces, board.NORTH) - board.getSideValue(spaces, board.SOUTH)

#I'm not sure if having the AI know if it can steal stones from the 
#opponent and vice versa is useful, since it can already determine that
#from seeing the point value go up from a successful capture.
def captureVal(spaces, player):
    capturePoints = 0
    playerSpaces = None
    
    if (player == board.NORTH):
        playerSpaces = range(7, 13)
    elif (player == board.SOUTH):
        playerSpaces = range(0, 6)
    else:
        raise Exception("player param in captureVal not set to valid player id")
    
    for i in playerSpaces:
        if spaces[i] == 0 and spaces[12-i] > capturePoints:
            capturePoints = spaces[12-i]
    
    return capturePoints
