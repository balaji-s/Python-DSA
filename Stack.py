class Stack:
    """
    List based implemenation of stack
    """
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items)-1]
  

'''stack = Stack()
stack.push('balaji')
print(stack.pop())
print(stack.size())
stack.push(True)
stack.push(2)
print(stack.pop())
print(stack.size())
print(stack.peek())
print(stack.pop())
print(stack.size())
stack.push("aa")
stack.push("birni")
stack.push("irnib")
print(stack.size())
print(stack.peek())'''

class sNode:

    def __init__(self, data,next_node = None ):
        self.data = data
        self.next_node = next_node
    

class linkedstack:
    """
    Linked list based implementation of stack
    """ 
    def __init__(self):

        self._head = None
        self.size = 0
    
    def push(self, item):
        node = sNode(item)
        node.next_node = self._head
        self._head = node
        self.size += 1

    
    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if not self.is_empty():
            return self._head.data
    
    def pop(self):
        node = self._head.data
        self._head = self._head.next_node
        self.size -= 1
        return node

linstack = linkedstack()

for i in range(4):
    linstack.push(i)
print(linstack.size)
print(linstack.peek())
print(linstack.pop())
print(linstack.size)
print(linstack.pop())
print(linstack.peek())
print(linstack.size)

