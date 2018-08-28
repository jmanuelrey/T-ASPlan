#script(Python)

import clingo

def obtain_dynamic(atom):
    start = atom.find('(')
    end = atom.find(')')    
    return atom[start+1:end+1]

def obtain_t(atom):
    start = atom.find('(')
    end = atom.find(')')
    new_atom = atom[start+1:end]
    items = new_atom.split(",")
    return items.pop() 

def main():
    """ Creates the program object """
    program1 = clingo.Control([])
    program2 = clingo.Control([])
    
    """ We want to obtain ALL possible stable models """
    program1.configuration.solve.models = 0
    program2.configuration.solve.models = 0
    
    """ We initialize data structures """
    states = []
    action_list = []
    fluent_list = []
    initial_state = []
    
    """ Reads from the input file """
    file_name1 = '/home/jmanuel/workspace/TFG/TFG/src/asp/simple.lp'
    file_name2 = '/home/jmanuel/workspace/TFG/TFG/src/asp/simple2.lp'
    program1.load(file_name1)
    program2.load(file_name1)
    
    
    program2.ground([('initial', []), ('types', [0]), ('static', [])])
    #backend = program.backend().__enter__()
    
    models = program2.solve(yield_ = True)
    print('program2:')
    for element in models:
        for atom in element.symbols(atoms = True):
            if 'action' in str(atom):
                action_list.append(clingo.Function(obtain_dynamic(str(atom))))
            elif 'fluent' in str(atom):
                fluent_list.append(clingo.Function(obtain_dynamic(str(atom))))
            else:
                for element in fluent_list:
                    if str(element) == str(atom):
                        initial_state.append(atom)
                for element in action_list:
                    if str(element) == str(atom):
                        initial_state.append(atom)
                        
    print(initial_state)
    print('Actions: ') ,
    print(action_list)
    print('Fluents: ') ,     
    print(fluent_list)
    
    for atom in initial_state:
        program1.add('added',[],str(atom)+".") 
        
    program1.ground([('added', []), ('dynamic', [0]), ('static', [])]) 
    models = program1.solve(yield_ = True)
    print('program1:')
    for element in models:
        for atom in element.symbols(atoms = True):
            t = obtain_t(str(atom))
            if t == '1':
                print(atom)
            
    
            
            
    
            
    

            
         
    














#end.

main()