#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab02_1
# 229223 Sec 002

def main():
    test_set_kth_digit()

def kth_digit(number, k):
    return (abs(number) // pow(10, k)) % 10

def set_kth_digit(number, k, value):
    digit_at_k = kth_digit(number, k)
    power_of_10 = pow(10, k)
    return number - digit_at_k * power_of_10 + value * power_of_10

def test_set_kth_digit():
    assert set_kth_digit(2343,2,7) == 2743
    assert set_kth_digit(51,0,2) == 52
    assert set_kth_digit(1,2,5) == 501
    print("All OK!")


if __name__ == '__main__':
    main()