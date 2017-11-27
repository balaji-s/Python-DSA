class BinHeap:
    '''
      implements a binary heap
    '''
    def __init__(self):

        self.heaplist = [0]
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def add(self, item):
        self.heaplist.append(item)
        self.size += 1
        self.percolate_up(self.size)

        
    def percolate_up(self, current_size):
        while current_size // 2 > 0:
            if self.heaplist[current_size] < self.heaplist[current_size // 2]:
                temp = self.heaplist[current_size]
                self.heaplist[current_size] = self.heaplist[current_size // 2]
                self.heaplist[current_size // 2 ] = temp
            current_size = current_size // 2

    def delete_minimum (self):
        minimum = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.size -= 1
        self.heaplist.pop()
        self.percolate_down(1)
        return minimum

    def percolate_down(self, ele):
        while (ele * 2)  <= self.size:
            child = self.minimum_child(ele)
            print(child)
            if self.heaplist[ele] > self.heaplist[child]:
                self.heaplist[ele], self.heaplist[child] = self.heaplist[child],self.heaplist[ele]
            ele = child
    def print_list(self):
        print(self.heaplist)
    
    def minimum_child(self, ele):
        if ele * 2 + 1 > self.size :
            return ele * 2
        else:
            if self.heaplist[ele] < self.heaplist[ele * 2 + 1]:
                return ele * 2
            else:
                return ele * 2 + 1



bin_heap =BinHeap()

bin_heap.add(5)
bin_heap.add(9)
bin_heap.add(7)
bin_heap.add(14)
bin_heap.add(18)

print(bin_heap.delete_minimum())
bin_heap.print_list()
print(bin_heap.delete_minimum())

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


def parse_tree(fp_exp):
    fp_list = fp_exp.split()
    fp_tree = Binarytree(' ')
    

