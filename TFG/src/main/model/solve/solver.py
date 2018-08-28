#script(Python)
#AUTHOR: Juan Manuel Rey Escobar

import clingo
from src.main.model.search.search import Search
from src.main.model.datastructures.fifoqueue import FifoQueue

def obtain_dynamic(atom):
    start = atom.find('(')
    end = atom.find(')')    
    return atom[start+1:end+1]

def main():
    """ Creating the program object """
    program_types = clingo.Control([])
    program_dynamic = clingo.Control([])
    program_goal = clingo.Control([])
    
    """ We want to obtain ALL possible stable models """
    program_types.configuration.solve.models = 0
    program_dynamic.configuration.solve.models = 0
    program_goal.configuration.solve.models = 0
    
    """ We initialize data structures """
    action_list = []
    fluent_list = []
    initial_state = []
    fringe = FifoQueue()
    goal = []
    
    """ Reading from the input file """
    file_name = '/home/jmanuel/workspace/TFG/TFG/src/asp/wolf.lp'
    program_types.load(file_name)
    program_dynamic.load(file_name)
    program_goal.load(file_name)
    
    """ We obtain the set of atoms that configure the final state """
    program_goal.ground([('final', [0])])
    models = program_goal.solve(yield_ = True)
    for element in models:
        for atom in element.symbols(atoms = True):
            goal.append(clingo.Function(str(atom)))
    
    """ We obtain fluents, actions and the initial state """
    program_types.ground([('initial', []), ('types', [0]), ('static', [])])   
    models = program_types.solve(yield_ = True)
    for element in models:
        for atom in element.symbols(atoms = True):
            if 'action' in str(atom):
                action_list.append(clingo.Function(obtain_dynamic(str(atom))))
            elif 'fluent' in str(atom):
                fluent_list.append(clingo.Function(obtain_dynamic(str(atom))))
            elif ((clingo.Function(str(atom))) in fluent_list) or ((clingo.Function(str(atom))) in action_list):
                initial_state.append(clingo.Function(str(atom)))
    
    """ We add as external atoms all the possible fluents and actions """
    for atom in fluent_list:
        program_dynamic.add('fluents',[],"#external" + " " + str(atom) + ".") 
        
    for atom in action_list:
        program_dynamic.add('actions',[],"#external" + " " + str(atom) + ".") 
        
    program_dynamic.ground([('fluents', []), ('actions', []), ('dynamic', [0]), ('static', [])])
    
    search = Search(program_dynamic)
    search.graph_search(initial_state, fringe, goal, action_list, fluent_list)
#end.

main()
