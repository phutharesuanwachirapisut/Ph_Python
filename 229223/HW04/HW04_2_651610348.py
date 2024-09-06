#!/usr/bin/env python3
# ภูธเรศวร วชิรพิศุทย์
# 651610348
# HW04_2
# 229223 Sec 002

def main():
    test_rotate()

def rotate(num, pos):
    num = str(num)
    pos = int(pos)
    len_num = len(num)
    if pos >= 0: # เป็นบวก
        if pos >= len_num:
            pos = pos % len_num # len_num = 6 and pos = 7 จะวนกลับมายัง pos = 1

        back_value_num = num[(-1*pos):] # ใช้เก็บค่าที่จะเอาไปแทรกหน้า/หลัง
        forward_value_num = num[:-1*pos]
        num = int(back_value_num + forward_value_num)
        return num
    elif pos < 0:
        if pos >= len_num:
            pos = pos % len_num # len_num = 6 and pos = 7 จะวนกลับมายัง pos = 1
        pos=-1*(pos)
        forward_value_num = num[pos:]
        back_value_num = num[:pos]
        num = int(forward_value_num + back_value_num)
        return num

def test_rotate():
    assert rotate(12345,3) == 34512
    assert rotate(12345,2) == 45123
    assert rotate(12345,-3) == 45123
    assert rotate(1597,-1) == 5971
    print("All Ok!")

if __name__ == '__main__':
        main()