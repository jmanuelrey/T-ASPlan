# AUTHOR: Juan Manuel Rey Escobar

from TFG.src.main.model.datastructures.fifoqueue import FifoQueue
from TFG.src.main.model.search.graphsearch import GraphSearch

""" Current version """
version = "1.0.0"

def print_help():
    print('  usage: [file] [options] [search]')
    print('  Available options:')
    print('  -all: Searches for all possible plans.')
    print('  -h: Search with heuristic. The program specification must include an heuristic.')
    print('  -help: Displays help menu')
    print('  --version: Current installed version')
    print('  Available search algorithms:')
    print('  breadth ')
    print('  depth ')
    print('  greedy ')
    print('  astar ')

    
def print_version():
    print(version)
    
def print_error():
    print('ERROR: solving was not possible.')
    
