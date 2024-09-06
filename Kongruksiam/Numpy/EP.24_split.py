# Split     
    # เป็นการแบ่ง array จาก 1 ชิ้น เป็นหลาย ๆ ชิ้น ชิ้นละเท่ากัน ต้องเท่ากัน!!
    # np.split(array,แบ่ง array กี่ส่วน แต่ต้องสอดคล้องกับจำนวนสมาชิก)
    # ไม่มี เศษ!!

# 1D
import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

arr_a = np.arange(1,21)
arr_b = np.array(list_a)
arr_c = np.array([list_a,list_b])

arr_d = np.arange(1,13).reshape(4,3)

print("arr_a : {}".format(arr_a))
print("Split 1D : {}".format(np.split(arr_a,4)))

# 2D
    # np.hsplit(array, แบ่ง array กี่ส่วน ) -> เป็นการแบ่งตามแนวแกนตั้ง
    # np.vsplit(array, แบ่ง array กี่ส่วน ) -> เป็นการแบ่งตามแนวแกนนอน

print("arr_d : {}".format(arr_d))
print("Split 2D แกนตั้ง : {}".format(np.hsplit(arr_d,3)))
print("Split 2D แกนนอน : {}".format(np.vsplit(arr_d,4)))







