# AUTHOR: Juan Manuel Rey Escobar

import clingo
import time
from searchnode import SearchNode
from memory_profiler import memory_usage
from TFG.src.main.model.util.searchutils import expand
from TFG.src.main.model.util.atomutils import decorate_action
from TFG.src.main.model.util.atomutils import print_solution

           
class GraphSearch:
    def __init__(self):
        self.domain = None

    def add_domain(self,domain):
        self.domain = domain
        
    """ Searches for a plan """   

    def search(self, initial, fringe, actions, fluents, use_heuristic, bfs):
        """ Fringe: data structure for storing search nodes """
        fringe = fringe
        """ Maximum number of nodes in the fringe """
        max_size = 0
        """ Number of explored nodes """
        explored = 0
        """ Set of visited nodes """
        closed = set()
        """ Node which stores the initial state """
        root_node = SearchNode(initial, None, [], 0, 0, 0)
        fringe.push(root_node)
        """ The goal predicate """
        goal = clingo.Function("goal", [0])
        """ The instant which marks the start of the execution """
        start = time.time()
        while 1:
            if max_size < fringe.size():
                max_size = fringe.size()
            """ Empty fringe means there are no solution """
            if fringe.is_empty():
                """ The instant which marks the end of the execution """ 
                end = time.time()
                """ The amount of memory usage in MB """
                memory = memory_usage()
                print('UNSATISFIABLE')
                print('Execution time: ') ,
                print(end - start) ,
                print('s')
                print('Memory usage: ') ,
                print(memory[0]) ,
                print('MB')
                print('Explored states: ') ,
                print(explored) 
                print('Maximum number of nodes stored: ') ,
                print(max_size) 
                return 0
            
            """ Recover fringe's frist node """
            node = fringe.pop()
            """ We check if the recovered node is a posible solution """
            if (clingo.Function(str(goal))) in frozenset(node.state):
                """ The instant which marks the end of the execution """
                end = time.time()
                """ The amount of memory usage in MB """
                memory = memory_usage()
                print('SATISFIABLE')
                print('Solution found: ')
                for element in node.state:
                    if element != (clingo.Function(str(goal))):
                        print(clingo.Function(decorate_action(str(element)))) ,
                print('')
                print('Execution time: ') ,
                print(end - start) ,
                print('s')
                print('Memory usage: ') ,
                print(memory[0]) ,
                print('MB')
                print('Explored states: ') ,
                print(explored)
                print('Maximum number of nodes stored: ') ,
                print(max_size) 
                print('Obtained plan: ') ,
                print_solution(node)
                return 1
            """ If it is not a solution, then we have to store it in closed """
            if frozenset(node.state) not in closed:
                closed.add(frozenset(node.state))
                explored = explored + 1
                for child in expand(self.domain, node, actions, fluents, use_heuristic, bfs):
                    fringe.push(child)

