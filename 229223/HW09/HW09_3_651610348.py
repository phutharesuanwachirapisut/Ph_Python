#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW09_3
# 229223 Sec 002

def main():
    assert left_max([3,14,3,82,3,0,1,6,490]) == [3,14,14,82,82,82,82,82,490]
    assert left_max([2, 8, 1]) == [2, 8, 8]
    assert left_max([3, 3, 1, 1, 2, 4]) == [3, 3, 3, 3, 3, 4]
    assert left_max([1]) == [1]
    assert left_max([2,1]) == [2,2]
    assert left_max([1,2,3,2,1]) == [1,2,3,3,3]
    print("ok")

def left_max(n):
    if len(n) == 1:
        return [n[0]]
    if n[0] >= n[1]:
        return [n[0]] + left_max([n[0]] + n[2:])
    else:
        return [n[0]] + left_max(n[1:])
    
if __name__ == '__main__':
    main()