#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW09_1
# 229223 Sec 002

def main():
    life_path(1234)
def life_path(n):
    if n < 10:
        return n
    n = list(str(n))
    n = list(map(int, n))
    n = sum(n)
    return life_path(n)
if __name__ == '__main__':
    main()