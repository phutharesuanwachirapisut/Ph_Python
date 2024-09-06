#!/usr/bin/env python3
# @Author: Phutahresuan Wachirapisut 651610348
# @Last Modified time: 2022-09-24 21:16:41




def main():
    print(cat_altar(int(input())))


def cat_altar(n):
    cat = \
    ''' ／|、    |
(°、。7   |
|、 ~ヽ  |
ᒐᒐ_f_ )ノ|
__________|
'''
    for i in range(n+1):
        list_cat = cat
    return cat*n


if __name__ == '__main__':
    main()
