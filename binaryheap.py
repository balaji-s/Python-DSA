from Array import Array
class maxheap:

    def __init__(self, maxsize):
        self.heap_array = Array(maxsize)
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add(self, value):
        assert len() < self.is_empty(), "cannot add full heap"
        self.heap_array[self.size] = value
        self.size += 1
        self.percolate(self.size - 1)
    
    def percolate(self, size):
        
    

