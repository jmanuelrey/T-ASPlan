# AUTHOR: Juan Manuel Rey Escobar

import clingo
from TFG.src.main.model.util.atomutils import reset
from TFG.src.main.model.util.atomutils import obtain_name
from TFG.src.main.model.util.atomutils import obtain_params
from TFG.src.main.model.util.atomutils import obtain_t
from TFG.src.main.model.search.searchnode import SearchNode

""" Succesors is called by expand to obtain the next possible states """   


def succesors(domain, state, actions, fluents):
    succ_states = []
    old_ones = state[:]
    for atom in state:
        params = obtain_params(str(atom)) 
        name = obtain_name(str(atom)) 
        domain.assign_external(clingo.Function(name, params), True)
            
    models = domain.solve(yield_=True)
            
    for element in models:
        priority = 0
        atoms = []
        performed_actions = []
        for atom in element.symbols(atoms=True):
            if "heuristics" in str(atom):
                priority = obtain_t(str(atom))
            t = obtain_t(str(atom))
            if t == '1':
                reseted = clingo.Function(reset(str(atom)))
                if reseted in fluents:
                    atoms.append(reseted)
                    old_ones.append(atom)
                elif reseted in actions:
                    performed_actions.append(reseted)
                    old_ones.append(atom)
        succ_states.append((performed_actions, atoms, int(priority)))
                
    for atom in old_ones:
        params = obtain_params(str(atom))
        name = obtain_name(str(atom))
        domain.assign_external(clingo.Function(name, params), False)
    return succ_states

        
""" Expand function """ 


def expand(domain, node, actions, fluents):
    """ List of succesors of a specific state """
    succersors = []
    """ We obtain the succesor states and the action associated with each one """ 
    for action, result, priority in succesors(domain, node.state, actions, fluents):
        new_node = SearchNode(result, node, action, priority, node.depth + 1)
        succersors.append(new_node)
    return succersors
