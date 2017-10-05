from Node import Node

class UnorderedList:
    def __init__(self):
        self.head = None
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
        while current != None:
            if current.get_data() == item:
                return True
            else :
                print(current.get_data())
                current = current.get_next()
                found = False
        return found

    def remove(self, item):
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

        if previous ==  None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return found
    def lengthUl(self):
        return self.length

ll = UnorderedList()

for i in range(10):
    ll.add(i)

print(ll.lengthUl())
print(ll.remove(9))
print(ll.find(9))
print(ll.lengthUl())

