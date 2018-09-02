# AUTHOR: Juan Manuel Rey Escobar


class SearchNode:

    def __init__(self, state, parent, action, pathCost, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self. pathCost = pathCost
        self.depth = depth
