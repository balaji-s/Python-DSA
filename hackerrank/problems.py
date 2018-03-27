'''n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)'''
from decimal import Decimal
def sod(list_list,n):
    left_diagonal = 0
    right_diagonal = 0
    for count, my_list in enumerate(list_list):
        for num, list_elem in enumerate(my_list):
            if num == count:
                print('in num== count', count, num, list_elem)
                left_diagonal += list_elem
            elif num + count == n - 1:
                print(count, num, list_elem)
                right_diagonal += list_elem
            if(n % 2 == 1 and num == count and num + count == n-1):
                right_diagonal += list_elem

    return left_diagonal - right_diagonal
#a =[[1,2,3,4],[4,5,6,7],[7,8,9,10],[11,12,13,14]]
#sod(a,2)

#print(sod(a, 4))
'''b =[[1,2,3],[4,5,6],[7,8,9]]
print(sod(b, 3))'''

def pnz(array, array_len):
    positive = 0
    negative = 0
    zero = 0
    for i in array:
        if i > 0:
            positive

def pnz(array, array_length):
    positive = 0
    negative = 0
    zero = 0

'''def printhash(symbol,num):
    
    count = 1
    for i in range(7,0,-1):
        print(' '* i+symbol*count)
        count += 1
    for i in array:
        if i > 0:
            positive += 1
        elif i < 0 :
            negative += 1
        else:
            zero +=1
    return(Decimal(round(positive/array_length, 5)),round(negative/array_length, 6),round(zero/array_length, 6))
'''
#k = pnz([-4, 3, -9, 0 , 4, 1],6)
#print(k)


#printhash('#',6)
def staircase(num_stairs):
    for stairs in range(1, num_stairs + 1):
        print (' ' * (num_stairs - stairs) + '#' * stairs)

#staircase(6)

def timeconversion(s):
    
    if s.endswith('AM'):
        return s[:-2]
    else:
        k = s[:-2]
        m = int(k[:2]) + 11
        if(m == 12):
            return s[:-2]
        else:
            return str(m)+k[2:]


print(timeconversion('12:45:54PM'))

def timeconversion(time_string):

    k ="name"
    #
    if time_string.endswith("AM") and time_string.startswith('12'):
        hour = int(time_string[:2]) - 12
        return '00' + time_string[2:][:-2]
    elif time_string.endswith("PM") and time_string.startswith('12'):
        return time_string[:-2]
    else:
        hour = int(time_string[:2]) + 12
        return str(hour) + time_string[2:]

print(timeconversion('12:05:39AM'))
def solve(grades):
    gr_li= list()
    for grade in grades:
        if grade > 36:
            if(grade % 5 == 0):
                gr_li.append(grade)
                print('div by zero', grade)
            elif(grade % 5 <= 4):
                rem = grade % 5
                part = 5 - rem
                if(part <= 2):
                    #print(grade+part)
                    print("part less than 2",grade, grade+part)
                    gr_li.append(grade+part)
                else:
                    print('part greater than 3',grade)
                    gr_li.append(grade)
        else:
            gr_li.append(grade)
    #print(gr_li)
    return gr_li
j = [41,42,43,44,45,46,47,48,49,50]
k = solve(j)
print(k)



'''
0,0 0,1 0,2 0,3 0,4
1,0 1,1 1,2 1,3 1,4
2,0 2,1 2,2 2,3 2,4
3,0 3,1 3,2 3,3 3,4
4,0 4,1 4,2 4,3 4,4'''    

class Node:

    def __init__(self, data = None, node = None):
        self.data = data
        self.next_node = node

class linkedList :
    def __init__(self):
        self.head = None
    
    def add_last(head, data):
        node = Node(data)
        if head is None:
            node.next_node(head)
            head = node
            return head
        else:
            temp = head
            while (temp.next_node is not None):
                temp = temp.next_node
            temp.next_node = node
            head = node
            return head

ll = linkedList()

'''for i in range(3):
    ll.add_last(i)'''


def sockMerchant(n, ar):
    socks = dict()
    for element in ar:
        if element in  socks:
            socks[element] += 1
        else:
            socks[element] =1
    sum = 0
    for value in socks.values():
        sum = sum + value // 2

    return sum
a = 2
dd = [10, 20, 20, 10 ,10, 30,50, 10, 20]
print(sockMerchant(a, dd))
