#AUTHOR: Juan Manuel Rey Escobar
from fringe import Fringe

class FifoQueue(Fringe):
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return len(self.list) == 0
    
    def push(self, element):
        self.list.insert(0,element)
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.list.pop()
        
    def size(self):
        return len(self.list)
