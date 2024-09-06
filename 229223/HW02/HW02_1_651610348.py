#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab02_1
# 229223 Sec 002

# x=float(input("x: "))
# octagon_area = octagon_area(x)
# print(octagon_area)

import math

def main():
    test_octagon_area()

def octagon_area(x):
    octagon_area = 4*(1/2)*((abs(x)/3)**2)+(5*(abs(x)/3)**2)
    return octagon_area

def test_octagon_area():
    assert octagon_area(0) == 0
    assert octagon_area(12) == 112
    print("All OK!")


if __name__ == '__main__':
    main()

