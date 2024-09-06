#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab08_2
# 229223 Sec 002

def main():
    test_reverse_digits()

def reverse_digits(x):
    x = int(x)    
    if x > 0:
        if x == 0:
            return x
        else:
            return (x % 10)*(10**(digit_count(x)-1)) + int(reverse_digits(x//10))
    else:
        x = abs(x)
        if x == 0:
            return x
        else:
            return -1*((x % 10)*(10**(digit_count(x)-1)) + int(reverse_digits(x//10)))
def digit_count(x):
    if x == 0:
        return x
    else:
        return 1 + digit_count(x//10)
def test_reverse_digits():
    assert reverse_digits(-1234) == -4321
    assert reverse_digits(1) == 1
    print("OK!")

if __name__ == '__main__':
    main()