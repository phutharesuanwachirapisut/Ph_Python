#!/usr/bin/env python3
# Phutharesuan_Wachirapisut
# 651610348
# HW07_3
# 229223 Sec 002

def main():
    # test_num_to_world()
    a = int(input("Enter a number: "))
    print(num_to_word(a))
    return(num_to_word(a))
def three_digits_to_word(n):
    unit_list = ["", "one", "two", "three", "four", "five", 
                 "six", "seven", "eight", "nine", "ten", 
                 "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
                 "sixteen", "seventeen", "eighteen", "nineteen"]
                 
    two_digits_unit_list = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    three_digits_unit_list = list(map(lambda x: x + " hundred", unit_list))

    if n > 99:
        n_hun = n // 100
        hun = three_digits_unit_list[n_hun]
        n_ten = n % 100

        if n_ten < 20:
            ten = unit_list[n_ten]
            result = f'{hun} {ten}' if ten else hun

        else:
            n_ten = n_ten // 10
            ten = two_digits_unit_list[n_ten]
            dig = unit_list[n % 10]
            result = f'{hun} {ten}' + (f'-{dig}' if dig else '')

    else:  # Two digits or less
        n_ten = n

        if n_ten < 20:
            result = unit_list[n_ten]

        else:
            n_ten = n_ten // 10
            ten = two_digits_unit_list[n_ten]
            dig = unit_list[n % 10]
            result = f'{ten}' + (f'-{dig}' if dig else '')

    return result

def num_to_word(num):
    if num == 0:
        return "zero"
    
    sextillion = (num % 10**24) // 10**21
    quintillion = (num % 10**21) // 10**18
    quadrillion = (num % 10**18) // 10**15
    trillion = (num % 10**15) // 10**12
    billion = (num % 10**12) // 10**9
    million = (num % 10**9) // 10**6
    thousand = (num % 10**6) // 1000
    ones = num % 1000

    result = ""
    if sextillion > 0:
        result += three_digits_to_word(sextillion) + " sextillion "
    if quintillion > 0:
        result += three_digits_to_word(quintillion) + " quintillion "
    if quadrillion > 0:
        result += three_digits_to_word(quadrillion) + " quadrillion "
    if trillion > 0:
        result += three_digits_to_word(trillion) + " trillion "
    if billion > 0:
        result += three_digits_to_word(billion) + " billion "
    if million > 0:
        result += three_digits_to_word(million) + " million "

    if thousand > 0:
        result += three_digits_to_word(thousand) + " thousand "

    if ones > 0:
        result += three_digits_to_word(ones)

    return result.strip()
    
def test_num_to_world():
    assert num_to_word(14) == "fourteen"
    assert num_to_word(248) == "two hundred forty-eight"
    assert num_to_word(111) == "one hundred eleven"
    assert num_to_word(0) == "zero"
    assert num_to_word(42641323862) == "forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two"
    print("OK!")

if __name__ == '__main__':
    main()

