#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW14_1
# 229223 Sec 002

# def main():
#     assert reshape([[2, 3, 4], 
#  [1, 2, 3]]) == [[2, 3, 4], 
#  [1, 2, 3]]
#     assert reshape([[1, 2], 
#  [1, 2, 3], 
#  [1, 2], 
#  [1, 2], 
#  [1]] ) == [[1, 2, 1, 2],  
#  [3, 1, 2, 1],  
#  [2, 1, 0, 0]]
#     assert reshape([[1, 2],  
#  [3, 4],  
#  [5, 6]]) == [[1, 2, 3],  
#  [4, 5, 6]] 
#     print('OK')
    
def main():
    filename = input("Input FileName: ")
    with open(filename, 'r') as file:
        lines = file.readlines()
    # filename = [line.strip('\n') for line in filename]
    filename = [line.split('\n') for line in filename]
    for line_index in range(0, len(filename), 3):
        list_a = filename[line_index]
        row = int(filename[line_index + 1])
        col = int(filename[line_index + 2])

        removed_list = remove_row_col(list_a, row, col)

        print(removed_list)

import copy
from functools import reduce

def reshape(matrix):
    matrix_ = copy.deepcopy(matrix)
    rows = len(matrix_)
    cols = max(len(row) for row in matrix_)  # ใช้ generator expression แทนการ loop เพื่อหาค่า cols ที่มากที่สุด
    flattened_matrix = reduce(lambda x, y: x + y, matrix_)
    
    # หาขนาดใหม่ของเมทริกซ์
    m = min(rows, cols)
    m_ = m
    n = max(rows, cols)
    n_ = n
    if not abs(n - m) <= 1:
        while not abs(n - m) <= 1: 
            n -= 1    
        zero_matrix_1 = [[0 for _ in range(n)] for _ in range(m)]
        ze_1 = reduce(lambda x, y: x + y, zero_matrix_1)
        while not abs(n_ - m_) <= 1:    
            m_ += 1
        zero_matrix_2 = [[0 for _ in range(m_)] for _ in range(n_)]
        ze_2 = reduce(lambda x, y: x + y, zero_matrix_2)

        if ze_1.count(0) < ze_2.count(0):
            zero_matrix = zero_matrix_1 
        else:
            zero_matrix = zero_matrix_2
    else:
        zero_matrix = make_2d_list(m, n)
    
    for i in range(m):
        for j in range(n):
            if i * n + j < len(flattened_matrix):
                zero_matrix[i][j] = flattened_matrix[i * n + j]
    
    matrix[:] = zero_matrix

def make_2d_list(rows, cols): # สร้าง zero matrix
    a = []
    for row in range(rows):
        a.append([0] * cols)
    return a
if __name__ == '__main__':
    main()