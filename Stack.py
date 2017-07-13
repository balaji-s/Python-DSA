class Stack:

    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items)-1]

stack =  Stack()
stack.push("balaji")
print(stack.size())
