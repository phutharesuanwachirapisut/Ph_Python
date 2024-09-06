#!/usr/bin/env python3
#Phutharesuan Wachirapisut
#651610348
#Pattrajit Chaiwut
#651610338
#Lab4_1
#229223 Sec 002

def main():
    test_is_wildcard_match()

def is_wildcard_match(pattern, word):
    pos_quest = pattern.index('?')
    count_quest = pattern.count('?')
    len_pattern = len(pattern)
    len_word = len(word)
    if len_pattern != len_word:
        return False
 # ถ้าแทน "?" ซึ่งเอาข้อมูลตำแหน่งมาจาก pos_quest เข้าไปในตำแหน่งของ word แล้ว มีค่าเท่ากัน จะคืนค่า True
 # [:pos_quest] and word[pos_quest + count_quest:] == pattern[pos_quest + count_quest:]        
    else:
        if word[:pos_quest] == pattern[:pos_quest] and word[pos_quest + count_quest:] == pattern[pos_quest + count_quest:]:
            return True
        else:
            return False


def test_is_wildcard_match():
    assert is_wildcard_match('c??t', 'cart') == True
    assert is_wildcard_match('c??t', 'caree') == False

    
    print("All tests passed!")

if __name__ == "__main__":
    main()