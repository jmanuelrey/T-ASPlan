# AUTHOR: Juan Manuel Rey Escobar

import clingo
import time
from searchnode import SearchNode
from memory_profiler import memory_usage

def print_solution(node): 
        plan = []
        while node.parent != None:
            plan.insert(0,node.action)
            node = node.parent
        print(plan)
            
class Search:
    def __init__(self,domain):
        self.domain = domain
        
    def reset(self,atom):
        pos = atom.find(')')
        new_atom = atom[:pos-1]
        return new_atom + '0)'

    def obtain_t(self, atom):
        start = atom.find('(')
        end = atom.find(')')
        new_atom = atom[start+1:end]
        items = new_atom.split(",")
        return items.pop() 

    def obtain_params(self,atom):
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
    
    def obtain_name(self, atom):
        pos = atom.find('(')
        new_atom = atom[:pos]
        return new_atom
            
    """ Succesors if called by expand to obtain the next possible states """   
    def succesors(self, state, actions, fluents):
        succ_states = []
        old_ones = state[:]
        for atom in state:
            params = self.obtain_params(str(atom)) 
            name = self.obtain_name(str(atom)) 
            self.domain.assign_external(clingo.Function(name,params), True)
            
        models = self.domain.solve(yield_ = True)
            
        
        for element in models:
            atoms = []
            performed_actions = []
            for atom in element.symbols(atoms = True):
                t = self.obtain_t(str(atom))
                if t == '1':
                    reseted = clingo.Function(self.reset(str(atom)))
                    if reseted in fluents:
                        atoms.append(reseted)
                        old_ones.append(atom)
                    elif reseted in actions:
                        performed_actions.append(reseted)
                        old_ones.append(atom)
            succ_states.append((performed_actions,atoms))

                
        for atom in old_ones:
            params = self.obtain_params(str(atom))
            name = self.obtain_name(str(atom))
            self.domain.assign_external(clingo.Function(name,params), False)
        return succ_states
                        
        
    """ Expand function """ 
    def expand(self, node, actions, fluents):
        """ List of succesors of a specific state """
        succersors = []
        """ We obtain the succesor states and the action associated with each one """ 
        for action,result in self.succesors(node.state,actions,fluents):
            new_node = SearchNode(result, node, action, node.pathCost + 1, node.depth + 1)
            succersors.append(new_node)
        return succersors
            
        
    def graph_search(self, initial, fringe, goal, actions, fluents):
        """ Fringe: data structure for storing search nodes """
        fringe = fringe
        """ Maximum number of nodes in the fringe """
        max_size = 0
        """ Number of explored nodes """
        explored = 0
        """ Set of visited nodes """
        closed = set()
        """ Node which stores the initial state """
        root_node = SearchNode(initial, None, [], 0, 0)
        fringe.push(root_node)
        max_size+= 1
        """ The instant which marks the start of the execution """
        start = time.time()
        i = 0
        while 1:
            i+=1
            """ Empty fringe means there are no solution """
            if fringe.is_empty():
                """ The instant which marks the end of the execution """ 
                end = time.time()
                """ The amount of memory usage in MB """
                memory = memory_usage()
                print('UNSATISFIABLE')
                print('Execution time: ') ,
                print(end - start) ,
                print('ms')
                print('Memory usage: ') ,
                print(memory[0]) ,
                print('MB')
                print('Explored states: ') ,
                print(explored) 
                print('Maximum number of states stored: ') ,
                print(max_size) 
                return 0
            
            """ Recover fringe's frist node """
            node = fringe.pop()
            """ We check if the recovered node is a posible solution """
            if frozenset(node.state) == frozenset(goal):
                """ The instant which marks the end of the execution """
                end = time.time()
                """ The amount of memory usage in MB """
                memory = memory_usage()
                print('SATISFIABLE')
                print('Solution found: ')
                print(node.state)
                print('Execution time: ') ,
                print(end - start) ,
                print('ms')
                print('Memory usage: ') ,
                print(memory[0]) ,
                print('MB')
                print('Explored states: ') ,
                print(explored)
                print('Maximum number of states stored: ') ,
                print(max_size) 
                print('Obtained plan: ') ,
                print_solution(node)
                return 1
            """ If it is not a solution, then we have to store it in closed """
            if frozenset(node.state) not in closed:
                closed.add(frozenset(node.state))
                explored = explored + 1
                for child in self.expand(node,actions,fluents):
                    fringe.push(child)
                    max_size+=1
            
            
                

               
    
    
    
        

