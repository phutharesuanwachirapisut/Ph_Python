#!/usr/bin/env python3
#Phutharesuan Wachirapisut
#651610348
#HW5_2
#229223 Sec 002

def main():
    test_transform_name()

def transform_name(name):
    # first_name = name.lstrip()
    # last_name = name.rstrip()
    name = name.strip()
    name = name.split(' ')    
    first_name = name[-1]
    last_name = name[0] 
    
    len_last_name = len(last_name)
    len_first_name = len(first_name)

    len_outside_lname = 5 - len_last_name
    len_outside_fname = 9 - len_first_name

    if len_last_name < 5 and len_first_name < 9:
        last_name = last_name[:]
        first_name = first_name[:]
    elif len_last_name >= 5 and len_first_name >= 9:
        last_name = last_name[:5]
        first_name = first_name[:9]
    elif len_last_name >= 5 and len_first_name < 9:
        last_name = last_name[:5+len_outside_fname]
        first_name = first_name[:]
    elif len_last_name < 5  and len_first_name >= 9:
        last_name = last_name[:]
        first_name = first_name[:9+len_outside_lname]
        
    name = first_name + '.' + last_name
    name = name.title()
    return name

def test_transform_name():
    assert transform_name('elisabeth andre') == 'Andre.Elisabeth'
    assert transform_name('  lena Eive   ') == 'Eive.Lena'
    assert transform_name('Toyoakini shidai') == 'Shidai.Toyoakin' 
    assert transform_name('lala Divesdentinala') == 'Divesdenti.Lala'
    assert transform_name('Yoshimasa Ohmotoyoshi') == 'Ohmotoyos.Yoshi'
    assert transform_name('Tse Michelangelo') == 'Michelangel.Tse'
    assert transform_name(' wachirapisut  phutharesuan') == 'Phuthares.Wachi'
    print("All Ok!")
if __name__ == '__main__':
    main()