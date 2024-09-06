# Concatenate = การรวมร่าง แค่รวมร่าง เหมือน list + list
import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

arr_a = np.arange(1,8)
arr_b = np.array(list_a)
arr_c = np.array([list_a,list_b])
arr_d = np.array([1,5,9,7,3,1,30])

con_ = np.concatenate((arr_a,arr_d))
print("concatenate = {}".format(con_))

append_1D = np.append(arr_a,55)
print("append 1D = {}".format(append_1D))

append_2D = np.append(arr_c,[[10],[20],[30]],axis=1)
print("append 2D = {}".format(append_2D))









