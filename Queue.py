class Queue:

    def __init__(self):
        self.queue_items = []
    
    def is_empty(self):
        return self.queue_items == []

    def enqueue(self,item):
        self.queue_items.insert(0,item)
    
    def dequeue(self):
        return self.queue_items.pop()
    
    def size(self):
        return len(self.queue_items)



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
