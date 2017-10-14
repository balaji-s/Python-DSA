from Array import Array, _ArrayIterator

class Array2D:

    def __init__(self, nrows, ncolumns):
        self._rows = Array(nrows)
        self.row_length, self.column_length = nrows, ncolumns
        for i in range(nrows):
            self._rows[i] = Array(ncolumns)

    def numRows(self):
        return self.row_length

    def numColumns(self):
        return self.column_length

    def clear(self, value):
        for i in range(self.numRows()):
            self._rows.clear(value)

    def __getitem__(self, ntuples):
        row = ntuples[0]
        column = ntuples[1]
        the_array = self._rows[row]
        return the_array[column]

    def __setitem__(self, ntuples, value):
        row = ntuples[0]
        column = ntuples[1]
        the_array = self._rows[row]
        the_array[column] = value
    
array2d = Array2D(2,3)
#print(array2d.row_length, array2d.column_length)

'''for i in range(array2d.row_length):
    for j in range(array2d.column_length):
        array2d[i,j] = i*i + j *j

for i in range(array2d.row_length):
    for j in range(array2d.column_length):
        print(array2d[i,j])'''
print(array2d.numRows(), array2d.numColumns())