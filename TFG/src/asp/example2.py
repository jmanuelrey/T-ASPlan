#script(python)
# AUTHOR: Juan Manuel Rey Escobar

""" Script to obtain a list of stable models and from a problem instance,
    and a list of actions for obtaining those models. """
import clingo
import sys
import os

def clean_atom(atom):
    pos = atom.find('(')    
    return atom[:pos]

def main(program):
    program.configuration.solve.models = 0
    
    # We use a list of lists for the stable models
    states = []

	# We use a list for store all atoms which correspond to actions and fluents
    action_list = []
    fluent_list = []
    
    # We load our logical program.
    program.load('wolf.lp')

    # First, we ground types program.
    program.ground([("types",[])])

    
    iterator = program.solve(yield_ = True)
	
    for element in iterator:
        for atom in element.symbols(atoms = True):
            if 'action' in str(atom):
                action_list.append(clingo.Function(str(atom)[7:-3]))
            elif 'fluent' in str(atom):
                fluent_list.append(clingo.Function(str(atom)[7:-3]))
            
                

                  
                    
                    
	            
    # Second, we ground the dynamic program.
    program.ground([("initial",[]), ("static",[]), ("dynamic",[0]), ("final",[0])])
    
		
    stable_models = program.solve(yield_ = True)
	
    for model in stable_models:
		atoms = []
		actions = []
		for atom in model.symbols(atoms = True):
			if '0' not in str(atom):
			    if (clingo.Function(clean_atom(str(atom)))) in action_list:
			        actions.append(atom)
			    elif (clingo.Function(clean_atom(str(atom)))) in fluent_list:
			    	atoms.append(atom)
                    
		states.append((atoms,actions))
    print('States: ' + str(len(states)))
    print('Actions: ') ,
    print(action_list)
    print('Fluents: ') ,
    print(fluent_list)
    for fst,scd in states:
    	print('State: ') ,
    	print(fst) ,
    	print('Action: ') ,
    	print(scd)
		

                      
#end.

program = clingo.Control([])
main(program)
