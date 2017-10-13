class Queue:

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


class circularQueue:
    def __init__(self , max_size):

        self.cQueue = list()
        self.count = 0
        self.front = 0
        self.back = max_size - 1
        
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
