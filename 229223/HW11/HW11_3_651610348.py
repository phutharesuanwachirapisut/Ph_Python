#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW11_3
# 229223 Sec 002

def main():
    assert words_to_num("fourteen") == 14
    assert words_to_num("two hundred forty-eight") == 248
    assert words_to_num("one hundred eleven") == 111
    assert words_to_num("forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two") == 42641323862
    assert words_to_num("twenty thousand") == 20000
    assert words_to_num("seven billion one hundred million thirty one thousand three hundred thirty seven") == 7100031337

    print('OK')
   
def words_to_num(words):
    result = 0
    current_number = 0 
    final_result = 0
    words = words.split()
    unit_dict = {"": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, 
                 "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, 
                 "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, 
                 "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}
    two_digits_unit_dict = {"ten": 10, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
                            "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
    dict_hundred = {"hundred": 100, "thousand": 1000}
    large_num_dict = {"million": 10**6, "billion": 10**9,
                      "trillion": 10**12, "quadrillion": 10**15, "quintillion": 10**18, "sextillion": 10**21}
           
    for word in words:
        if "-" in word:
            parts = word.split("-")
            current_number += two_digits_unit_dict[parts[0]]
            current_number += unit_dict[parts[1]]
        else:
            if word in unit_dict: 
                current_number += unit_dict[word] 
            elif word in two_digits_unit_dict: 
                current_number += two_digits_unit_dict[word] 
            elif word in dict_hundred: 

                if word == "hundred":
                    current_number *= dict_hundred[word]
                    result += current_number
                    current_number = 0
                if word == "thousand" and result == 0:
                    current_number *= dict_hundred[word]
                    result += current_number
                    current_number = 0
                elif word == "thousand" and result != 0:
                    current_number *= dict_hundred[word]
                    result *= dict_hundred[word]
                    result += current_number
                    final_result += result
                    current_number = 0
                    result = 0                    

            elif word in large_num_dict:
                if current_number == 0:
                    final_result += (result) * large_num_dict[word]
                else:
                    final_result += (result + current_number) * large_num_dict[word]
                result = 0
                current_number = 0
            else:
                continue
            
    final_result += result + current_number
    return final_result
if __name__ == '__main__':
    main()