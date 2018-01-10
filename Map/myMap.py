class mymap:
    
    def __init__(self):
        self.dict = []
    
    def __len__(self):
        return len(self.dict)

    def __iter__(self):
        return _mapIterator(self.dict)

    def add(self, key, value):
        keyPosition = self.find_key(key)
        if keyPosition is not None:
            self.dict[keyPosition].value = value
            return False
        else:
            map = mapStorage(key, value)
            print(key,value)
            self.dict.append(map)
            return True
    def value(self, key):
        keyPosition = self.find_key(key)
        if keyPosition is not None:
            return self.dict[keyPosition].value
        
    def remove(self, key):
        keyPosition = self.find_key(key)
        if key is not None:
            self.dict.remove(keyPosition)
    def find_key(self, key):
        for i in range(len(self.dict)):
            if key == self.dict[i].key:
                return i
        return None


class mapStorage:

    def __init__(self, key , value):
        self.key = key
        self.value = value

class _mapIterator:

    def __next__(self):
        if self.currentItem < len(self.uMap):
            dic = self.uMap[self.currentItem]
            self.currentItem += 1
            return (dic.key, dic.value)
        else:
            raise StopIteration
        
    def __iter__(self):
        return self
    def __init__(self, uMap):
        self.uMap = uMap
        self.currentItem = 0



mapper = mymap()
mapper.add("name","balaji")
mapper.add("age",32)
mapper.add("city","chennai")

print(mapper.value("name"))

for i in mapper:
    print(i)