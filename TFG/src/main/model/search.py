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

    """ POP method """
    def fringePOP(fringe):
        return fringe.delMin()

    """ Node insertion in fringe => fringe.insert(item) """
 

    """ Node insertion in successors """

    
    """ Expands a node """
    

    """ Prints the solution """

    
    """ Search algorithm """
    def graphSearch():
        closed = {}
        rootNode = searchNode(initialState, None, None, 0, 0)
        fringe = self.newFringe(root)
        
        while 1:
        if (fringe.isEmpty): return 0
        node = self.fringePOP(fringe)

        if(goalTest(node.state)):
            printSolution(node)
            return 1
        if(node.state) not in closed:
            closed[key] = node.state
            fringe.insert(expand(node))
        


