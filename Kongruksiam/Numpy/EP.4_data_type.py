# Data Type
import numpy as np

list_a = [1,2,3,5]
arr_a = np.array(list_a)
print(arr_a.dtype)

arr_b = np.array([1.2,2.5,22.33,3.69])
print(arr_b.dtype)

arr_c = np.array([1.+0.j, 2.+0.j, 3.+0.j, 4.+0.j])
print(arr_c.dtype)

arr_d = np.array(["fasf","fafqw","daf"])
print(arr_d.dtype)

#___________________________________________
# Note
    # variance.dtype แสดง data type ของตัวแปร