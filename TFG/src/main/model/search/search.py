# AUTHOR: Juan Manuel Rey Escobar


import searchnode


class Search:
    def __init__(self, fringe, problem, init, goal, expand):
        self.fringe = fringe
    
    def graph_search(self, init):
        """ We create a hash table to stock visited nodes """
        closed = set()
        root_node = SearchNode(init, None, [], 0, 0)
        fringe.push(root_node)
        while 1:
            """ Empty fringe means there are no solution """
            if fringe.is_empty(): return 0
            """ Recover fringe's frist node """
            node = fringe.pop()
            """ We check if the recovered node is a posible solution """
            if goal_test(node.state):
                print('Solution found: ')
                print(node.state)
                print(node.action)
                return 1
            """ If it is not a solution, then we have to store it in closed """
            if node.state not in closed:
                closed.add(node.state)
                for child in expand(node):
                    fringe.push(child)
            
            
                

               
    
    
    
        

