#!/usr/bin/env python3
# ภูธเรศวร วชิรพิศุทย์
# 651610348
# HW05_1
# 229223 Sec 002

import string

def main():
    test_is_valid_license()

def is_valid_license(license_str):
    str_digits = string.digits # 0-9
    str_ascii_uppercase = string.ascii_uppercase # อักขระ
    len_license = len(license_str)

    if 1 <= len_license <= 7:
        if len_license <= 2:
            return False
        else:
            if license_str[0] in str_digits and license_str[1] in str_ascii_uppercase and license_str[2] in str_ascii_uppercase: # พิสูจน์ว่าตำแหน่งที่ 1 เป็นตัวเลขหรือไม่ true : แสดงว่ามีสูงสุด 7 ตัว
                backward_str = license_str[3:]
                len_backward_str = len(backward_str)
                if len_license == 3:
                    return True

                elif len_license == 4:
                    backward_str_3 = license_str[3]
                    if backward_str_3 in str_digits:
                        return True
                    else:
                        return False

                elif len_license == 5:
                    backward_str_3 = license_str[3]
                    backward_str_4 = license_str[4]
                    if backward_str_3 in str_digits and backward_str_4 in str_digits:
                        return True
                    else:
                        return False
                
                elif len_license == 6:
                    backward_str_3 = license_str[3]
                    backward_str_4 = license_str[4]
                    backward_str_5 = license_str[5]
                    if backward_str_3 in str_digits and backward_str_4 in str_digits and backward_str_5 in str_digits:
                        return True
                    else:
                        return False

                elif len_license == 7:
                    backward_str_3 = license_str[3]
                    backward_str_4 = license_str[4]
                    backward_str_5 = license_str[5]
                    backward_str_6 = license_str[6]
                    if backward_str_3 in str_digits and backward_str_4 in str_digits and backward_str_5 in str_digits and backward_str_6 in str_digits:
                        return True
                    else:
                        return False          
                else:
                    return False

            elif license_str[0] in str_ascii_uppercase and license_str[1] in str_ascii_uppercase:
                if len_license == 2:
                    return True
                elif len_license == 3:
                    backward_str_2 = license_str[2]
                    if backward_str_2 in str_digits:
                        return True
                    else:
                        return False
                        
                elif len_license == 4:
                    backward_str_2 = license_str[2]
                    backward_str_3 = license_str[3]
                    if backward_str_2 in str_digits and backward_str_3 in str_digits:
                        return True
                    else:
                        return False
                elif len_license == 5:
                    backward_str_2 = license_str[2]
                    backward_str_3 = license_str[3]
                    backward_str_4 = license_str[4]
                    if backward_str_2 in str_digits and backward_str_3 in str_digits and backward_str_4 in str_digits:
                        return True
                    else:
                        return False
                
                elif len_license == 6:
                    backward_str_2 = license_str[2]
                    backward_str_3 = license_str[3]
                    backward_str_4 = license_str[4]
                    backward_str_5 = license_str[5]
                    if backward_str_2 in str_digits and backward_str_3 in str_digits and backward_str_4 in str_digits and backward_str_5 in str_digits:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

    else:
        return False


def test_is_valid_license():
    assert is_valid_license('9AB8954') == True
    assert is_valid_license('9999') == False
    assert is_valid_license('CD700') == True
    assert is_valid_license('99D1234') == False
    assert is_valid_license('1235456786') == False
    assert is_valid_license('aaaaaaaaaabaaa') == False
    assert is_valid_license('9D1234') == False
    assert is_valid_license('9') == False
    assert is_valid_license('131546g') == False

    print("All tests passed!")

if __name__ == '__main__':
    main()
