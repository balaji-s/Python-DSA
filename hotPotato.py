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
        return string
    else:
        print(string[:-1], string[-1:])
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
        return number
    else:
        print(number)
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
'''print(string_rev('balaji'))
print(string_rev('birni'))
print(string_rev("kayaak"))
print(factorial(5))
print("hotpotato",hotPotato(['brad','tom','bill','bush','barney'],7))
print(to_Str(17, 16))
print(to_Str(10,2))
print(palindromeLower('Go hang a salami; I\'m a lasagna hog.'))
print(recursiveList([2,1,4,7,-2,456,45]))'''
    
print(palindromeQueue("kayaka"))
print(palindromeQueue("madam"))