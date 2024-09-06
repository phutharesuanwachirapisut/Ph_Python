#!/usr/bin/env python3
#Phutharesuan Wachirapisut
#651610348
#Pattrajit Chaiwut
#651610338
#Lab4_2
#229223 Sec 002

def main():
    test_compare_date()

def compare_date(d1, d2):
    d1=d1.split ('/')
    d2=d2.split ('/')

    if int(d1[2])<int(d2[2]):
        return -1
    elif int(d1[2])>int(d2[2]):
        return 1
    else:
        if int(d1[1])<int(d2[1]):
            return -1
        elif int(d1[1])>int(d2[1]):
            return 1
        else:
            if int(d1[0])<int(d2[0]):
                return -1
            elif int(d1[0])>int(d2[0]):
                return 1
            else:
                return 0

def test_compare_date():
    assert compare_date('29/2/2024', '1/1/2024') == 1
    assert compare_date('28/2/2023', '1/1/2024') == -1
    print("All tests passed!")

if __name__ == '__main__':
    main()
