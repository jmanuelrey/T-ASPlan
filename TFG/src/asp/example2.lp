#script(python)
# AUTHOR: Juan Manuel Rey Escobar

""" Script to obtain a list of stable models and from a problem instance,
    and a list of actions for obtaining those models. """
import clingo

        
def main(prg):
    program = clingo.Control([])
    program.configuration.solve.models = 0
    
    # We use a list of lists for the stable models
    states = []

    action_list = []
    
    # We load our logical program.
    program.load("actionsproblem.lp")

    # First, we ground config program.
    program.ground([("config",[])])

    
    iterator = program.solve(yield_ = True)
	
    for element in iterator:
        for atom in element.symbols(atoms = True):
	        if 'action' in str(atom):
	            action_list.append(str(atom)[7:-3])
	            
    # Second, we ground the base program.
    program.ground([("base",[1])])
		
    stable_models = program.solve(yield_ = True)
	
    for model in stable_models:
		atoms = []
		for atom in model.symbols(atoms = True):
			if '0' not in str(atom):
			    if (str(atom)[:-3]) not in action_list:
			        atoms.append(str(atom)[:-3])
		states.append(atoms)
	
    print('Actions: ' + str(len(action_list)))   
    print(action_list)
    print('States: ' + str(len(states)))
    print(states)
		

                      
#end.
