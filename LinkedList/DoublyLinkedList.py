class doublyLinkednode:
    def __init__(self, data):
        self.data = data
        self.prev_node = None
        self.next_node = None
    
    

class DLinkedList:

    def __init__(self):
        self.head = doublyLinkednode(None)
        self.tail = doublyLinkednode(None)     
        self.size = 0
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add(self, data):
        dnode = doublyLinkednode(data)
        if self.is_empty():
            self.head.next_node = dnode
            dnode.prev_node = self.head
            self.tail.prev_node = dnode
            dnode.next_node = self.tail
        else:
            nextnode = self.head.next_node
            self.head.next_node = dnode
            dnode.next_node = nextnode
            
        self.size += 1
        
    def add_last(self, item) :
        dnode = doublyLinkednode(item)
        if self.is_empty():
            self.head.next_node = dnode
            dnode.prev_node = self.head
            self.tail.prev_node = dnode
            dnode.next_node = self.tail
        else:
            prevnode = self.tail.prev_node
            prevnode.next_node = dnode
            self.tail.prev_node = dnode
        self.size += 1

    def find(self, item) :
        found = False
        stop = False
        if self.head is None:
            return found
        else:
            current = self.head
        
        while current is not None and not found:
            if  item == current.data:
                found = True
            else:
                current = current.next_node
                found = False
        return found

    def pop(self, position = None):
        if position is None:
            nextnode = self.head.next_node
            self.head = nextnode.next_node
        elif position == self.size - 1:
            prevnode = self.tail.prev_node
            previous =  prevnode.prev_node
            self.tail = previous
        else:
            if not self.is_empty():
                current = self.head
                while current is not None:
                    pass
        self.size -= 1

    
    def remove(self, item):
        pass
    
    def insert(self, item, position):
        pass
    
    def index(self, position):
        pass
    
    
    def traversal(self):
        current = self.head
        while current :
            if current.data is not None:
                print(current.data)
            current = current.next_node

dlinkedlist = DLinkedList()

'''for i in range(5):
    dlinkedlist.add_last(i)
dlinkedlist.traversal()
print('------ traversal------')'''
dkk = DLinkedList()
for j in range(5):
    dkk.add(j)
#dkk.traversal()
print(dkk.find(7))
print(dkk.pop())
print('--traversing after pop---')
dkk.traversal()
print('-traversing after removing last element using pop')
dkk.pop(3)
dkk.traversal()