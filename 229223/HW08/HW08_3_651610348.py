#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW08_3
# 229223 Sec 002

def main():
    test_patterned_message()

def patterned_message(message, pattern):
    message = message.replace(" ",'')
    def helper(result, message_index, pattern_index):
        if pattern_index == len(pattern):
           return result

        char = pattern[pattern_index]

        if char.isspace():
           return helper(result + char, message_index, pattern_index + 1)

        message_char = message[message_index % len(message)]
        result += message_char

        return helper(result, message_index + 1, pattern_index + 1)

    pattern = pattern.strip()
    print(helper("", 0, 0))
    


def test_patterned_message():
    assert patterned_message("123", "** *** ** ** ****") == "12 312 31 23 1231"
    assert patterned_message("D and C",'''*************** 
******   ****** 
*************** 
''') == '''DandCDandCDandC 
DandCD   andCDa 
ndCDandCDandCDa
'''
    assert patterned_message("Three Diamonds!",'''    *     *     * 
   ***   ***   *** 
  ***** ***** ***** 
   ***   ***   *** 
    *     *     * ''') == '''    T     h     r 
   eeD   iam   ond 
  s!Thr eeDia monds 
   !Th   ree   Dia 
    m     o     n '''
    print("All OK!")


if __name__ == '__main__':
    main()
