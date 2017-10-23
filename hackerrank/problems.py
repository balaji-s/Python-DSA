'''n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)'''
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
b =[[1,2,3],[4,5,6],[7,8,9]]
print(sod(b, 3))









'''
0,0 0,1 0,2 0,3 0,4
1,0 1,1 1,2 1,3 1,4
2,0 2,1 2,2 2,3 2,4
3,0 3,1 3,2 3,3 3,4
4,0 4,1 4,2 4,3 4,4'''    