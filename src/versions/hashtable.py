# AUTHOR: Juan Manuel Rey Escobar

class Hashtable:
    # Creates a hash table.
    def __init__(self, numLists, keySize):
        # Array of lists
        self.lists = [None] * numLists
        # Number of lists (use a prime number)
        self.numLists = numLists
        # Fixed size for all keys
        self.keySize = keySize

    # Compares two hash entries using their keys.   
    def entryCmp(self, entry1, entry2):
    

    # Computes the hash value for a given key.
    def hashValue(self, key):

    # Inserts an element in the hash table.
    def hashInsert(self, key, data):

    # Searchs the first entry which is greater of equal than entry.
    def geqEntry(self, queue, entry):
    
    # Seachrs for entry 'entry'
    # Returns 0 if the key was not found.
    # Returns 1 if the key was found.
    def hashFind(entry):

    # Delete all lists.
    def hashFree(self):
