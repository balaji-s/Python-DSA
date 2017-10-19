class _priority:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next_node = None

class priority_queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    def __len__(self):
        return self.size

    def enqueue(self, item, priority):
        pQueue = _priority(item, priority)
        if self.head is None:
            self.head = pQueue
        else:
            current = self.head
            stop = False
            previous = None
            while current is not None and not stop:
                if item > current.data and < current.next_node.data:
                    stop = True
                elif item == current.data:
                    stop = True
                else:
                    previous = current
                    current = current.next_node
                
            self.tail.next = pQueue
        self.tail = pQueue
        self.size += 1

class binaryheap:

    def __init__(self):
        self.heap_list = [0]
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty():
        return self.size == 0

    
    def insert(self, item):
