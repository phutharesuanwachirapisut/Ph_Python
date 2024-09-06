# ______________________________________________
# 3D array

import numpy as np

list_a = [1,2,3,5]
arr_a = np.array(list_a) # 1D

list_b = [4,5,6,8]
arr_b = np.array([list_a,list_b]) # 2D

list_c = [7,8,9,5]
arr_c = np.array([[list_a],[list_b],[list_c]])

# print(arr_c)
# print(arr_c.ndim)
# print(arr_c[0][0][0]) # มองเป็น ลูกบาศก์ array[dept][row][column]
# print(arr_c[2][0][0])

arr_d = np.array([[list_a,list_a],[list_b,list_a],[list_c,list_a]])
# print(arr_d)
# print(arr_d[2][1][1])

arr_e = np.array([[list_a,list_a,list_b],[list_b,list_a,list_b],[list_c,list_a,list_b]])
print(arr_e)
print(arr_e[1][2][3])
# ______________________________________________

# array index เหมือนกับ matrix
# 3D = มองเป็น ลูกบาศก์ array[dept][row][column]









