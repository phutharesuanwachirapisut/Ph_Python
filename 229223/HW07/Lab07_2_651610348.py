#!/usr/bin/env python3
# Phutharesuan_Wachirapisut
# 651610348
# Pattrajit Chaiwut
# 651610338
# Lab07_2
# 229223 Sec 002

import string
def main():
    uniform('coMP scI!!!')

def uniform(line):
    u = 0
    l = 0
    result_l = list(map(lambda x : 1 if x in string.ascii_lowercase else 0 , line))
    result_l = sum(result_l)

    result_u = list(map(lambda x : 1 if x in string.ascii_uppercase else 0 , line))
    result_u = sum(result_u)

    if result_l > result_u:
        result = line.lower()
    elif result_l < result_u:
        result = line.upper()
    else:
        if line[0] in string.ascii_lowercase:
            result = line.lower()
        else:
            result = line.upper()
    return result

if __name__ == '__main__':
    main()