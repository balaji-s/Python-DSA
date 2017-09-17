def binary_search(myList,number):
    midpoint = len(myList)//2 # length is 5
    print(myList[midpoint])
    if midpoint == number:
        print('found your number: ', number)
   
    if len(myList) == 1:
        if myList[0]==number:
            print("found")
        return;
    if myList[midpoint] < number:
         print("first",myList[midpoint:len(myList)])
         binary_search(myList[midpoint:len(myList)],number)

    elif myList[midpoint] > number:
         print("second",myList[0:midpoint])
         binary_search(myList[0:midpoint],number)
    


binary_search([1,3,5,7,9], 15)
