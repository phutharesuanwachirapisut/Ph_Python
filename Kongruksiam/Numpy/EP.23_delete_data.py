# Delete Data from Array
    # np.delete(array,index)
import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

arr_a = np.arange(1,5)
arr_b = np.array(list_a)
arr_c = np.array([list_a,list_b])

arr_d = np.arange(1,13).reshape(4,3)

print("arr_a : {}".format(arr_a,2))
print("Delete 1D : {}".format(np.delete(arr_a,2)))

print("arr_d: {}".format(arr_d,2))
print("Delete 2D : {}".format(np.delete(arr_d,2,axis=1)))











