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

def obtain_params(atom):
    params = []
    start = atom.find('(')
    end = atom.find(')')
    new_atom = atom[start+1:end]
    items = new_atom.split(",")
    for item in items:
        try:
            params.append(int(item))
        except ValueError:
            params.append(clingo.Function(item))
    return params

def obtain_name(atom):
    pos = atom.find('(')
    new_atom = atom[:pos]
    return new_atom

def reset(atom):
    pos = atom.find(')')
    new_atom = atom[:pos-1]
    return new_atom + '0)'
    
    
    

def main():
    """ Creates the program object """
    program1 = clingo.Control([])
    program2 = clingo.Control([])
    
    """ We want to obtain ALL possible stable models """
    program1.configuration.solve.models = 0
    program2.configuration.solve.models = 0
    
    program1.configuration.solve.opt_mode = "ignore"
    
    """ We initialize data structures """
    states = []
    action_list = []
    fluent_list = []
    initial_state = []
    
    """ Reads from the input file """
    file_name1 = '/home/jmanuel/workspace/TFG/TFG/src/asp/wolf.lp'
    file_name2 = '/home/jmanuel/workspace/TFG/TFG/src/asp/simple2.lp'
    program1.load(file_name1)
    program2.load(file_name1)
    
    
    program2.ground([('initial', []), ('types', [0]), ('static', [])])   
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
    
    for atom in fluent_list:
        program1.add('added',[],"#external" + " " + str(atom) + ".") 
        
    program1.ground([('added', []), ('dynamic', [0]), ('static', [])]) 
    
    for atom in initial_state:
        params = obtain_params(str(atom))
        name = obtain_name(str(atom))
        print(name) ,
        print(params)
        program1.assign_external(clingo.Function(name,params), True)
        
    models = program1.solve(yield_ = True)
    
    print('program1:')
    old_ones = initial_state[:]
    del initial_state[:]
    for element in models:
        for atom in element.symbols(atoms = True):
            t = obtain_t(str(atom))
            if t == '1':
                old_ones.append(atom)
                initial_state.append(clingo.Function(reset(str(atom))))
    print(initial_state)
    print(old_ones)
                
    for atom in old_ones:
        params = obtain_params(str(atom))
        name = obtain_name(str(atom))
        print(name) ,
        print(params)
        program1.assign_external(clingo.Function(name,params),False)
     
    print('initial')                   
    for atom in initial_state:
        params = obtain_params(str(atom))
        name = obtain_name(str(atom))
        print(name) ,
        print(params)
        program1.assign_external(clingo.Function(name,params), True)
        
    models = program1.solve(yield_ = True)
    
    print('program1:')
    old_ones = initial_state[:]
    del initial_state[:]
    for element in models:
        for atom in element.symbols(atoms = True):
            t = obtain_t(str(atom))
            if t == '1':
                old_ones.append(atom)
                initial_state.append(clingo.Function(reset(str(atom))))
    print(initial_state)
    print(old_ones)


                
            
    
            
            
    
            
    

            
         
    














#end.

main()