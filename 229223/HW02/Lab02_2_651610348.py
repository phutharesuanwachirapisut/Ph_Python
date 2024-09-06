#!/usr/bin/env python3
# ภูธเรศวร วชิรพิศุทย์ (โอโซน)
# 651610348
# ภัทราจิตร ไชยวุฒิ
# 651610338
# Lab02_1
# 229223 Sec 002

def main():
    test_reverse_digits()


# implement ฟังก์ชันนี้ให้ถูกต้อง
def reverse_digits(x):
    rev_num=(abs(x)%10)*1000+((abs(x)//10)%10)*100+((abs(x)//100)%10)*10+((abs(x)//1000)%10)
    return rev_num


# เพิ่ม test case อื่นๆ ตามความเหมาะสม
def test_reverse_digits():
    assert reverse_digits(1234) == 4321
    assert reverse_digits(1) == 1000
    assert reverse_digits(123) == 3210
    assert reverse_digits(12) == 2100
    assert reverse_digits(-1235) == 5321
    assert reverse_digits(-123) == 3210
    assert reverse_digits(-12) == 2100
    assert reverse_digits(-1) == 1000
    print("All OK!")

if __name__ == '__main__':
    main()