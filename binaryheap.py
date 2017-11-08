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