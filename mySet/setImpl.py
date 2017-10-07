class mySet:
    def __init__(self):
        self.uniqueItems = list()
        self.currentItem = 0
    
    def add(self, item):
        if item not in self.uniqueItems:
            self.uniqueItems.append(item)
    
    def __len__(self):
        return len(self.uniqueItems)

    def __contains__(self, item):
        return item in self.uniqueItems

    def remove(self, item):
        self.uniqueItems.remove(item)
    
    def isSubsetOf(self, setB):
        for element in self.uniqueItems:
            if element not in setB:
                return False
            else:
                return True
    
    def Union(self, setB):
        uSet = mySet()
        uSet.uniqueItems.extend(self.uniqueItems)
        for element  in setB:
            uSet.add(element)
        return uSet
    def __iter__(self):
        return _SetIterator(self.uniqueItems)

    def intersection(self, setB):
        iSet = mySet()
        for element in self.uniqueItems:
            if element in setB:
                iSet.add(element)
        return iSet

    def difference(self,setB):
        iSet = mySet()
        for element in self.uniqueItems:
            iSet.add(element)
        for el in setB:
            iSet.add(el)
        return iSet
class _SetIterator:
    def __init__(self,theList):
        self.uniqueItems = theList
        self.currentItem = 0

    def __next__(self):
        item = 0
        if self.currentItem < len(self.uniqueItems):
            item = self.uniqueItems[self.currentItem]
            self.currentItem += 1
            return item
        else:
            raise StopIteration
        
    def __iter__(self):
        return self
sett = mySet()
for i in range(0, 7):
    sett.add(i)
setA = mySet()
for j in range(6,10):
    setA.add(j)

for i in sett:
    print(i)
print('----------------')
for j in setA:
    print(j)
setU = sett.Union(setA)
print('----------------')
for ele in setU:
    print(ele)
print('---------------------')
setI  = sett.intersection(setA)
for jj in setI:
    print(jj)
print('----------------')
setD = sett.difference(setA)
for kk in setD:
    print(kk)
