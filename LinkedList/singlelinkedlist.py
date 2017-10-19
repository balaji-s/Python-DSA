from Node import Node
'''
importing node module from node
'''
class LinkedList:
    """
    Linked list implementation with head and tail reference
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_last(self, item):
        node = Node(item)
        if self.is_empty():
            node.set_next(self.head)
            self.head = node
        else:
            self.tail.set_next(node)
        
        self.tail = node
        self.size += 1
    
    def traversal(self):
        current = self.head
        while current is not None:
            print(current.get_data())
            current = current.get_next()
    def remove(self, item):
        current = self.head
        previous = None
        while current is not None and current.get_data() != item:
            previous = current
            current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            if current.get_next() is None:
                previous.set_next(current.get_next())
                self.tail = previous
            else:
                previous.set_next(current.get_next())
        self.size -= 1
    
    def pop(self, position = None):
        current = self.head
        previous = None
        count = 0
        if position is not None and position > self.size:
            raise Exception("position is greater than zero")
        if position is None or position == 0:
            item = current
            self.head = current.get_next()
            self.size -= 1
            
        else:
            while current.get_next() is not None and count < position:
                previous = current
                current = current.get_next()
                item = current
                count += 1
        
            if current.get_next() is None:
                previous.set_next(current.get_next())
                self.tail = previous
            else:
                previous.set_next(current.get_next())
        self.size -= 1
        return item.get_data()
    def insert(self, item, position = None):
        """
        inserts the item at particular location

        """
        previous = None
        count = 0
        current = self.head
        if position is None or position == 0:
            self.add(item)
        elif position == self.size :
            self.add_last(item)
        else:
            while count < position:
                previous = current
                current = current.get_next()
                count += 1
            node = Node(item)
            previous.set_next(node)
            node.set_next(current)
            self.size += 1

    def index(self, position) :
        """
            gets the item at the corresponding position
        """
        current = self.head
        if position == 0:
            return self.head.get_data()
        elif position == self.size:
            return self.tail.get_data()
        else:
            count = 0
            while count < position:
                current = current.get_next()
                count += 1
            return current.get_data()

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            node.set_next(self.head)
            self.head = node
            self.tail = node
        else:
            node.set_next(self.head)
            self.head = node
        self.size += 1

singlell = LinkedList()

'''for i in range(5):
    singlell.add(i)'''
'''print('-- traversal---')
singlell.traversal()
print('-- traversal---')
print('tail data - before removing anything ',singlell.tail.data)

singlell.remove(4)

print('-- traversal after removing head---')
singlell.traversal()
print('-- traversal---')
print('tail data - ', singlell.tail.data)
singlell.remove(0)
print('tail data - ', singlell.tail.data)
print('----traversal- after removing tail---')
singlell.traversal()
print('-- traversal---')

singlell.remove(2)
print(singlell.tail.data)
print('----traversal- after removing mid---')
singlell.traversal()
print('-- traversal---')

singlell.pop()
print('after popping top item')
singlell.traversal()
print('--------')
singlell.pop(1)
singlell.traversal()
print('self tail after removing 1st postion', singlell.tail.data)

print('pop on positon three',singlell.pop(2))
print('self tail after removing last postion', singlell.tail.data)
singlell.traversal()
print(len(singlell))'''

singlell.insert(0)
singlell.insert(1,1)
singlell.insert(2,2)
singlell.insert(3,2)
singlell.add(4)
singlell.add_last(5)
'''print('tail data',singlell.tail.data)
print('tail data',singlell.tail.data)

print('---traversal---')
singlell.traversal()
print('tail data', singlell.tail.data)'''
#singlell.traversal()
#print('tail data', singlell.tail.data)
#print('tail data', singlell.tail.data)
#singlell.traversal()

print('printing indexes')
for i in range(6):
    print(singlell.index(i))