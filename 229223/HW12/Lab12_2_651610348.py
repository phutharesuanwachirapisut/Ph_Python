#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab12_2
# 229223 Sec 002


def main():
    print(matching_sum((1,), 1))
    print(matching_sum((5,2), 7))
    print(matching_sum((10,-1,1,-8,3,1), 2))
    print(matching_sum((10,-1,1,-8,3,1), 10))

def matching_sum(t, target_value):
    
    t_ = set()
    
    dict_ = {}

    for i in t:
        com = target_value - i
        if com in t_:
            return [i,com]
        t_.add(i)
    return []

if __name__ == '__main__':
    main()