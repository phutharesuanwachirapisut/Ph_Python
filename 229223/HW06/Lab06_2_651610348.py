#!/usr/bin/env python3
# Phutharesuan_Wachirapisut
# 651610348
# Pattrajit Chaiwut
# 651610338
# Lab06_2
# 229223 Sec 002


def main():
    test_classify()


def classify(list_x):
    list_a = [] # เก็บ int
    list_b = [] # เก็บ float
    list_c = [] # เก็บ str
    list_a = list(filter(lambda x : isinstance(x, int),list_x))

    list_b = list(filter(lambda x : isinstance(x, float),list_x))

    list_c = list(filter(lambda x : isinstance(x, str),list_x))
    return list_a , list_b ,list_c


def test_classify():
    assert classify([10 , 'hello' ,230.5 ,4]) == [10,4]
    [230.5]
    ['hello']
    print("OK")


if __name__ == '__main__':
    main()