#!/usr/bin/env python3
# Phutharesuan Wachirapisut 
# 651610348
# Lab10_1
# 229223 Sec 002

def main():
    print(bean_count(-90))

def bean_count(n):
    x = 0
    if n % 100 == 0 or n <= 0: # เป็น 100
        x = 0
    else:
        n = n % 100
        for i in range(1,n+1):
            if (i % 10) == 0: # เป็น 10
                x += -5
            else: # เป็นหลักหน่วย
                x += 1
    return x

if __name__ == '__main__':
    main()