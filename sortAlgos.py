import random

kk = list(range(234,2300,5))
random.shuffle(kk)
a_list = [54, 26, 93, 17, -1, 77, 31, 44, -2, 55, 20]
b_list = [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]

def bubble_sort(my_list):
  
  for i in range(len(my_list)):
    k = i+1
    for k in range(len(my_list)-1):
      if my_list[ k] > my_list[k+1]:
        my_list[k], my_list[k+1] = my_list[k+1] , my_list[k]

  return my_list

def selection_sort(my_list):
  temp = 0
  for i in range(len(my_list)):
    minimum = i
    j = i
    for j in range(len(my_list)-1):
      if my_list[minimum] < my_list[j] :
        minimum = j

        temp = my_list[i]
        my_list[i] = my_list[j]
        my_list[j] = temp

  
  return my_list


def insertion_sort(my_list):
  
  for i in range(len(my_list)):
    temp = my_list[0]
    j = i
    for j in range(i):
      if my_list[i] < my_list[j]:
        temp = my_list[i]
        my_list[i] = my_list[j]
        my_list[j]= temp
    
  return my_list

def shell_sort(my_list):
  gaps = len(my_list) //2
  while(gaps > 0):
    for i in range(len(my_list)):
      j =0
      while(j < len(my_list)):
        if j + gaps < len(my_list) and my_list[j] > my_list[j+gaps]:
          my_list[j],my_list[j+gaps] = my_list[j+gaps], my_list[j]
        
        j += gaps
    gaps = gaps // 2
  return my_list
 
 
 

  
    
'''print(bubble_sort(a_list))
print (selection_sort(a_list))
print(insertion_sort(a_list))


print(bubble_sort(b_list))
print (selection_sort(b_list))
print(insertion_sort(b_list))'''



'''print(bubble_sort(kk))
print(selection_sort(kk))
print(insertion_sort(kk))
print(shell_sort(kk))
print(shell_sort([5,4,3]))
kc = list(range(2,45,2))
random.shuffle(kc)
print(kc)
print(shell_sort(kc))'''

def quick_sort(any_list):
  if len(any_list) < 2:
    return any_list
  else:
    mp = len(any_list) // 2
    pivot = any_list.pop(mp)
    gt_pivot = [i for i in any_list if i <= pivot]
    lt_pivot = [i for i in any_list if i > pivot]
    return quick_sort(gt_pivot) + [pivot] + quick_sort(lt_pivot)

    

print(a_list)
print(quick_sort(a_list))

