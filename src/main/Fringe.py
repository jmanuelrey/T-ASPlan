# AUTHOR: Juan Manuel Rey Escobar

class Fringe:
""" The fringe is the heart of the graphSearch. It can be implemented by 
    several ways """

    @abstractmethod
    insert(): """ inserts a node in the fringe """

    @abstractmethod
    Pop(): """ returns and eliminates a node """

    @abstractmethod
    create(): """ initializes a fringe """
        
    
