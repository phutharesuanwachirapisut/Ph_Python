#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW10_1
# 229223 Sec 002
def main():
    # assert float_to_base_b(44.1875, 2) == '101100.001100'
    # assert float_to_base_b(0.99999999, 2) == '0.111111'
    # assert float_to_base_b(-3.1415, 3) == '-10.010211'
    # assert float_to_base_b(300.9375, 16) == '12C.F00000'
    # print('OK')
    print(float_to_base_b(3123465784.9375,16))

def float_to_base_b(x, b):
    
    if x < 0:
        x = abs(x)
        return "-" + str(forward_base(x,b)) + "." + backward_base(x,b)
    else:
        return str(forward_base(x,b)) + "." + backward_base(x,b)

def forward_base(x, b):
    list_a = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D',"E","F"]
    x = int(x // 1)
    if b > 9:
        if b > x:
            return list_a[x]
        else:
            result = str(forward_base(x//b,b)) + str(list_a[x % b])
            return str(result)
    else:
        if b > x:
            return x
        else:
            result = str(forward_base(x//b,b)) + str(list_a[x % b])
            return int(result)

def backward_base(x,b):
    list_a = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D',"E","F"]
    x = x % 1
    a = ""
    while len(a) < 6 and x != 0:
        x = x * b
        if x >= 1:
            a += str(list_a[int(x//1)])
            x = x - (x//1)
        else:
            a += '0'

    if len(a) < 6:
        a += "0"*(6 - len(a))
    return a

if __name__ == '__main__':
    main()