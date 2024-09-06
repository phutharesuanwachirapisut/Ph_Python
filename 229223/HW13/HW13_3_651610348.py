#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW13_3
# 229223 Sec 002

def main():
    assert sum_d_product([[3, 3, 3, 2], 
                          [2, 0, 3, 1], 
                          [2, 1, 2, 3], 
                          [1, 0, 2, -1]]) == 33
    assert sum_d_product([[1, 1, 5, -1], 
                          [12, 2, -2, 0], 
                          [4, 8, 8, 12], 
                          [4, 12, 12, 15]]) == 3856
    assert sum_d_product([[0, -1, -1, 3, 2, 3, -1, 3], 
                          [3, -1, -1, 2, 0, -1, 2, 1], 
                          [3, 0, 1, 2, 3, 1, 3, 1], 
                          [2, 2, 1, -1, -1, 2, 0, 3], 
                          [1, 3, 2, 1, 3, 2, 2, 1], 
                          [1, 2, 2, 1, 3, 3, 1, 3], 
                          [2, 2, 2, 2, 2, 2, 3, 3], 
                          [1, 3, 2, 3, 1, 1, 2, 2]]) == -6290
    print('OK')
import copy
import math
def sum_d_product(m):
    list_a = []
    m_ = copy.deepcopy(m)
    n = len(m_) # จำนวน row ทั้งหมด
    while n != 1:
        for row in range(0,n,2):
            for col in range(0,len(m_[row]),2):
                c = m_[row][col] * m_[row+1][col+1] + m_[row][col+1] * m_[row+1][col]
                list_a.append(c)
        h = math.ceil(len(list_a)**0.5)
        m_ = []
        for i in range(0,len(list_a),h):

            m_ += [list_a[i:i + h]]
        list_a = []
        n = len(m_)
    m_ = sum(m_,[])
    return m_[0]

if __name__ == '__main__':
    main()