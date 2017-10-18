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
            