#script(python)
# AUTHOR: Juan Manuel Rey Escobar

""" Script to obtain a list of stable models and from a problem instance,
    and a list of actions for obtaining those models. """
import clingo


def feasible(list):
    for element in list:
        if "0" in str(element): list.remove(element)

def returnAction(action):
    if "action" in action: return action[7:-1]

def actionCompare(action, key):
    index = action.find("(")
    return (key == action[:index])

        
def main(prg):
    #problem = str(input('Problem instance: '))
    # We ask for all stable models
    prg.configuration.solve.models = 0

    # We load our logical program.
    prg.load("actionsproblem.lp")

    # Grounding is done just once.
    prg.ground([("load",[1])])

    # We use a list of lists for the stable models
    stableModels = []

    actionList = []



    with prg.solve(yield_ = True) as iterator:
        for element in iterator: 
            atoms = []
            actions = []
            keys = []
            for atom in element.symbols(atoms = True):
                if "action" in str(atom):
                    keys.append(returnAction(str(atom)))

            for atom in element.symbols(atoms = True):  
                if "action" not in str(atom):
                    for key in keys:
                        if (actionCompare(str(atom), key)): actions.append(atom)
                        else: atoms.append(atom)

            feasible(atoms)
            actionList.append(actions)
            stableModels.append(atoms)      
            print(iterator.get())
        
        print('Stable Models: ' + str(len(stableModels)))
        print(stableModels)
        print(' Actions: ' + str(len(actionList)))
        print(actionList)
                      
#end.
