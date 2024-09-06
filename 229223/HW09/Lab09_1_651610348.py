#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab09_1
# 229223 Sec 002
def main():
    return(is_anagram("c","ac"))

def is_anagram(s1, s2):
    s1 = s1.lower().replace(" ","")
    s2 = s2.lower().replace(" ","")
        
    if s1 == "" and s2 == "":
        return True
    if s1 == "" or s2 == "":
        return False

    if s1[0] in s2:
        s2 = s2.replace(s1[0], '', 1)
        s1 = s1.replace(s1[0], '', 1)
        return is_anagram(s1, s2)
    else:
        return False

if __name__ == '__main__':
    main()