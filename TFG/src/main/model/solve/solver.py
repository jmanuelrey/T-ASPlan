#AUTHOR: Juan Manuel Rey Escobar

import clingo
from TFG.src.main.model.datastructures.priorityqueue import PriorityQueue
from TFG.src.main.model.datastructures.fifoqueue import FifoQueue
import TFG.src.main.model.util.atomutils 


class Solver():
    def __init__(self, file_name, search_algorithm, fringe, heuristic, bfs, states):
        self.file_name = file_name
        self.fringe = fringe
        self.search_algorithm = search_algorithm
        self.heuristic = heuristic
        self.bfs = bfs
        self.states = states
    
    def solve(self):
        """ Creating the program object """
        program_types = clingo.Control([])
        program_dynamic = clingo.Control([])
        
        """ We want to obtain ALL possible stable models """
        program_types.configuration.solve.models = 0
        program_dynamic.configuration.solve.models = 0
        
        """ We initialize data structures """
        action_list = []
        fluent_list = []
        initial_states = []
        
        """ Reading from the input file """
        try:
            program_types.load(self.file_name)
        except RuntimeError:
            return 
        
        try:
            program_dynamic.load(self.file_name)
        except RuntimeError:
            raise RuntimeError 
        
        """ We obtain fluents, actions and the initial state """
        try:
            program_types.ground([('initial', []), ('types', [0]), ('static', [])])  
        except RuntimeError:
            raise RuntimeError
        
        models = program_types.solve(yield_ = True)
        for element in models:
            initial_state = []
            for atom in element.symbols(atoms = True):
                if 'action' in str(atom):
                    action_list.append(clingo.Function(TFG.src.main.model.util.atomutils .obtain_dynamic(str(atom))))
                elif 'fluent' in str(atom):
                    fluent_list.append(clingo.Function(TFG.src.main.model.util.atomutils .obtain_dynamic(str(atom))))
                elif ((clingo.Function(str(atom))) in fluent_list) or ((clingo.Function(str(atom))) in action_list):
                    initial_state.append(clingo.Function(str(atom)))
            initial_states.append(initial_state)
            
        if len(initial_states) > 1:
            print('Warning: several answer sets obtained as initial state')
            
        """ We add as external atoms all the possible fluents and actions """
        for atom in fluent_list:
            program_dynamic.add('fluents',[],"#external" + " " + str(atom) + ".") 
            
        for atom in action_list:
            program_dynamic.add('actions',[],"#external" + " " + str(atom) + ".") 
        
        try:   
            program_dynamic.ground([('fluents', []), ('actions', []), ('dynamic', [1]), ('static', []), ('final',[1])])
        
        except RuntimeError:
            raise RuntimeError
        
        """ Delegates to its search algorithm """
        self.search_algorithm.add_domain(program_dynamic)
        self.search_algorithm.search(initial_states[0],self.fringe,action_list,fluent_list, self.heuristic, self.bfs, self.states)

