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


def pnz(array, array_length):
    positive = 0
    negative = 0
    zero = 0

    for i in array:
        if i > 0:
            positive += 1
        elif i < 0 :
            negative += 1
        else:
            zero +=1
    return(Decimal(round(positive/array_length, 5)),round(negative/array_length, 6),round(zero/array_length, 6))

k = pnz([-4, 3, -9, 0 , 4, 1],6)
print(k)




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