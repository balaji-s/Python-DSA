import ctypes
class Array:

    def __init__(self, size):
        self.size = size
        self.array = ctypes.py_object * size
        self.elements = self.array ()
        self.clear(None)
    
    def clear(self, item):
        for i in range(len(self)):
            self.elements[i] = None

    def __len__(self):
        return self.size

    def get_item(self, index):
        return self.elements[index]

    def set_item(self, index, value):
        self.elements[index] = value
    
    def __iter__(self):
        return __ArrayIterator(self)


class __ArrayIterator:

    def __init__(self, yArray):
        self.pyArray = yArray
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.pyArray):
            item = self.pyArray[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


myArray = Array(10)

for i in range(10):
    myArray.set_item(i, i*i)

for j in range(len(myArray)):
    print(myArray.get_item(j))