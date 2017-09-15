from Queue import Queue

def hotPotato(name_list, num):
    queue = Queue()
    for name in name_list:
        queue.enqueue(name)
    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue() 

#print(hotPotato(['brad','tom','bill','bush','barney'],7))



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

'''print(string_rev('balaji'))
print(string_rev('birni'))
print(string_rev("kayaak"))'''
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
        return number * factorial(number-1)
#print(factorial(5))


def to_Str(number, base):
    const = "0123456789ABCDEF"

    if number < base:
        return const[number]
    else:
        a = const[number % base]
        print(a)
        return to_Str(number//base, base) + a


#print(to_Str(17, 16))
#print(to_Str(10,2))

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


print(palindromeLower('Go hang a salami; I\'m a lasagna hog.'))
    