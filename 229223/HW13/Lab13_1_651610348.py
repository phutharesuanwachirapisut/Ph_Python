#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab13_1
# 229223 Sec 002
import copy
def main():
    assert matrix_mult([[1, 2, 3], 
                        [4, 5, 6]] ,
 [[7, 8], 
 [9, 10], 
 [11,12]]) == [[58, 64], 
 [139, 154]]
    assert matrix_mult([[1, 2, 3], 
 [4, 5, 6]] ,
[[7, 8, 5, 9, 3], 
 [9, 10, -3, 7, 13], 
 [11, 12, 6, 2, 9]]) == [[58, 64, 17, 29, 56],  
 [139, 154, 41, 83, 131]]
    assert matrix_mult([[1, 2, 3],[1, 2, 4],[1, 2, 5]], [[1, 2],[1, 3]]) == None

    print('OK')

def matrix_mult(m1, m2):
    m_1 = copy.deepcopy(m1)
    m_2 = copy.deepcopy(m2)
    len_row_4_m1 = len(m_1)
    len_row_4_m2 = len(m_2)
    len_col_4_m1 = len(m_1[0])
    len_col_4_m2 = len(m_2[0])
    # สร้าง zero matrix
    matrix_result = make_2d_list(len_row_4_m1, len_col_4_m2)

    for i in range(0,len_row_4_m1): # แทนค่าใน zero matrix
        re = 0
        if len_row_4_m2 == len_col_4_m1:
            for j in range(0,len_col_4_m2): 
                re = 0
                for k in range(0,len_row_4_m2):
                    re += m_1[i][k] * m_2[k][j]
                matrix_result[i][j] = re
        else:
            return None
    return matrix_result 
    
def make_2d_list(rows, cols):
    a = []
    for row in range(rows):
        a += [[0] * cols]
    return a

if __name__ == '__main__':
    main()