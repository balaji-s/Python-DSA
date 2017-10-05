class Node:

    def __init__(self,data):
        self.data = data
        self.node = None
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.node

    def set_data(self, data):
        self.data = data
    
    def set_next(self, node):
        self.node = node




