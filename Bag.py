class Bag:
    
    def __init__(self):
        self.items = list()
        self.currentItem = 0
    
    def add(self, item):
        self.items.append(item)
    
    def is_empty(self):
        self.items == []
    
    def contains(self, item):
        return item in self.items

    def length(self):
        return len(self.items)

    def remove(self, item):
        self.items.remove(item)
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.currentItem < len(self.items):
            item = self.items[self.currentItem]
            self.currentItem += 1
            return item
        else:
            raise StopIteration

bag = Bag()

for i in range(10):
     bag.add(i)

for j in bag:
      print(j)
