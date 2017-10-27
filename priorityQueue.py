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
        for i in self.pq_list:
            pqlist += ' ' + str(i.item) + '-' + str(i.priority) +'--'
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


pq = priorityQueue()
pq.enqueue("white",5)
pq.enqueue("blue", 4)
pq.enqueue("red",3)
pq.enqueue("yellow",6)
pq.enqueue("indigo",6)
pq.enqueue("green",5)
pq.enqueue("violet",6)
pq.enqueue("orange",6)


#print(pq)

for i in range(len(pq)):
    print(pq.dequeue())








