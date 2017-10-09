from Queue import Queue 

class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None
    def insert_left(self, branch):
        if self.left_child == None:
            self.left_child = BinaryTree(branch)
        else:
            tree = BinaryTree(branch)
            tree.left_child = self.left_child
            self.left_child = tree
    
    def insert_right(self, branch):
        if self.right_child == None:
            self.right_child = BinaryTree(branch)
        else:
            tree = BinaryTree(branch)
            tree.right_child = self.right_child
            self.right_child = tree
    
    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child
    
    def set_root_val(self, value):
        self.root = value
    
    def get_root_value(self):
        return self.root

    def preOrderTrav(self, subtree):
        if subtree is not None:
            print(subtree.root)
            self.preOrderTrav(subtree.get_left_child())
            self.preOrderTrav(subtree.get_right_child())
    
    def inOrderTrav(self, subtree):
        if subtree is not None:
            self.preOrderTrav(subtree.get_left_child())
            print(subtree.root)
            self.preOrderTrav(subtree.get_right_child())

    def postOrderTrav(self, subtree):
        if subtree is not None:
            self.preOrderTrav(subtree.get_left_child())
            self.preOrderTrav(subtree.get_right_child())
            print(subtree.root)
    def breathFirstTrav(tree):
        queue = Queue()
        queue.enqueue(tree)

        while not queue.is_empty():
            node = queue.dequeue()
            print (node.root)

            if node.get_left_child() is not None:
                queue.enqueue(node.get_left_child())
            if node.get_right_child() is not None:
                queue.enqueue(node.get_right_child())


rot = BinaryTree('a')
rot.insert_left('b')
rot.insert_right('c')
rot.get_left_child().insert_right('d')
rot.get_left_child().insert_left('e')
rot.get_right_child().insert_left('f')
rot.get_right_child().insert_right('g')

'''print(rot.get_root_value())
print(rot.get_left_child().get_root_value())
print(rot.get_left_child().get_right_child().get_root_value())

print(rot.get_right_child().get_root_value())
print(rot.get_right_child().get_left_child().get_root_value())
print(rot.get_right_child().get_right_child().get_root_value())'''

rot.preOrderTrav(rot)
print('-------------')
rot.inOrderTrav(rot)
print('-------------')
rot.postOrderTrav(rot)
print('--------------')
rot.breathFirstTrav(rot)
'''
        a
    b       c
  e    d   f  g    
'''
