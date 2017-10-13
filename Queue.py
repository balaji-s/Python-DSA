from Array import Array


class Queue:

    def __init__(self):
        self.queue_items = []
    
    def is_empty(self):
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
        self.array = ;Array(max_size)
    
    def is_empty(self):
        return self.array.size == 0

    def is_full (self):
        return self.count == len(self.array)
    def __len__(self):
        return self.count

    def enqueue(self, item):
        if !array.is_full():
            self.array.



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
