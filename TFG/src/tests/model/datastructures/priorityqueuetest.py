#AUTHOR: Juan Manuel Rey Escobar

import sys
import unittest
sys.path.append('/home/jmanuel/workspace/TFG/TFG/src')
from main.model.datastructures.priorityqueue import PriorityQueue

class PriorityQueueTest(unittest.TestCase):   
    def test_push(self):
        q = PriorityQueue()
        for i in range(5):
            q.push(i)
        self.assertEqual(q.list, [0,1,2,3,4])
        
        
    def test_pop(self):
        q = PriorityQueue()
        q.list = [0,1,2,3,4]
        self.assertEqual(q.pop(), 0)
        
        
        
    def test_is_empty(self):
        q = PriorityQueue()
        q.list = [0,1,2,3,4]
        self.assertFalse(q.is_empty())
