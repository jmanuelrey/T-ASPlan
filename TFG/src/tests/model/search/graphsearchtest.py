#script(python)

import time
from src.main.model.datastructures import priorityqueue
from src.main.model.datastructures import fifoqueue
from src.main.model.datastructures import lifoqueue
from src.main.model.search.searchnode import SearchNode
from memory_profiler import memory_usage

s0 = (1,8,2,9,4,3,7,6,5)
sf = (1,2,3,4,5,6,7,8,9)
N = 3
fringe = fifoqueue.FifoQueue()

def goal_test(state):
    return state == sf

def swap(state,pos1,pos2):
    mutable = list(state)
    temp = mutable[pos2]
    mutable[pos2] = mutable[pos1]
    mutable[pos1] = temp
    return tuple(mutable)
    
def print_solution(node): 
    if node.parent == None:
        return
    else:
        print_solution(node.parent)
        print(node.action) ,
         
def expand(node):
    expanded = []
    i = node.state.index(9)
    if i >= N:
        new_node = SearchNode(swap(node.state,i,i-N), node, ["up"], node.pathCost + 1, node.depth + 1)   
        expanded.append(new_node)
    if i < N*(N-1):
        new_node = SearchNode(swap(node.state,i,i+N), node, ["down"], node.pathCost + 1, node.depth + 1)   
        expanded.append(new_node)
    if (i % N) > 0:
        new_node = SearchNode(swap(node.state,i,i-1), node, ["left"], node.pathCost + 1, node.depth + 1)   
        expanded.append(new_node)
         
    if (i % N) < (N-1):
        new_node = SearchNode(swap(node.state,i,i+1), node, ["right"], node.pathCost + 1, node.depth + 1)   
        expanded.append(new_node)
         
    return expanded
        

def graph_search_test():
    """ We create a set to stock visited nodes """
    max_size = 0
    explored = 0
    closed = set()
    root_node = SearchNode(s0, None, [], 0, 0)
    fringe.push(root_node)
    max_size+= 1
    start = time.time()
    while 1:
        """ Empty fringe means there are no solution """
        if fringe.is_empty(): 
            end = time.time()
            memory = memory_usage()
            print('UNSATISFIABLE')
            print('Execution time: ') ,
            print(end - start) ,
            print('ms')
            print('Memory usage: ') ,
            print(memory[0]) ,
            print('MB')
            print('Explored states: ') ,
            print(explored) 
            print('Maximum number of states stored: ') ,
            print(max_size) 
            return 0
        """ Recover fringe's frist node """
        node = fringe.pop()
        """ We check if the recovered node is a posible solution """
        if goal_test(node.state):
            end = time.time()
            memory = memory_usage()
            print('SATISFIABLE')
            print('Solution found: ')
            print(node.state)
            print('Execution time: ') ,
            print(end - start) ,
            print('ms')
            print('Memory usage: ') ,
            print(memory[0]) ,
            print('MB')
            print('Explored states: ') ,
            print(explored)
            print('Maximum number of states stored: ') ,
            print(max_size) 
            print('Obtained plan: ') ,
            print_solution(node)
            return 1
        """ If it is not a solution, then we have to store it in closed """
        if node.state not in closed:
            closed.add(node.state)
            explored = explored + 1
            for child in expand(node):
                fringe.push(child)
                max_size+= 1
    
#end.

if __name__ == '__main__':
    graph_search_test()
    
    