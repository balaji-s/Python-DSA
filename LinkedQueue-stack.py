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
            self._qtail.next = e_node // line no 20 e_node.next
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


class       

llqueue = linkedqueue()
for i in range(4):
    llqueue.enqueue(i)
    
for i in range(4):
    print(llqueue.dequeue())
