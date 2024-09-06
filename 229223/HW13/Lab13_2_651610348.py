#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab13_2
# 229223 Sec 002

def main():
    assert is_magic_square([[2, 7, 6], 
 [9, 5, 1], 
 [4, 3, 8]]) == True
    assert is_magic_square([[5, 5, 5], 
 [5, 5, 5], 
 [5, 5, 5]]) == False
    assert is_magic_square([[7, 12, 1, 14], 
 [2, 13, 8, 11], 
 [16, 3, 10, 5], 
 [9, 6, 15, 4]]) == True
    assert is_magic_square([[1,2,3], 
 [4,5,6], 
 [7,8,9], 
 [10,11,12]]) == False
    assert is_magic_square([ [1,2,3,4]
    , [5,6,7,8]
    , [9,10,11,12]
    , [13,14,15,16]
    ]) == False
    assert is_magic_square([ [8,11,14,1]
    , [13,2,7,12]
    , [3,16,9,6]
    , [10,5,4,15]
    ]) == True
    print('OK')

import copy
from functools import reduce

def is_magic_square(board):
    board_ = copy.deepcopy(board)
    n = len(board_)
    result = (n * (n**2 + 1)) // 2
    
    for z in range(n):
        if not len(board_[z]) == n or n < 3: # non-square
            return False
    board_test = reduce(lambda x, y: x + y, board_) # ทำให้เป็น Matrix 1xN
    for i in board_test: # หาตัวซ้ำ
        if board_test.count(i) > 1:
            return False
    
    g = 0
    sum_lr = 0
    sum_rl = 0

    while g < n:
        sum_lr += board_[g][g]
        sum_rl += board_[g][n-g-1]
        g += 1
    if not sum_lr == sum_rl == result:
        return False
        
    i = 0
    j = 0
    for i in board_:
        if sum(i) != sum(board_[0]):
            return False
    cols = [[j[c] for j in board_] for c in range(len(board_[0]))]
    for c in cols:
        if sum(c) != sum(board_[0]):
            return False
    if not sum_lr == sum_rl == sum(c) == sum(i) == result:
        return False
    else:
        return True
    # while i < n:
    #     sum_row = 0
    #     sum_col = 0
    #     j = 0
    #     while j < n:
    #         sum_row += board_[i][j]
    #         sum_col += board_[j][i]
    #         j += 1
    #     if not sum_row == sum_col:
    #         return False
    #     else:
    #         i += 1

    # c = 0
    # d = 0
    # for i in range(len(board_)):
    #     c += board_[i][i] # แนว ทะแยงจากซ้ายไปขวา
    #     d += board_[i][len(board_)-i-1]  # แนว ทะแยงจากขวาไปซ้าย
        
    # if c != result or d != result:
    #     return False
        
    # for i in range(len(board_)): # ผลบวกในแนว column
    #     a = 0
    #     b = 0
    #     for j in range(len(board_)):
    #         a += board_[i][j] # แนว row
    #         b += board_[j][i] # แนว column

    #     if a != result or b != result:
    #         return False
    # return True 
if __name__ == '__main__':
    main()