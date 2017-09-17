a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

def bubble_sort(my_list):
  
  for i in range(len(my_list)):
    k = i+1
    for k in range(len(my_list)-1):
      if my_list[ k] > my_list[k+1]:
        my_list[k], my_list[k+1] = my_list[k+1] , my_list[k]
      print(my_list)

  return my_list

def selection_sort(my_list):
  max = 0
  position = len(my_list) -1
  i = 0
  for i in range(len(my_list) - i):
      if max < i:
        max = i
        i += 1
      my_list[position] = max
      max = 0
      position -=1
      return my_list


    


print(selection_sort(a_list))
