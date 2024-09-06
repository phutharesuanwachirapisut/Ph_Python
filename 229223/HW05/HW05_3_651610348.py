#!/usr/bin/env python3
# ภูธเรศวร วชิรพิศุทย์
# 651610348
# HW05_3
# 229223 Sec 002

def main():
    test_to_roman_numeral()

def to_roman_numeral(n): 
    n = int(n)
    roman_n = ''
    thoun_n = n//1000 # M(1000)
    hund_n = (n - (thoun_n*1000))//100 # C(100) and D(500)
    ten_n = (n - (thoun_n*1000) - (hund_n*100))//10 # X(10) and L(50)
    one_n = (n - (thoun_n*1000) - (hund_n*100) - (ten_n*10)) # I(1) and V(5)
    
    if thoun_n <= 4 and thoun_n >= 0:
        roman_n += 'M'*thoun_n
    else:
        roman_n += ''

    if hund_n < 4 and hund_n >= 0:
        roman_n += 'C'*hund_n
    elif hund_n == 4:
        roman_n += 'CD'
    elif hund_n == 5:
        roman_n += 'D'
    elif hund_n == 9:
        roman_n += 'CM'
    else:
        roman_n += 'D' + 'C'*(hund_n-5)
    
    if ten_n < 4 and ten_n >= 0:
        roman_n += 'X'*ten_n
    elif ten_n == 4:
        roman_n += 'XL'
    elif ten_n == 5:
        roman_n += 'L'
    elif ten_n == 9:
        roman_n += 'XC'
    else:
        roman_n += 'L' + 'X'*(ten_n-5)
    
    if one_n < 4 and one_n >= 0:
        roman_n += 'I'*one_n
    elif one_n == 4:
        roman_n += 'IV'
    elif one_n == 5:
        roman_n += 'V'
    elif one_n == 9:
        roman_n += 'IX'
    else:
        roman_n += 'V' + 'I'*(one_n-5)

    return roman_n




def test_to_roman_numeral():
    assert to_roman_numeral(1) == "I"
    assert to_roman_numeral(4) == "IV"
    assert to_roman_numeral(9) == "IX"
    assert to_roman_numeral(25) == "XXV"
    assert to_roman_numeral(22) == "XXII"
    assert to_roman_numeral(0) == ""
    assert to_roman_numeral(222) == "CCXXII"
    assert to_roman_numeral(2222) == "MMCCXXII"
    assert to_roman_numeral(267) == "CCLXVII"
    assert to_roman_numeral(4999) == "MMMMCMXCIX"
    print("All tests passed!")

if __name__=='__main__':
    main()