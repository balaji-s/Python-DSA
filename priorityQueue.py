from Array import Array
from LinkedQueuestack import linkedqueue
class priorityQueue:
    '''list based implementation of priority queues
    '''
    def __init__(self):
        self.pq_list = list()
    
    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.pq_list)

    def enqueue(self, item, priority):
        priority_storage = _prioritystorage(item, priority)
        self.pq_list.append(priority_storage)
    
    def __str__(self):
        pqlist =''
        for pq_elem in self.pq_list:
            pqlist += ' ' + str(pq_elem.item) + '-' + str(pq_elem.priority) +'--'
        return pqlist
            
    def dequeue(self):
        highest = self.pq_list[0].priority
        count = 0
        for pq_elem in range(len(self.pq_list)):
            if self.pq_list[pq_elem].priority < highest:
                highest = self.pq_list[pq_elem].priority
                count = pq_elem
        entry = self.pq_list.pop(count)
        return entry.item
        

class _prioritystorage:

    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

class queuePriority:

    def __init__(self, data, priority, node = None):
        self.data = data
        self.next_node = node
        self.priority = priority
    

class priorityQueue_linkedlist:

    '''
        priority queue linked list based implementation
    '''

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item , priority):
        ''' takes item , priority and enqueues it  '''
        node = queuePriority(item, priority)
        previous = None
        stop = False
        current = self.head
        while current is not None and not stop:
            if current.priority > priority:
                stop = True
            else:
                previous = current
                current = current.next_node
        
        if previous is None:
            node.next_node = self.head
            self.head = node
        else:
            node.next_node = current
            previous.next_node = node
        self.size += 1
    
    def __iter__(self):
        return _llIterator(self.head)

    def dequeue(self):
        ''' removes item of top priority'''
        current = self.head
        self.head = current.next_node
        self.size -= 1
        return current.data


class _llIterator:

    def __init__(self, llist):
        self.llist = llist
    
    def __next__(self):
        if self.llist.next_node is None:
            raise StopIteration
        else:
            item = self.llist.data
            self.llist = self.llist.next_node
            return item

    def __iter__(self):
        return self
            

class boundedpriorityQueue:
    '''
    bounded priority queue implementation using Array class and queue class
    '''

    def __init__(self, levels):
        self.queue_levels = Array(levels)
        for num_level in range(levels):
            self.queue_levels[num_level] = linkedqueue()
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0


    def enqueue(self, item, priority):
        if priority >= 0 and priority < len(self.queue_levels):
            self.queue_levels[priority].enqueue(item)
            self.size += 1
    
    def dequeue(self):
        
        for q_elem in range(len(self)):
            if  not self.queue_levels[q_elem].is_empty():
                return self.queue_levels[q_elem].dequeue()




pq = boundedpriorityQueue(9)
pq.enqueue("nine", 9)
pq.enqueue("white",5)
pq.enqueue("blue",4)
pq.enqueue("red",3)
pq.enqueue("der",3)
pq.enqueue("one",0)
pq.enqueue("zero",0)
pq.enqueue("yellow",6)
pq.enqueue("indigo",6)
pq.enqueue("green",5)
pq.enqueue("two",2)
pq.enqueue("three", 3)
pq.enqueue("violet",6)
pq.enqueue("orange",6)


#print(pq)
print('size of priority queue is:', len(pq))
for i in range(len(pq)):
    print(pq.dequeue())








