# AUTHOR: Juan Manuel Rey Escobar

from .searchNode import SearchNode


class Search:
    def __init__(self, initialState):
        self.options = options()
        self.statistics = statistics()
        self.initalState = initialState

    """ Method for creating the fringe """
    def newFringe(root):
        fringe = BinaryHeap()
        fringe.insert(root)
        return fringe

    """ Returns TRUE if fringe is empty """
    def fringeIsEmpty(fringe):
        return (fringe.currentSize == 0)

    """ POP method """
    def fringePOP(fringe):
        return fringe.delMin()

    """ Node insertion in fringe => fringe.insert(item) """
 

    """ Node insertion in successors """

    
    """ Expands a node """
    def inPath(node, state):
        while (node != None):
            if(

    """ Prints the solution """

    
    """ Search algorithms """
    def graphSearch():
        closed = {}
        rootNode = searchNode(initialState, None, None, 0, 0)
        fringe = self.newFringe(root)
        
        while 1:
        if (fringeIsEmpty(fringe)): return 0
        node = self.fringePOP(fringe)

        if(goalTest(node.state)):
            printSolution(node)
            return 1

        


