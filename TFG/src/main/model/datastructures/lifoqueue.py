#AUTHOR: Juan Manuel Rey Escobar
from fringe import Fringe

class LifoQueue(Fringe):
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return len(self.list) == 0
    
    def push(self, element):
        self.list.append(element)
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.list.pop()