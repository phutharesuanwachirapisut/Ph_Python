#!/usr/bin/env python3
#Phutharesuan Wachirapisut
#651610348
#Pattrajit Chaiwut
#651610338
#Lab4_2
#229223 Sec 002

def main():
    test_zodiac_element()

def zodiac_power(year):
    if year%2 == 0:
        return 'Yang'
    else:
        return 'Yin'

def zodiac_animal(year):
    buddha_year = year+543
    if buddha_year%12==0:
        return 'Snake'
    if buddha_year%12==1:
        return 'Horse'
    if buddha_year%12==2:
        return 'Goat'
    if buddha_year%12==3:
        return 'Monkey'
    if buddha_year%12==4:
        return 'Rooster'
    if buddha_year%12==5:
        return 'Dog'
    if buddha_year%12==6:
        return 'Pig'
    if buddha_year%12==7:
        return 'Rat'
    if buddha_year%12==8:
        return 'Ox'
    if buddha_year%12==9:
        return 'Tiger'
    if buddha_year%12==10:
        return 'Rabbit'
    else:
        return 'Dragon'

def zodiac_essence(year):
    if year%10==0 or year%10==1:
        return 'Metal'
    if year%10==2 or year%10==3:
        return 'Water'
    if year%10==4 or year%10==5:
        return 'Wood'
    if year%10==6 or year%10==7:
        return 'Fire'
    else:
        return 'Earth'

def zodiac_element(year):
    zodiac = zodiac_power(year)+' '+zodiac_essence(year)+' '+zodiac_animal(year)
    return zodiac


def test_zodiac_element():
    assert zodiac_element(1997)=='Yin Fire Ox'
    assert zodiac_element(2022)=='Yang Water Tiger'
    print('All Ok!')

if __name__ == '__main__':
    main()  