count = 0
def mergesort(array_elements):
    global count 
    if len(array_elements) > 1:
        midpoint = len(array_elements)//2
        left_half = array_elements[:midpoint]
        right_half = array_elements[midpoint:]

        #print(left_half)
        #print(right_half)
        mergesort(left_half)
        mergesort(right_half)
        i = 0
        j = 0
        k = 0
        #print("splitting over")
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array_elements[k] = left_half[i]
                print(left_half[i],right_half[j])
                i = i + 1
                count += 1
            else:
                array_elements[k] = right_half[j]
                count += 1
                j = j + 1
            k = k + 1
        while i < len(left_half):
            array_elements[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array_elements[k] = right_half[j]
            j += 1
            k += 1
    #print("another",array_elements)
   
    print(count)
    

#array = [19,5,3,1,45,34,21]
array = [5, 3, 1, 0, 2, 4]
mergesort(array)
print(array)