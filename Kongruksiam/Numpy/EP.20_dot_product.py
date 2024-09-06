# Dot Product
    # การคูณ Matrix

import numpy as np
list_a = [14,22,93]
list_b = [40,58,67]
list_c = [71,108,59]
list_d = [32,55,68]
arr_a = np.arange(1,5)
arr_b = np.array(list_a)

arr_c = np.array([list_a,list_b,list_d])
arr_d = np.array([list_c,list_d,list_a])

dot_product = arr_c.dot(arr_d)
print("dot_product = {}".format(dot_product))









