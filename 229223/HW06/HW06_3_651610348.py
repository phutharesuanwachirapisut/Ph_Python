#!/usr/bin/env python3
# Phutharesuan_Wachirapisut
# 651610348
# HW06_3
# 229223 Sec 002

def main():
    test_moving_average()

def moving_average(list_a, w):
    moving_average = list(map(lambda i: (sum(list_a[i:i+w]) / w) if i + w <= len(list_a) else None, range(len(list_a) - w + 1)))
    return moving_average

def test_moving_average():
    assert moving_average([1, 2, 3, 4, 5],3) == [2.0, 3.0, 4.0]
    print("OK!")

if __name__ == '__main__':
    main()
