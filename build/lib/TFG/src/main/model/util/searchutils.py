# AUTHOR: Juan Manuel Rey Escobar

import clingo
from TFG.src.main.model.util.atomutils import reset
from TFG.src.main.model.util.atomutils import obtain_name
from TFG.src.main.model.util.atomutils import obtain_params
from TFG.src.main.model.util.atomutils import obtain_t
from TFG.src.main.model.util.atomutils import obtain_n
from TFG.src.main.model.search.searchnode import SearchNode

""" Succesors is called by expand to obtain the next possible states """   


def succesors(domain, state, actions, fluents, use_heuristic):
    priority = -1
    succ_states = []
    old_ones = state[:]
    for atom in state:
        params = obtain_params(str(atom)) 
        name = obtain_name(str(atom)) 
        domain.assign_external(clingo.Function(name, params), True)
             
    models = domain.solve(yield_=True)
    
    for element in models:
        priority = -1
        cost = -1
        atoms = []
        performed_actions = []
        for atom in element.symbols(atoms=True):
            if (use_heuristic == True) and ((obtain_name(str(atom))) == "heuristics"):
                priority = obtain_n(str(atom))
            if (obtain_name(str(atom))) == "cost":
                cost = obtain_n(str(atom))
            t = obtain_t(str(atom))
            if t == '1':
                reseted = clingo.Function(reset(str(atom)))
                if reseted in fluents:
                    atoms.append(reseted)
                    old_ones.append(atom)
                elif reseted in actions:
                    performed_actions.append(reseted)
                    old_ones.append(atom)
        succ_states.append((performed_actions, atoms, int(priority),int(cost)))
                
    for atom in old_ones:
        params = obtain_params(str(atom))
        name = obtain_name(str(atom))
        domain.assign_external(clingo.Function(name, params), False)
    return succ_states

        
""" Expand function """ 


def expand(domain, node, actions, fluents, use_heuristic, bfs):
    """ List of succesors of a specific state """
    succersors = []
    priority_value = 0
    cost_value = 0
    """ We obtain the succesor states and the action associated with each one """ 
    for action, result, priority, cost in succesors(domain, node.state, actions, fluents, use_heuristic):
        if priority != -1:
            priority_value = priority
        if cost != -1:
            cost_value = cost
        else:
            cost_value = node.pathCost + 1
          
        if bfs == "greedy":
            new_node = SearchNode(result, node, action, cost_value , node.depth + 1, priority_value)
        else:
            new_node = SearchNode(result, node, action, cost_value , node.depth + 1, priority_value + cost_value)
            
        succersors.append(new_node)
    return succersors
