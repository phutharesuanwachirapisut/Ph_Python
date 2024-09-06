#!/usr/bin/env python3
# ภูธเรศวร วชิรพิศุทย์
# 651610348
# HW03_1
# 229223 Sec 002

def main():
    my_min_mid_max(1,2,3)
    
def my_min_mid_max(a, b, c):
    if a >= b:
        max_ = a
        min_ = b
    else:
        max_ = b
        min_ = a

    if c > max_:
        mid_ = max_
        max_ = c
    elif c < min_:
        mid_ = min_
        min_ = c
    else:
        mid_ = c

    print(f"min = {min_}\nmid = {mid_}\nmax = {max_}")

if __name__ == '__main__':
    main()

