#AUTHOR: Juan Manuel Rey Escobar
import heapq 
from TFG.src.main.model.datastructures.fringe import Fringe

class PriorityQueue(Fringe):
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return len(self.list) == 0
    
    def push(self, element):
        heapq.heappush(self.list, (element.priority, element))
    
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            return heapq.heappop(self.list)[1]
        
    def size(self):
        return len(self.list)
        