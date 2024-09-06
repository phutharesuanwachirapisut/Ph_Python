#!/usr/bin/env python3
# ภูธเรศวร วชิรพิศุทย์
# 651610348
# HW04_1
# 229223 Sec 002

def main():
    text = str(input('text: '))
    c = str(input('c: '))
    print(palindrome_without(text,c))

def palindrome_without(text, c): 
    text = text.lower()
    c = c.lower()
    text = text.replace(c,'')
    text_is_palindrome = isPalindrome(text)
    len_text = len(text)
    if len_text < 1:
        return False
    else:
        if text_is_palindrome:
            return True
        else:
            return False

def isPalindrome(text):
    text = text.lower()
    if text == text[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    main()