# Zero Matrix
import numpy as np
    # 1D
arr_a = np.zeros(5,dtype="int")
# print(arr_a)

    # 2D

arr_b = np.zeros((5,5),dtype="int") # เหมือนกัน
arr_b = np.zeros([5,5],dtype="int") # เหมือนกัน
# print(arr_b)

#________________________________________

# Note:
    # variable = numpy.zeros(ขนาดที่ให้สร้าง ถ้าเป็นหลายมิติให้ทำเป็น list or tuple, dtype) ใช้สร้าง matrix 0
#________________________________________

# One Matrix
    
arr_a = np.ones(10,dtype= "int")
# print(arr_a)

arr_b = np.ones([3,3], dtype="int")
# print(arr_b)

# Note:
    # variable = numpy.ones(ขนาดที่ให้สร้าง ถ้าเป็นหลายมิติให้ทำเป็น list or tuple, dtype) ใช้สร้าง matrix 1
#________________________________________

# Other NUmbers

arr_a = np.full(5, 10) # [10, 10, 10, 10, 10]
arr_b = np.full((3,3),7)    # [[7 7 7]
                            # [7 7 7]
                            # [7 7 7]]
print(arr_b)

# Note: 
   # variance = np.full(ขนาด Matrix, ตัวเลขที่จะแสดงทั้งหมดฝน Matrix)
