#script(python)
# AUTHOR: Juan Manuel Rey Escobar

""" Script to obtain a list of stable models from a problem instance. """
import clingo
import sys
sys.path.append('../')
import main.model.datastructures.hash

def feasible(list):
    for element in list:
        if "0" in str(element): list.remove(element)
        
        
def main(prg):
    #problem = str(input('Problem instance: '))
    # We ask for all stable models
    prg.configuration.solve.models = 0

    # We load our logical program.
    prg.load("gunproblem.lp")

    # Grounding is done just once.
    prg.ground([("load",[1])])

    # We use a list of lists for the stable models
    stableModels = []


    # We iterate over the solution(s)
    with prg.solve(yield_ = True) as iterator:
        for element in iterator: 
            atoms = []
            for atom in element.symbols(atoms = True):
                atoms.append(atom)
            feasible(atoms)
            stableModels.append(atoms)      
            print(iterator.get())
        
        print('Stable Models:' + str(len(stableModels)))
        print(stableModels)
                      
#end.


