# AUTHOR: Juan Manuel Rey Escobar

from TFG.src.main.model.datastructures.fifoqueue import FifoQueue
from TFG.src.main.model.search.graphsearch import GraphSearch

""" Current version """
version = "1.0.0"

""" default parameters """
fringe = FifoQueue()
search_algorithm = GraphSearch()


def print_help():
    print('  usage: [options] [file]')
    print('  Available options:')
    print('  -all: Searches for all possible plans.')
    print('  -d: Depth search.')
    print('  -b: Breadth search.')
    print('  -h: Indicates the tool to use an heuristic given within the specification.')
    print('  -help: Shows help menu')
    print('  --version: Current installed version')

    
def print_version():
    print(version)
    
