# AUTHOR: Juan Manuel Rey Escobar

from _pyio import __metaclass__
from abc import ABCMeta
from abc import abstractmethod

class Fringe(object):
    __metaclass__ = ABCMeta
    
    """ Pushes an element to the fringe """
    @abstractmethod
    def push(self, element):
        return
    
    """ Returns and removes the next element from the fringe """
    @abstractmethod
    def pop(self):
        return
    
    """ Returns a boolean value """
    @abstractmethod
    def is_empty(self):
        return
    
    """ Returns a the number of elements stored in the fringe """
    @abstractmethod
    def size(self):
        return
        
    
