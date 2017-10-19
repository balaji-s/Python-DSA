from Array import Array
<<<<<<< HEAD


=======
>>>>>>> master
class Queue:
    '''
    List based implementation
    '''
    def __init__(self):
        self.queue_items = []
    
    def is_empty(self):
        ''' checks if the queue is empty'''
        return self.queue_items == []

    def enqueue(self,item):
        self.queue_items.append(item)
    
    def dequeue(self):
        assert not self.is_empty(), "cannot dequeue from empty queue"
        return self.queue_items.pop(0)
    
    def size(self):
        return len(self.queue_items)

class circularQueue:
    def __init__(self , max_size):

        self.count = 0
        self.front = 0
        self.back = max_size - 1
        self.circulararray = Array(max_size)
    
    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.circulararray)

    def __len__(self):
        return self.count

    def enqueue(self, item):
        max_size = len(self.circulararray)
        self.back = (self.back + 1) % max_size
        self.circulararray[self.back] = item
        self.count += 1
    
    def dequeue(self):
        item = self.circulararray[self.front]
        self.front += 1
        self.count -= 1
        return item


'''
cir_array = circularQueue(4)

for i in range(4):
    cir_array.enqueue(i*i)

for j in range(4):
    print(cir_array.dequeue())

cir_array.enqueue(5)
print(len(cir_array))'''




        
'''myQue = Queue()
print(myQue.is_empty())
myQue.enqueue(2)
myQue.enqueue(True)
myQue.enqueue("Name")
myQue.enqueue(1.03)
print("the size of queue is", myQue.size())
print(myQue.dequeue())
print("the size of queue is", myQue.size())
print(myQue.is_empty())
print(myQue.dequeue())
print(myQue.dequeue())
print(myQue.size())'''
