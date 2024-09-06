#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW12_3
# 229223 Sec 002

def main():
    assert subset_sum({1, 2, 3}) == [0, 1, 2, 3, 3, 4, 5, 6]
    print('OK')

def subset_sum(set_a):
    result = [[]]  # เริ่มต้นด้วยเซตว่าง
    for element in set_a:
        new_result = [subset + [element] for subset in result] # โคลน แล้วเพิ่มเรื่อย ๆ
        result.extend(new_result)
    return [sum(subset) for subset in result]

if __name__ == '__main__':
    main()