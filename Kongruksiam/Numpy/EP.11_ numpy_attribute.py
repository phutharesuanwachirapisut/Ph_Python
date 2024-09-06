import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]
arr_a = np.array([list_a,list_b,list_c])

# 1. np.ndim
arr_a_ndim = arr_a.ndim
# 2. dtype
arr_a_dtype = arr_a.dtype
# 3. shape -> บอกโครงสร้าง ดังตัวอย่าง ได้ output = (3,3)
arr_a_shape = arr_a.shape
# 4. size -> บอกจำนวนสมาชิก
arr_a_size = arr_a.size
# 5. itemsize -> บอกขนาด byte โดยเอาตัวเลขข้างหลัง dtype มาหาร 8 เช่น int32 เอา 32/8 ได้ 4
arr_a_itemsize = arr_a.itemsize
print(arr_a_itemsize)



