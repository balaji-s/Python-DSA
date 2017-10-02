class Node:
    
    
  
    def __init__(self, data = None, node = None):
        self.data = data
        self.node = node
    
    def __str__(self):
        return str(self.data)

    def add(self, item):
        temp = Node(item)
        if self.data is None:
           self. __init__(item)
        else:
            self.node = temp


        



    def printNode(self,node):
        if node.node is  None:
            return
        print(node)
        self.printNode(node.node)
        

    
  
node = Node()
for i in range(10):
    node.add(i)

node.printNode(node)





