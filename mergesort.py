def mergesort(array_elements):
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
        #print(left_half)
        #print(right_half)
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array_elements[k] = left_half[i]
                i = i + 1
            else:
                array_elements[k] = right_half[j]
                j = j + 1
            k = k + 1
        print("there u go",left_half)
        while i < len(left_half):
            array_elements[k] = left_half[i]
            i += 1
            k += 1
        print("after one while", left_half)
        print("there we go ",right_half)
        while j < len(right_half):
            array_elements[k] = right_half[j]
            j += 1
            k += 1
    print("another",array_elements)

    

array = [7,8,2,1,5,3,99,45,34,21]
mergesort(array)
print(array)