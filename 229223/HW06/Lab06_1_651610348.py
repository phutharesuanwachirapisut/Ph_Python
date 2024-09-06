#!/usr/bin/env python3
# Phutharesuan_Wachirapisut
# 651610348
# Pattrajit Chaiwut
# 651610338
# Lab06_1
# 229223 Sec 002


def main():
    test_triangle()


def triangle(n):
    n = int(n)
    n_1 = list(range(2 , n))
    n_2 = list(range(n,n+1))
    b = list(map(lambda x: '*' + ('.'*(2*(x-1)-1)) + '*',n_1))
    c = list(map(lambda x: '* '*n ,n_2))
    start = list('*')
    result = start +b +c
    result = '\n'.join(result)
    result = result + '\n'
    return result



def test_triangle():

    T3 = '''
*
*.*
* * *
'''

    T7 = '''
*
*.*
*...*
*.....*
*.......*
*.........*
* * * * * * *
'''

    assert triangle(3) == T3
    assert triangle(7) == T7
    print("OK")


if __name__ == '__main__':
    main()
