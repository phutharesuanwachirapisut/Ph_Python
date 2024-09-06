#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab14_2
# 229223 Sec 002

def main():
    assert remove_row_col([[2, 3, 4, 5],  
                           [8, 7, 6, 5],  
                           [0, 1, 2, 3]], 1, 2) == [[2, 3, 5],  
                                                    [0, 1, 3]]
    assert remove_row_col([[2, 3, 4, 5],  
                           [8, 7, 6, 5],  
                           [0, 1, 2, 3]], 1, -3) == [[2, 4, 5],  
                                                     [0, 2, 3]]
    print('OK')

import copy 

def remove_row_col(list_a, row, col):
    list_x = copy.deepcopy(list_a)
    # ลบ row 
    if row <= len(list_a):
        list_x = list_x[:row] + list_x[row + 1:]
    else:
        return list_x
    for i in list_x: # ลบ col
        if col <= len(i):
            list_x[list_x.index(i)] = i[:col] + i[col + 1:]
        else:
            return list_x
    return list_x

if __name__ == "__main__":
    main()
