#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW13_2
# 229223 Sec 002

def main():
    list_x = [3, 7, 4, 9, 5, 2, 6] 
    bottom_up_m_sort(list_x, True) 
    print('--------') 
    print(list_x)

    print('-------------------------') 

    list_x = [3, 7, 4, 9, 5, 2, 6, 1] 
    bottom_up_m_sort(list_x) 
    print('--------') 
    print(list_x)
 
import copy
def bottom_up_m_sort(list_x, show_step=False):
    list_a = copy.deepcopy(list_x)
    list_a = list(map(lambda x: [x],list_a))
    if show_step == True:
        print(list_a)
    rows = len(list_a) # assert แรก -> 7
    while rows != 1:
        a = 0
        for row in range(0,rows,2):
            if row != rows and rows - row != 1:
                if list_a[row] < list_a[row + 1]:
                    list_a[a] = list_a[row] + list_a[row+1] 
                else:
                    list_a[a] = list_a[row+1] + list_a[row] 
            else:
                list_a[a] = list_a[row]
            a += 1
        list_a = list_a[:a]
        list_a = sausage(list_a)
        if show_step == True:
            print(list_a)
        rows = len(list_a)        
    list_x[:] = sum(list_a, [])
    
def sausage(list_a):
    for k in list_a:
        n = len(k)
        for i in range(n):
            for j in range(0, n-i-1):
                if k[j] > k[j+1]:
                    k[j], k[j+1] = k[j+1], k[j]
    return list_a


if __name__ == '__main__':
    main()