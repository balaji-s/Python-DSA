def searching(myList, item):
    position = 0
    found = False
    while position < len(myList) and not found:
        if myList[position] == item:
            found = True
        else:
            position += 1

    return found
print(searching([2,4,54,34,1,-4,-1,0,343],-4))