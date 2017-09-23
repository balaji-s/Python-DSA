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


    
print(bubble_sort(a_list))
print (selection_sort(a_list))
print(insertion_sort(a_list))


print(bubble_sort(b_list))
print (selection_sort(b_list))
print(insertion_sort(b_list))
