# Index Operator
import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

arr_a = np.arange(1,10)
print("arr_a = {}".format(arr_a))
index = np.array([1,5,7])
print("index = {}".format(index))
print(arr_a[index]) # ต้องใช้ array index ที่เราสร้างขึ้นใหม่เพื่อระบุตำแหน่งของ arr_a
                    # จากตัวอย่างจะได้ array 1D ซึ่งแสดง arr_a[1], arr_a[5], arr_a[7]
arr_b = np.array([list_a, list_b, list_c])
print("arr_b[[0,2]] = {}]".format(arr_b[[0,2]])) # 0 คือ row ที่ 0, 2 คือ column ที่ 2
print("arr_b[[0,1],[2,0]] = {}]".format(arr_b[[0,1],[2,0]]))    # [0,1] คือ row ที่ 0 column ที่ 1 
                                                                # และ [2,0] คือ row ที่ 0 column ที่ 2
arr_c = arr_a[[1,4, 1,4, 1,4]] # แสดง arr_a index ที่ 1 กับ 4 หลายครั้ง     
print("arr_c = {}".format(arr_c))                           # เป็นการแสดงผลแค่ 2 ตัวใน 1 array

arr_d = np.array([[1,-2,-3],[-4,5,8]])
print("arr_d[arr_d < 2] = {}".format(arr_d[arr_d < 2]))
print("arr_d[arr_d < 2]*-1 = {}".format(arr_d[arr_d < 2]*-1,dtype="int"))


