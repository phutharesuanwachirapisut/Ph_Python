#!/usr/bin/env python3
#Phutharesuan Wachirapisut
#651610348
#Pattrajit Chaiwut
#651610338
#Lab4_1
#229223 Sec 002

import string

def main():
    test_german_num_format()

def german_num_format(num_str): # ทำให้ไม่เกิดการทำซ้ำ เช่น แปลง period เป็น comma แล้วก็แปลง comma เป็น period

    comma = ',' in num_str
    if comma:
        num_str = num_str.replace(',','s')

    period = '.' in num_str 
    if period:
        num_str = num_str.replace('.',',')
    
    num_str=num_str.replace('s','.')
    return num_str
 
def test_german_num_format():
    assert german_num_format('1,234') == '1.234'
    assert german_num_format('1,020.50') == '1.020,50'
    print("All OK!")

if __name__ == '__main__':
    main()