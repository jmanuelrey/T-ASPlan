#AUTHOR: Juan Manuel Rey Escobar

import unittest
from TFG.src.main.model.datastructures.priorityqueue import PriorityQueue

class PriorityQueueTest(unittest.TestCase):   
    def test_push(self):
        q = PriorityQueue()
        for i in range(5):
            q.push((i,str(i)))
        self.assertEqual(q.list, [(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4')])
        
    def test_pop(self):
        q = PriorityQueue()
        q.list = [(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4')]
        self.assertEqual(q.pop(), '0')
        
    def test_is_empty(self):
        q = PriorityQueue()
        q.list = [(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4')]
        self.assertFalse(q.is_empty())

    def test_size(self):
        q = PriorityQueue()
        q.list = [(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4')]
        self.assertEqual(q.size(),5)