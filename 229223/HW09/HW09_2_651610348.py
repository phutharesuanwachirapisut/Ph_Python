#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW09_2
# 229223 Sec 002
def main():
    assert longest_digit_run(11777338) == 3
    assert longest_digit_run(117733878) == 2
    print("ok")

def longest_digit_run(n):
    max = 1
    current = 1
    return help_me_plz(n,max, current)
    
def help_me_plz(n,max=1,current=1):
    n = str(n)
    if len(str(n)) == 1:
        return max
    else:
        if n[0] == n[1]:
           current += 1
        else:
            current = 1
        if current >= max:
            max = current
    return help_me_plz(n[1:], max, current)
    
if __name__ == '__main__':
    main()