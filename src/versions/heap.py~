# AUTHOR: Juan Manuel Rey Escobar

class BinaryHeap:
    # Creates a binary heap
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    """ Private method that perlocates a new item as far up in the tree 
        as it needs to maintain the heap property """
    def __percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    
    """ Inserts a new item to the heap """
    def insert(self, item):
        self.heapList.append(item)
        self.currentSize = self.currentSize + 1
        self.__percUp(self.currentSize)

    """ Private method that is used inside percDown """
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
    """ Method for maintaining the heap order property """
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]    
                self.heapList[mc] = tmp

            i = mc

    """ Deletes the minimum element """
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
               
        
