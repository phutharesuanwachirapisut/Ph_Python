#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW12_1
# 229223 Sec 002

import math
def main():
    assert nth_term(1) == 6
    assert nth_term(4) == 67
    assert nth_term(16) == 6667
    assert nth_term(1000) == 777767667
    print('OK')

# 6, 7, 66, 67, 76, 77, 666, 667, 676, 677, 766, 767, 776, 777, 6666, 6667, 6676, 6677, 6766, 6767, 6776, 6777, ...

def nth_term(n):
    dict_ = {1:6, 0:7}
    dict_d = {}
    if n == 1 or n == 2:
        if n == 2:
            n == 0
        return dict_[n]
        
    digits = math.floor(math.log2(n)) + 1 # จำนวนหลักของ output
    b = (2 ** digits) - n
    for i in range(2 ** digits):
        dict_d = {}
        dict_d[i] = "6" * i
         

if __name__ == '__main__':
    main()