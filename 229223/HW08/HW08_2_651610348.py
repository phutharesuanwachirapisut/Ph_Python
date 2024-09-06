#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW08_2
# 229223 Sec 002

def main():
    print(base_b(44,2))

def base_b(x, b):
    if b > x:
        return x
    else:
        result = str(base_b(x//b,b)) + str(x % b)
        return  int(result)

# def test_base_b():
#     assert base_b(8, 2) == 1000
#     assert base_b(11, 3) == 102
#     print("All OK!")


if __name__ == '__main__':
    main()
