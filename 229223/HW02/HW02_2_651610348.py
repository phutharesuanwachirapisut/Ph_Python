#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab02_1
# 229223 Sec 002

import math

def main():
    test_kth_digit()

def kth_digit(number, k):
    return (abs(number) // pow(10, k)) % 10

def test_kth_digit():
    assert kth_digit(789,0) == 9
    assert kth_digit(789,1) == 8
    assert kth_digit(789,2) == 7
    assert kth_digit(789,3) == 0
    print("All OK!")


if __name__ == '__main__':
    main()

