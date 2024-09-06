# Transpose

import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

arr_a = np.arange(1,5)
arr_b = np.array(list_a)
arr_c = np.array([list_a,list_b])

print(arr_c.transpose()) # ไม่ถูกเปลี่ยนถาวร ต้องสร้างตัวแปรมารับค่า
 
arr_d = arr_c.transpose()

print(arr_c.shape)
print(arr_d.shape)





