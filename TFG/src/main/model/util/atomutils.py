#!/usr/bin/env python
# AUTHOR: Juan Manuel Rey Escobar

import clingo

""" Obtains a dynamic fluent without parameters """


def obtain_dynamic(atom):
    start = atom.find('(')
    end = atom.find(')')    
    return atom[start + 1:end + 1]


""" Applies a friendly format to actions and fluents """


def decorate_action(action):
    end = action.find(')')    
    return action[:end - 2] + ')'


""" Prints the plan obtained by a search algorithm """


def print_solution(node): 
        plan = []
        while node.parent != None:
            if len(node.action) == 0:
                plan.insert(0, clingo.Function("no action"))
            elif len(node.action) == 1:
                plan.insert(0, clingo.Function(decorate_action(str(node.action[0]))))
            else:
                actions = ()
                for action in node.action:
                    actions.add(clingo.Function(decorate_action(str(action))))
                plan.insert(0, actions)
                
            node = node.parent
        i = 1
        for action in plan:
            print(str(i) + ': '),
            print(action) ,
            print(' ') ,
            i += 1
        print('\n')

        
""" Resets the given atom to t=0 """     


def reset(atom):
    pos = atom.find(')')
    new_atom = atom[:pos - 1]
    return new_atom + '0)'


""" Obtains the temporal parameter t of a given atom """


def obtain_t(atom):
        start = atom.find('(')
        end = atom.find(')')
        new_atom = atom[start + 1:end]
        items = new_atom.split(",")
        return items.pop() 

    
""" Obtains the list of params of a given atom """


def obtain_params(atom):
        params = []
        start = atom.find('(')
        end = atom.find(')')
        new_atom = atom[start + 1:end]
        items = new_atom.split(",")
        for item in items:
            try:
                params.append(int(item))
            except ValueError:
                params.append(clingo.Function(item))
        return params

    
""" Obtains the name of a given atom as a string """ 


def obtain_name(atom):
        pos = atom.find('(')
        new_atom = atom[:pos]
        return new_atom
