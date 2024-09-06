#!/usr/bin/env python3
# Phutharesuan_Wachirapisut
# 651610348
# HW07_1
# 229223 Sec 002

def main():
    square_frame(4, '.')

def square_frame(n, sep=' '):
    l_n = list(range(1, 4*n - 4 + 1)) # (n**2) - ((n-2)**2) + 1
    r_n = list(range(len(str(l_n[-1])),len(str(l_n[-1]))+1))*(len(l_n)) # สร้าง list จำนวนหลักที่มากที่สุด
    l_n = list(map(lambda x , y : str(x).zfill(y), l_n,r_n)) # ทำให้ตัวเลขใน main list มีจำนวนหลักเท่ากันโดยแทนที่ด้วย 0 ด้านหน้า

    point = list(map(lambda x: (x+1) * sep ,r_n)) # สร้าง list '.'
    point = point[:n] # แสดงแค่ n ตัว

    list_a = list(map(lambda x :(x + sep if int(x) < n or not n <= int(x) < 2 * n else x ) ,l_n))
    list_first = "".join(list_a[:n])
    
    list_middle_back = list_a[n:2*n-2]
    list_middle_back = list_middle_back[::-1]
    list_middle_infront = list_a[2*n+(n-2):]
    list_middle = list(map(lambda x , y , z  : x + y*(n-2) + z ,list_middle_infront, point , list_middle_back ))
    list_middle = list_middle[::-1]
    list_middle = '\n'.join(list_middle)
    
    list_last = list_a[2*n-1:2*n+(n-2)]
    list_last = list_last[::-1] + list(str(list_a[2*n-2]))
    list_last = ''.join(list_last)
    result = list_first + "\n" + list_middle + "\n"  + list_last
    print(result)

if __name__ == '__main__':
    main()