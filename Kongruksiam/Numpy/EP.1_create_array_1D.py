# list and array

# array 
    # มีขนาดที่แน่นอน และเปลี่ยนแปลงขนาดไม่ได้
#***# มีข้อมูลได้แค่ 1 ชนิด ถ้าเป็น int ก็เป็น int ทั้งหมด
    # มีชื่อเรียกคือ ndarray

# ______________________________________________
# 1D array

import numpy as np

arr_a = np.array(1) # creating array by numpy, output = 1
arr_adim = arr_a.ndim # showing array dimension, output = 0

arr_b = np.array([1,2,3]) # 1D array , output = [1 2 3]
arr_bdim = arr_b.ndim # output = 1

list_a =[1,2,3,4]
arr_c = np.array(list_a) # output = [1 2 3 4]
arr_cdim = arr_c.ndim # output = 1

tup1 = (1,2,2,3,5)
arr_d = np.array(tup1)  # output = [1 2 2 3 5]
arr_ddim = arr_d.ndim # output = 1
print(arr_d,"\n",arr_ddim)

# ______________________________________________

# Note: 
    # varian = numpy.array(list)    เป็นการสร้าง array 1D
    # varian_a = varian.ndim        เป็นการแสดงมิติของ array