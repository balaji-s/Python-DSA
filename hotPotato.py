from Queue import Queue
from deque import deque

def hotPotato(name_list, num):
    queue = Queue()
    for name in name_list:
        queue.enqueue(name)
    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue() 





def revString(string,rString):
   
    if string =='':
        return rString
    else:
        
        return revString(string[:-1],rString+string[-1:])


def string_rev(string):
    if string == '':
        return ""
    else:
        #print(string[:-1], string[-1:])
        return  string[-1:] + string_rev(string[:-1]) 


def sumList(mylist):

    if(len(mylist) == 1):
        return mylist[0]
    else:
        print('a')
        return mylist[-1] + sumList(mylist[:-1])


def reverseString(string):
    return sumList(list(string))

def factorial(number):
    if number == 1:
        return 1
    else:
        #print(number)
        return  factorial(number-1) * number



def to_Str(number, base):
    const = "0123456789ABCDEF"

    if number < base:
        return const[number]
    else:
        a = const[number % base]
        print(a)
        return to_Str(number//base, base) + a




def palindromeLower(string):
    return palindrome(string.replace('\'','').replace('.','').replace(',','').replace(';','').replace(' ','').lower())
def palindrome(string):
    if len(string) == 1 or len(string) == 0:
        return True
    elif string[0] == string[-1:]:
        print(string[1:][:-1])
        return palindrome(string[1:][:-1])
    else:
        return False
def palindromeQueue(string):
    mydeck = deque()

    for ch in string:
        mydeck.add_front(ch)
    success = False
    while mydeck.size() > 1 :
        if mydeck.remove_front() == mydeck.remove_rear():
            success = True
            continue
        else:
            success = False
            break;

    return success
    



def recursiveList(myList):
    if len(myList) == 0:
        return myList
    else:
        return [myList[-1]] + recursiveList(myList[:-1])
def count_list(mylist):
    if len(mylist) == 0:
        return 0
    else:
        return 1 + count_list(mylist[:-1])

def max_element_rec(mylist, max):
    if len(mylist) == 1:
        return max
    else:
        if max < mylist[1]:
            max = mylist[1]
        return max_element_rec(mylist[1:], max)
        

k_list = [1,2,3]
print('number of items in a list:', count_list(range(1,10)))
'''
print(string_rev('birni'))
print(string_rev("kayaak"))
print("hotpotato",hotPotato(['brad','tom','bill','bush','barney'],7))
print(to_Str(17, 16))
print(to_Str(10,2))
print(palindromeLower('Go hang a salami; I\'m a lasagna hog.'))
print(recursiveList([2,1,4,7,-2,456,45]))'''
    
'''print(palindromeQueue("kayaka"))
print(palindromeQueue("madam"))'''
print(factorial(5))
print(string_rev('balaji'))
def printRev(n):
    if n > 0:
        printRev(n-1)
        print(n)

#printRev(4)
my_list = [123452,123453,5643,4,7,-2,456234,45,78, 34,1000,123544];
print(max_element_rec(my_list,my_list[0]))
