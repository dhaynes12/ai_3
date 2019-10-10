import board

class Node(object):
    
    def __init__(self, state, depth, depthLim, alpha, beta):
        self.state = state          # board state of the node
        self.depth = depth          # current depth of node
        self.depthLim = depthLim    # depth of how far the tree can evaluate
        self.alpha = alpha          # alpha and beta are values for pruning the tree
        self.beta = beta            
        self.nextMoves = []         # list of next possible moves
        self.weight = 0             # How good of a move is current node

        # if depth is at limit call weight function
        if depth == depthLim:
            pass
        else:       # else generate list of next possible moves
            genNextMoves()


    def genNextMoves(self):
        nextStates = []
        for i in range(0,6):
            if self.state.spaces[i] == 0:
                continue
            else:
                # need to add optional state pass to board
                tempState = board.getStartBoard()
                self.nextMoves.append(Node())

    # Generate how good a move is if node is a leaf node
    def setWeight(self):
        pass




