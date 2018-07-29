# AUTHOR: Juan Manuel Rey Escobar

import dependency_injector.containers as containers
import dependency_injector.providers as providers

class Fringes(containers.DeclarativeContainer):
""" IoC container of fringe providers """

    heap = providers.Factory(main.fringes.Fringe, 
        
    
