import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

# slice array 1D
# array[start:stop:step]

arr_a = np.arange(1,10)
a = arr_a[:]
b = arr_a[1:]
c = arr_a[:6]
d = arr_a[2:8]
e = arr_a[::2]

# slice array 2D
# array[start:stop:step,start:stop:step]
# array[row,column]
arr_b = np.array([list_a,list_b,list_c])
print(arr_b[0:3,1:]) # แสดง row 3 แถว และ column 2 แถวหลัง
print(arr_b[1:2,1:2])
print(arr_b[::2,:])





