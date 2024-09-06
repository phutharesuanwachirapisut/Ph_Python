# Broadcasting
    # กรณีที่ array มีขนาดไม่เท่ากัน แล้วเกิดการดำเนินการทางคณิตศาสตร์
    # เช่น array 1D + array 2D
    # ถ้า เป็น 1D(1 row)และ มี column เท่ากันกับ อีก array สามารถดำเนินการได้โดยเกิดกาใช้ row 1 row นั้น มาดำเนินการทุก row ของอีก array
    # และในทำนองเดียวกับ array 1x1
import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

arr_a = np.arange(1,5)
arr_b = np.array(list_a)
arr_c = np.array(list_a,list_b)