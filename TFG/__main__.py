#!/usr/bin/env python
#AUTHOR: Juan Manuel Rey Escobar

import sys
import TFG.src.main.model.solve.solver as solver
from TFG.src.main.model.datastructures.fifoqueue import FifoQueue
from TFG.src.main.model.datastructures.lifoqueue import LifoQueue
from TFG.src.main.model.datastructures.priorityqueue import PriorityQueue
from TFG.src.main.model.search.graphsearch import GraphSearch
from TFG.src.main.model.search.completegraphsearch import CompleteGraphSearch
from TFG.src.main.model.util.mainutils import print_help
from TFG.src.main.model.util.mainutils import print_version
from TFG.src.main.model.util.mainutils import print_error
from asynchat import fifo
from binstar_client.commands.search import search


def main():
    search_algorithm = GraphSearch()
    fringe = FifoQueue()
    bfs = "astar"
    use_heuristic = False
    
    if len(sys.argv) == 2:
        param1 = sys.argv[1]
        if param1 == "--version":
            print_version()
            return
        elif param1 == "-help":
            print_help()
            return
                
    if len(sys.argv) == 3:
        param1 = sys.argv[1]
        param2 = sys.argv[2]
        if param2 == "-h":
            use_heuristic = True
        elif param2 == "-all":
            search_algorithm = CompleteGraphSearch()
        elif param2 == "breadth":
            fringe = FifoQueue()
        elif param2 == "depth":
            fringe = LifoQueue()
        elif param2 == "greedy":
            fringe = PriorityQueue()
            bfs = 'greedy'
        elif param2 == "astar":
            fringe = PriorityQueue()
        else:
            print_error()
            print_help()
            return
            
    elif len(sys.argv) == 4:
        param1 = sys.argv[1]
        param2 = sys.argv[2]
        param3 = sys.argv[3]
        
        if param2 == "-h":
            use_heuristic = True
        elif param2 == "-all":
            search_algorithm = CompleteGraphSearch()   
        else:
            print_error()
            print_help()
            return
        
        if param3 == "breadth":
            fringe = FifoQueue()
        elif param3 == "depth":
            fringe = LifoQueue()
        elif param3 == "greedy":
            fringe = PriorityQueue()
            bfs = 'greedy'
        elif param3 == "astar":
            fringe = PriorityQueue()
        else:
            print_error()
            print_help()
            return 
        
    plan = solver.Solver(param1,search_algorithm,fringe,use_heuristic,bfs)
    try:
        plan.solve()
    except RuntimeError:
        print_error()
        print_help()
        return 
            
        

            
        


if __name__ == "__main__":
    main()