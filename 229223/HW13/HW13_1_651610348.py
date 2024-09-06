#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW13_1
# 229223 Sec 002

def main():
    assert square_matrix([[2, 3, 4], 
                          [1, 2, 3]]) == [[2, 3, 4], 
                                          [1, 2, 3], 
                                          [0, 0, 0]]
    assert square_matrix([[1, 2], 
                          [1, 2, 3], 
                          [1, 2], 
                          [1, 2], 
                          [1]]) == [[1, 2, 0, 0, 0], 
                                    [1, 2, 3, 0, 0], 
                                    [1, 2, 0, 0, 0], 
                                    [1, 2, 0, 0, 0], 
                                    [1, 0, 0, 0, 0]]
    assert square_matrix([[1, 2],
                          [3]]) == [[1, 2],
                                    [3, 0]]
    print('OK')
    
import copy

def square_matrix(list_x):
    list_a = copy.deepcopy(list_x)
    
    max_cols = max(len(row) for row in list_a)
    
    size = max(len(list_a), max_cols)
    
    for row in list_a:
        row.extend([0] * (size - len(row)))
    while len(list_a) < size:
        list_a.append([0] * size)
    list_x[:] = list_a

# def square_matrix(list_x):
#     list_a = copy.deepcopy(list_x)
#     n = len(list_a)
#     max_len = max(len(row) for row in list_a)
#     new_len = max(n, max_len)

#     for i in range(n):
#         while len(list_a[i]) < new_len:
#             list_a[i].append(0)
    
#     while len(list_a) < new_len:
#         list_a.append([0] * new_len)
#     return list_a


if __name__ == '__main__':
    main()