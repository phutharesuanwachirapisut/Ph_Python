#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab08_1
# 229223 Sec 002

def main():
    print(gcd(100,2))

def gcd(x,y):
    x = abs(int(x))
    y = abs(int(y))
    if  x % y == 0:
        return y
    else:
        return gcd(y , x % y)

if __name__ == '__main__':
    main()