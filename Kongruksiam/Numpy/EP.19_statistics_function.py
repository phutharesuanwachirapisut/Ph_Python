# Statistics Function
import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

arr_a = np.arange(1,5)
arr_b = np.array(list_a)
arr_c = np.array([list_a,list_b])

# 1D
print("sum: {}".format(arr_a.sum()))
print("prod: {}".format(arr_a.prod())) # ผลคูณสมชทั้งหมด (factoria)
print("min: {}".format(arr_a.min()))
print("argmin: {}".format(arr_a.argmin())) 
print("max: {}".format(arr_a.max()))
print("argmax: {}".format(arr_a.argmax())) # ตำแหน่งของ arr_a.max(

# 2D
    # axis 0 = แนวตั้ง (มองเป็นจำนวน column)
    # axis 1 = แนวนอน (มองเป็นจำนวน ROW)

print("min in axis 1: {}".format(np.min(arr_c,axis=1))) # ค่าที่ต่ำสุดของ แต่ละแถวแนวนอน 
print("min in axis 0: {}".format(np.min(arr_c,axis=0)))






