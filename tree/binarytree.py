import sys
sys.path.append("..")
print(sys.path)
from Stack import linkedstack

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
def preordertrav(subtree):

    if subtree is not None:
        print(subtree.root)
        preordertrav(subtree.get_left_child())
        preordertrav(subtree.get_right_child())
            
def inordertraversal(subtree):
    if subtree is not None:
        inordertraversal(subtree.get_left_child())
        print(subtree.root)
        inordertraversal(subtree.get_right_child())

def postordertraversal(subtree):
    if subtree:
        postordertraversal(subtree.get_left_child())
        postordertraversal(subtree.get_right_child())
        print(subtree.root)
def breathFirstTrav(tree):
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

print(rot.get_root_value())
print(rot.get_left_child().get_root_value())
print(rot.get_left_child().get_right_child().get_root_value())
print(rot.get_left_child().get_left_child().get_root_value())

print(rot.get_right_child().get_root_value())
print(rot.get_right_child().get_left_child().get_root_value())
print(rot.get_right_child().get_right_child().get_root_value())

print('------pre order traversal-------')
preordertrav(rot)
print('------in order traversal-------')
inordertraversal(rot)
print('-------------')
print('------post order traversal-------')
postordertraversal(rot)
print('-------breadth first search-------')
breathFirstTrav(rot)
'''    
    a
    b       c
  d   e   f  g    '''

'''_root = BinaryTree(1)
_right = BinaryTree(2)
_root.insert_right(3)'''

def parse_tree(fp_exp):
    fp_list = fp_exp.split()
    myStack = linkedstack()
    fp_tree = BinaryTree('')
    myStack.push(fp_tree)
    currentTree = fp_tree

    for i in fp_list:
        if i =='(':
            currentTree.insert_left('')
            

