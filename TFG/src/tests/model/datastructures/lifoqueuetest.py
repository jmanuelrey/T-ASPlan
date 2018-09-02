#AUTHOR: Juan Manuel Rey Escobar

import unittest
from TFG.src.main.model.datastructures.lifoqueue import LifoQueue

class LifoQueueTest(unittest.TestCase):   
    def test_push(self):
        q = LifoQueue()
        for i in range(5):
            q.push(i)
        self.assertEqual(q.list, [0,1,2,3,4])
    
    def test_pop(self):
        q = LifoQueue()
        q.list = [0,1,2,3,4]
        self.assertEqual(q.pop(), 4)
          
    def test_is_empty(self):
        q = LifoQueue()
        q.list = [0,1,2,3,4]
        self.assertFalse(q.is_empty())
        
    def test_size(self):
        q = LifoQueue()
        q.list = [0,1,2,3,4]
        self.assertEqual(q.size(),5)