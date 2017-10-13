from Node import Node

class UnorderedList:
    def __init__(self, node = None):
        self.head = node
        self.length = 0
    
    def is_empty(self):
        return self.head == None

    def add(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node
        self.length += 1

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def find(self, item):
        current = self.head
        found = False
        while current is not None and current.get_data() != item:
            if current.get_data() == item:
                return True
            else :
                current = current.get_next()
                found = False
        return found

    def remove(self, item):
        """Remove an item from LinkedList.
        """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
                self.length -= 1
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
           previous.set_next(current.get_next())
        
        return found
    def lengthUl(self):
        return self.length

    def traversal(self):
        current = self.head
        while current is not None:
            print(current.get_data())
            current = current.get_next()
    
    def __iter__(self):
        return _llIterator(self.head)

class _llIterator:

    def __init__(self, llist):
        self.llist = llist
    
    def __next__(self):
        if self.llist.get_next() is None:
            raise StopIteration
        else:
            item = self.llist.get_data()
            self.llist = self.llist.get_next()
            return item

    def __iter__(self):
        return self

ll = UnorderedList()

for i in range(11):
    ll.add(i)

print(ll.remove.__doc__)
print('size', ll.size())
print(ll.remove(4))
print('size', ll.size())
ll.traversal()

for i in ll:
    print(i)

