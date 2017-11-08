class binheap :

    def __init__(self):

        self.size = 0
        self.heaplist = [0]
    
    def insert(self, item):

        self.heaplist.append(item)
        self.size += 1
        self.percolate_item(self.size)
    
    def percolate_item(self, i):

        while i // 2 > 0:
            
            if self.heaplist[i] < self.heaplist[i // 2] :
                temp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[i//2]
                self.heaplist[i//2] = temp
            
            i = i // 2
    

bin_heap = binheap()

bin_heap.insert(5)
bin_heap.insert(3)
bin_heap.insert(7)
bin_heap.insert(4)
bin_heap.insert(2)
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
        
    

