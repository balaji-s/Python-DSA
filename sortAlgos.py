#class sortAlgos:

def bubble_sort(my_list):
  
  for i in range(len(my_list)):
    k =i+1
    for k in range(len(my_list)-1):
      if my_list[ k] > my_list[k+1]:
        my_list[k], my_list[k+1] =my_list[k+1] , my_list[k]

  return my_list

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(bubble_sort(a_list));