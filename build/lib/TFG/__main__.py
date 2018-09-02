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
from TFG.src.main.model.util.mainutils import fringe
from TFG.src.main.model.util.mainutils import search_algorithm


def main():
    
    if len(sys.argv) == 2:
        params = sys.argv[1]
        if params == "--version":
            print_version()
        elif params == "-help":
            print_help()
        else:
            plan = solver.Solver(params,search_algorithm,fringe)
            plan.solve()
        
    else:
        options = sys.argv[1]
        file_name = sys.argv[2]
        if options == "-all":
            plan = solver.Solver(file_name,CompleteGraphSearch(),fringe)
            plan.solve()
        elif options == "-d":
            plan = solver.Solver(file_name,search_algorithm,LifoQueue())
            plan.solve()
        elif options == "-b":
            plan = solver.Solver(file_name,search_algorithm,FifoQueue())
            plan.solve()
        elif options == "-h":
            plan = solver.Solver(file_name,search_algorithm,PriorityQueue())
            plan.solve()
            
        


if __name__ == "__main__":
    main()