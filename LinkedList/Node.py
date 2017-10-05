class Node(object):

    def __init__(self,data = None, next = None):
        self.data = data
<<<<<<< HEAD
        self.next = next
=======
        self.node = None
>>>>>>> master
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.node

    def set_data(self, data):
        self.data = data
    
<<<<<<< HEAD
    def set_next(self, next):
        self.next = next
    def __str__(self):
        return str(self.data)


temp = Node("birni")
temp1 = Node("irnib")
temp.next = temp1
print(temp)
print(temp.get_data())
=======
    def set_next(self, node):
        self.node = node




>>>>>>> master
