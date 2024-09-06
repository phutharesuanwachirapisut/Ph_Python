#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab14_1
# 229223 Sec 002

def main():
    assert count_segment([(2, 7, 1.5),           # a 
                          (3.2, 2.5, 4.06),      # b 
                          (-5.5, -4.5, 2.5),     # c 
                          (2, -5.2, 3),          # d 
                          (7.2, -2.8, 1.2)]) == (2, 1, 2, 3) 
    print('OK')

import copy

def count_segment(list_a): # เพิ่มเติมส่วนที่เป็นเสี้ยว
    list_x = copy.deepcopy(list_a)
    list_y = []
    o_45 = (2**0.5)/2
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for i in list_x:
        x = i[0]
        y = i[1]
        qa = 0
        qb = 0
        qc = 0
        qd = 0
        list_y = [(x,y + i[-1]),(x,y - i[-1]),(x + i[-1],y),(x - i[-1],y)]
        if x < 0 and y < 0:
            qc += 1
        elif x < 0 and y >= 0:
            qb += 1
        elif x >= 0 and y >= 0:
            qa += 1
        elif x >= 0 and y < 0:
            qd += 1
        for j in list_y:
            x = j[0]
            y = j[1]
            if x < 0 and y < 0 and not (i[0] < 0 and i[1] < 0):
                qc += 1
            elif x < 0 and y > 0 and not (i[0] < 0 and i[1] >= 0):
                qb += 1
            elif x > 0 and y > 0 and not (i[0] >= 0 and i[1] >= 0):
                qa += 1
            elif x > 0 and y < 0 and not (i[0] >= 0 and i[1] < 0):
                qd += 1
        
        q1 += qa
        q2 += qb
        q3 += qc
        q4 += qd
    return q1, q2, q3, q4

if __name__ == '__main__':
    main()