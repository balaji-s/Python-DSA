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

'''for i in range(4):
    linstack.push(i)
print(linstack.size)
print(linstack.peek())
print(linstack.pop())
print(linstack.size)
print(linstack.pop())
print(linstack.peek())
print(linstack.size)'''



def super_reduced_string(s):
    my_stack = Stack()
    for element in s:
        if my_stack.is_empty():
            my_stack.push(element)
        else:
            bb = my_stack.peek()
            if bb == element:
                my_stack.pop()
            else:
                my_stack.push(element)
    result =""
    for ele in my_stack.items:
       result = result + ele
    return result

print(super_reduced_string("aaabccddd"))
result =""
k = 87
value = k % 26
#middle-Outz
#sojjrk-Ua
#6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr
print(value)
for char in '6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr':
    if char.isalpha():
        if char.isupper():
            ordinal = ord(char)
            intermediate = ordinal + value
            if intermediate > 90:
                ord_ord =intermediate-90 + 64
                my_char = chr(ord_ord)
                result = result + my_char
            else:
                result = result + chr(intermediate)
        else:
            ordinal = ord(char)
            intermediate = ordinal + value
            if intermediate > 122:
                ord_ord = intermediate-122 + 96
                my_char = chr(ord_ord)
                result = result + my_char
            else:
                result = result + chr(intermediate)
    else:
        result = result + char
print (result)

S ='SOSOOSOSOSOSOSSOSOSOSOSOSOS'

messages = len(S) // 3

split_sos = []

while S:
    split_sos.append(S[:3])
    S = S[3:]
result1 = 0
sos ='SOS'
print(split_sos)
for letter in split_sos:
    if letter != 'SOS':
        count = 0
        for l in letter:
            if l!=sos[count]:
                result1 +=1
            count += 1
#print(result1)
lili =['hereiamstackerrank','hackerworld']
for a0 in lili:
    
    # your code goes here
    hk ='hackerrank'
    count = 0
    result =''
    success = False
    for lc, letter in enumerate(a0):
        if letter == hk[count]:
            result += letter
            success = True
            count += 1
            if count == len(hk):
                break
    if result == hk:
        print('YES')
    else:
        print('NO')
