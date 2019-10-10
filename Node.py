import board.py

class Node(object):
    
    def __init__(self, state, depth, depthLim):
        self.state = state          # board state of the node
        self.depth = depth          # current depth of node
        self.depthLim = depthLim    # depth of how far the tree can evaluate
        self.alpha = 0              # alpha and beta are values for pruning the tree
        self.beta = 0            
        self.nextMoves = []         # list of next possible moves
        self.weight = 0             # How good of a move is current node

        # if depth is at limit call weight function
        if depth == depthLim:
            setWeight()
        else:       # else generate list of next possible moves
            genNextMoves()


    def genNextMoves(self):
        if self.depth % 2 == 0:
            for i in range(7,13):
                if self.state.spaces[i] == 0:
                    continue
                else:
                    # need to add optional state pass to board
                    tempState = self.state[:]
                    move(tempState, 1, i)
                    tempNode = Node(tempState, self.depth+1, self.depthLim)
                    self.nextMoves.append(tempNode)
        else:
            for i in range(0,6):
                if self.state.spaces[i] == 0:
                    continue
                else:
                    # need to add optional state pass to board
                    tempState = self.state[:]
                    move(tempState, 0, i)
                    tempNode = Node(tempState, self.depth+1, self.depthLim)
                    self.nextMoves.append(tempNode)

    # Generate how good a move is if node is a leaf node
    def setWeight(self):
        self.weight = goalPitVal(self.state)

def ABPruning (node, alpha, beta):
    node.alpha = alpha
    node.beta = beta
    if not node.nextMoves:
        return node.weight
    elif node.depth % 2 == 1:
        for i in node.nextMoves:
            tempVal = ABPruning(i, node.alpha, node.beta)
            if tempVal < node.beta:
                node.beta = tempVal
            if node.beta <= node.alpha:
                break
        return node.beta
    else:
        for i in node.nextMoves:
            tempVal = ABPruning(i, node.alpha, node.beta)
            if tempVal > node.alpha:
                node.alpha = tempVal
            if node.beta <= node.alpha:
                break
        return node.alpha

def goalPitVal(spaces):
    return state[13] - state[6]

def sideVal(spaces):
    return board.getSideValue(spaces, Board.NORTH) - board.getSideValue(spaces, Board.SOUTH)

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
