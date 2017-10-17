class linkedqueue :

    '''Linked list implementation of queue
    '''
    
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0
    
    def is_empty(self):
        return self._count == 0

    def enqueue(self, item):
        e_node = _qnode(item)
        if self.is_empty():
            self._qhead = e_node
        else:
            self._qtail.next = e_node # line no 20 e_node.next
        self._qtail = e_node
        self._count += 1
    
    def dequeue(self):
        if not self.is_empty():
            item = self._qhead.data
            self._qhead = self._qhead.next
            self._count -= 1
            return item

    def __len__(self):
        return self._count


class _qnode(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class circularLinkedList:

    def __init__(self):
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        node = _qnode(item)
        if self.is_empty():
            node.next = node
        else:
            node.next = self.tail.next
            self.tail.next = node
        self.tail = node
        self.size += 1

    def traversal(self):
        current = self.tail
        count = 0
        while count < len(self) :
            print(current.data)
            current = current.next
            count += 1
    def dequeue(self):
        if not self.is_empty():
            node = self.tail.next
            if self.size == 1:
                self.tail = None
            else:
                self.tail.next = node.next
            self.size -= 1
            return node.data

    def rotate(self):
        if self.size > 0:
            self.tail = self.tail.next
    
    def traversal(self):
        current = self.tail
        count = 0
        while count < len(self) :
            print(current.data)
            current = current.next
            count += 1

circularll = circularLinkedList()

circularll.enqueue(12)
circularll.enqueue(-1)
circularll.enqueue(22)
circularll.enqueue(2)

circularll.traversal()


class orderedCircularLinkedList:

    def __init__(self):
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        current = self.tail
        previous = None
        count = 0 
        stop = False
        while count < len(self) and not stop :
            if current.data > item :
                stop = True
            else:
                previous = current
                current = current.next
        node = _qnode(item)
        if previous is  None:
            node.next = node
        else:
            previous.next = node
            self.tail.next = node
        self.tail = node
        self.size += 1
            


oo = orderedCircularLinkedList()   
oo.enqueue(12)
oo.enqueue(-1)
oo.enqueue(22)
oo.enqueue(2)

oo.traversal()


    

'''llqueue = linkedqueue()
for i in range(4):
    llqueue.enqueue(i)
    
for i in range(4):
    print(llqueue.dequeue())'''
