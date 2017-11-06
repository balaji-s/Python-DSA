class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, branch):
        if self.left_child is None:
            self.left_child = BinaryTree(branch)
        else:
            tree = BinaryTree(branch)
            tree.left_child = self.left_child
            self.left_child = tree
    
    def insert_right(self, branch):
        if self.right_child is None:
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

    def preordertrav(self, subtree):
        '''pre order traversal
        '''
        if subtree is not None:
            print(subtree.root)
            self.preordertrav(subtree.get_left_child())
            self.preordertrav(subtree.get_right_child())
    def inordertraversal(self, subtree):
        if subtree is not None:
            self.inordertraversal(subtree.get_left_child())
            print(subtree.root)
            self.inordertraversal(subtree.get_right_child())

    def postordertraversal(self, subtree):
        if subtree:
            self.postordertraversal(subtree.get_left_child())
            self.postordertraversal(subtree.get_right_child())
            print(subtree.root)
    def breathFirstTrav(self, tree):
        queue = _Queue()
        queue.enqueue(tree)

        while not queue.is_empty():
            node = queue.dequeue()
            print (node.root)

            if node.get_left_child() is not None:
                queue.enqueue(node.get_left_child())
            if node.get_right_child() is not None:
                queue.enqueue(node.get_right_child())

class _Queue:

    def __init__(self):
        self.queue_items = []
    
    def is_empty(self):
        return self.queue_items == []

    def enqueue(self,item):
        self.queue_items.append(item)
    
    def dequeue(self):
        return self.queue_items.pop(0)
    
    def size(self):
        return len(self.queue_items)


rot = BinaryTree('a')
rot.insert_left('b')
rot.insert_right('c')
rot.get_left_child().insert_left('d')
rot.get_left_child().insert_right('e')
rot.get_right_child().insert_left('f')
rot.get_right_child().insert_right('g')

'''print(rot.get_root_value())
print(rot.get_left_child().get_root_value())
print(rot.get_left_child().get_right_child().get_root_value())

print(rot.get_right_child().get_root_value())
print(rot.get_right_child().get_left_child().get_root_value())
print(rot.get_right_child().get_right_child().get_root_value())'''

print('------pre order traversal-------')
rot.preordertrav(rot)
print('------in order traversal-------')
rot.inordertraversal(rot)
print('-------------')
print('------post order traversal-------')
rot.postordertraversal(rot)
print('-------breadth first search-------')
rot.breathFirstTrav(rot)
'''
        a
    b       c
  d   e   f  g    
'''
_root = BinaryTree(1)
_right = BinaryTree(2)
_root.insert_right()

