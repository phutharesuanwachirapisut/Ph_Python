# Append and Insert
    # np.append(array,ตัวที่จะแทรก) เป็นการเพิ่มแบบต่อท้าย
    # np.insert(array,Index,ตัวที่จะแทรก) เป็นการเพิ่มแบบเบือกแทรกในตำแหน่งได้

# 1D
import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

arr_a = np.arange(1,5)
arr_b = np.array(list_a)
arr_c = np.array([list_a,list_b,list_c])
arr_d = np.array([list_c,list_a,list_b])

print("Append 1D : {0}".format(np.append(arr_a,12)))

print("Insert 1D : {0}".format(np.insert(arr_a,1,200)))

print("Insert multiple index : {0}".format(np.insert(arr_a,(1,3),200)))

# 2D
print("arr_c : {}".format(arr_c))

print("Insert 2D in row1 : {0}".format(np.insert(arr_c,1,200,axis=0))) # row = 1
print("Insert 2D in column2 : {0}".format(np.insert(arr_c,2,55,axis=1))) # column = 2
print("Insert 2D of [10,20,30] in column2 : {0}".format(np.insert(arr_c,2,[10,20,30],axis=1))) # column = 2








