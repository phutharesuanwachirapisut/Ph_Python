# Flatten 
    # array.flatten() ถ้าเกิดการเปลี่ยนแปลงข้อมูลจะไม่มีการเปลี่ยนแปลงด้วย
    # array.reval() # ถ้าเกิดการเปลี่ยนแปลงข้อมูลจะมีการเปลี่ยนแปลงด้วย
import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

arr_a = np.arange(1,5)
arr_b = np.array(list_a)

    # array.flatten() ถ้าเกิดการเปลี่ยนแปลงข้อมูลจะไม่มีการเปลี่ยนแปลงด้วย

arr_c = np.array([list_a,list_b])
print("Before Flatten = {}".format(arr_c))
arr_c_1 = arr_c.flatten()
arr_c[0,0] = 2121212
print("After Flatten = {}".format(arr_c_1)) 

print("arr_b = {}".format(arr_b))
arr_b[0]=12 
print("arr_b = {}".format(arr_b))

    # array.reval() # ถ้าเกิดการเปลี่ยนแปลงข้อมูลจะมีการเปลี่ยนแปลงด้วย

arr_d = np.array([list_a,list_b])
print("Before ravel = {}".format(arr_d))
arr_d_1 = arr_d.ravel()
arr_d[0,0]=512
print("After ravel = {}".format(arr_d_1)) 









