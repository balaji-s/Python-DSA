import ctypes
class Array:

    def __init__(self, size):
        self._size = size
        array = ctypes.py_object * size
        self.elements = array()
        self.clear(None)
    
    def clear(self, item):
        for i in range(len(self)):
            self.elements[i] = item

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value
    
    def __iter__(self):
        return _ArrayIterator(self.elements)


class _ArrayIterator:

    def __init__(self, yArray):
        self.py_array = yArray
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.py_array):
            item = self.py_array[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration





myArray = Array(10)



'''for i in range(10):
    myArray[i] = i

for j in myArray:
    print(myArray[j])'''