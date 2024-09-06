# Reshape and Resize
    # array.reshape(dimention, member for each of row)
        # ถ้าใช้ใน console -> เป็นการเปลี่ยนแปลงรูปร่างชั่วคราว(ถ้าเรียกใช้งานตัวที่ถูก reshape จะได้ค่าก่อน reshape) ต้องมีตัวมารับค่าถึงจะเปลี่ยนแปลงได้ถาวร
    # array.resize(dimention, member for each of row)
        # ถ้าใช้ใน console -> เป็นการเปลี่ยนถาวระ
import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

arr_a = np.arange(10)
print("Before Reshape = {}".format(arr_a))  # [0 1 2 3 4 5 6 7 8 9]
print("After Reshape = {}".format(arr_a.reshape((2,5))))   # [[0 1 2 3 4],[5 6 7 8 9]]
print("arr_a = {}".format(arr_a)) # ใช้อธิบายความต่างของ reshape กับ resize

arr_b = np.arange(10) 
print("Before Resize = {}".format(arr_b))
arr_b.resize(2,5)
print("Ater Resize = {}".format(arr_b))
arr_c = np.array([list_a,list_b])

















