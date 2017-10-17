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
        

    
    def traversal(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next_node

dlinkedlist = DLinkedList()

for i in range(5):
    dlinkedlist.add_last(i)
dlinkedlist.traversal()
    