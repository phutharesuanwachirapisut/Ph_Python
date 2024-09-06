#!/usr/bin/env python3
# Phutharesuan_Wachirapisut
# 651610348
# HW06_2
# 229223 Sec 002

def main():
    mylist = [1, 2, 3, 4]
    dest_rotate_list(mylist, 4)  
    print(mylist)  

def dest_rotate_list(list_a, n):
    n = n % len(list_a)  

    if n > 0:  # Rotate to the right
        list_a[:] = list_a[-n:] + list_a[:-n]
    else:  # Rotate to the left
        n = -n
        list_a[:] = list_a[n:] + list_a[:n]

# def test_dest_rotate_list():
#      assert dest_rotate_list([1, 2, 3, 4], 1) == [4, 1, 2, 3]
#      assert dest_rotate_list([1, 2, 3, 4], 105) == [4, 1, 2, 3]
#      assert dest_rotate_list([1, 2, 3, 4], -1) == [2, 3, 4, 1]
#      print('OK')

if __name__ == '__main__':
    main()