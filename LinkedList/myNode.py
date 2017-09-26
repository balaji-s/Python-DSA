class Node:
    
    
  
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

    def djs(self,node):
        if node.next == None:
            return
        print(node)
        self.djs(node.next)
        

    def printNode(node):
        while node:
            print(node)
            node = node.next
  

node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4


node1.djs(node1)
print(node1, node2)
