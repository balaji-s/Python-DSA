class binheap :

    def __init__(self):

        self.size = 0
        self.heaplist = [0]
    
    def insert(self, item):

        self.heaplist.append(item)
        self.size += 1
        self.percolate_item(self.size)
    
    def percolate_item(self, current_size):

        while current_size // 2 > 0:
            
            if self.heaplist[current_size] < self.heaplist[current_size // 2] :
                temp = self.heaplist[current_size]
                self.heaplist[current_size] = self.heaplist[current_size//2]
                self.heaplist[current_size//2] = temp
            
            current_size = current_size // 2
    
    def del_min(self):
        value = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.size -= 1
        self.heaplist.pop()
        self.percolate_down(1)
        return value
    
    def percolate_down(self, element):
        while (element * 2) <= self.size :
            minimum = self.minimum_child(element)
            if self.heaplist[element] > self.heaplist[minimum] :
                temp  = self.heaplist[element]
                self.heaplist[element] = self.heaplist[minimum]
                self.heaplist[minimum] = temp
            element = minimum
    
    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.size = len(a_list)
        self.heaplist = [0] + a_list[:]
        while i > 0 :
            self.percolate_down(i)
            i -= 1
    
    def minimum_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i* 2 +1

  




    

bin_heap = binheap()

my_list = [2,3,-1, 0, 4,5,-4,21,22]
for i in my_list:
    bin_heap.insert(i)

bin_heap.del_min()
print(bin_heap.heaplist)
print(bin_heap.del_min())
print(bin_heap.heaplist)



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
        pass
        
    

