#script(python)
import heapq
import sys
sys.path.append('/home/jmanuel/workspace/TFG/TFG/src')
from main.model.datastructures.priorityqueue import PriorityQueue
from main.model.datastructures.fifoqueue import FifoQueue
from main.model.search.searchnode import SearchNode

s0 = (9,1,3,4,2,5,7,8,6)
s1 = (1,9,3,4,2,5,7,8,6)
s2 = (1,2,3,4,9,5,7,8,6)
s3 = (1,2,3,4,5,9,7,8,6)
s4 = (1,2,3,4,5,6,7,8,9)

fringe = FifoQueue()

def goal_test(state):
    return state == s4
    
def expand(node):
    if node.state == s0: return [SearchNode(s1, None, [], 0, 0)]
    if node.state == s1: return [SearchNode(s2, None, [], 0, 0)]
    if node.state == s2: return [SearchNode(s3, None, [], 0, 0)]
    if node.state == s3: return [SearchNode(s4, None, [], 0, 0)]
    if node.state == s4: return [SearchNode([], None, [], 0, 0)]

def graph_search_test():
    """ We create a set to stock visited nodes """
    closed = set()
    root_node = SearchNode(s0, None, [], 0, 0)
    fringe.push(root_node)
    while 1:
        """ Empty fringe means there are no solution """
        if fringe.is_empty(): return 0
        """ Recover fringe's frist node """
        node = fringe.pop()
        print('Next expanded node: ') ,
        print(node.state)
        """ We check if the recovered node is a posible solution """
        if goal_test(node.state):
            print('Solution found: ')
            print(node.state)
            return 1
        """ If it is not a solution, then we have to store it in closed """
        if node.state not in closed:
            closed.add(node.state)
            for child in expand(node):
                fringe.push(child)
    
#end.

if __name__ == '__main__':
    graph_search_test()
    