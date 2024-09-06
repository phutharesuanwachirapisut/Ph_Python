#!/usr/bin/env python3
# Phutharesuan Wachirapisut 
# 651610348
# Lab10_2
# 229223 Sec 002

def main():
    comma_separated(3000,4)
    # assert comma_separated(3400,3) == '3,400'
    # assert comma_separated(3400,4) == '3400'
    # assert comma_separated(781588,5) == '7,81588'
    # assert comma_separated(1234) == '1,234'
    # assert comma_separated(1000000) == '1,000,000'
    # print('OK')

def comma_separated(n, digit=3):
    n = str(n)
    i = 0
    for i in range(len(n)):
        if i % digit == 0 and i != 0:
            n = n[:-i-n.count(',')] + "," + n[-i-n.count(','):]
        else:
            i += 1
    print(n)

    # while i < len(n):
    #     if i % digit == 0 and i != 0:
    #         n = n[:-i-n.count(',')] + "," + n[-i-n.count(','):]
    #         i += 1
    #     else:
    #         i += 1
    # print(n)
 
if __name__ == '__main__':
    main()