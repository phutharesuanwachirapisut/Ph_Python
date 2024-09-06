#!/usr/bin/env python3
# ภูธเรศวร วชิรพิศุทย์
# 651610348
# Lab03_2
# 229223 Sec 002

# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function is_p_triple()

def main():
    test_p_triple()

def find_hypotenuse(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

def is_p_triple(x, y, z):
    hypotenuse = find_hypotenuse(x, y, z)
    if hypotenuse == x:
        return y**2 + z**2 == x**2
    elif hypotenuse == y:
        return x**2 + z**2 == y**2
    else:
        return x**2 + y**2 == z**2

def test_p_triple():
    assert is_p_triple(4, 5, 3) == True
    assert is_p_triple(1, 1, 2) == False
    print("all ok!")


if __name__ == '__main__':
    main()



