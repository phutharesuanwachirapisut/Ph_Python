import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

# array +-*/% with float or int
arr_a = np.arange(1,5)
print(arr_a,arr_a.shape)
print(arr_a + 2)    # บวกทุกตัวใน array
print(arr_a % 2)    # mod 2 ทุกตัว

arr_b = np.array([4,5,6,9])
print(arr_b,arr_b.shape)

# array + array
re = arr_a + arr_b
print(re) # ต้องมี row and column เท่ากัน

arr_c = np.array([list_a,list_a])
arr_d = np.array([list_b,list_c])

if arr_c.shape == arr_d.shape:
    print("arr_d + arr_c = {}".format(arr_d + arr_c))

arr_e = np.array(list_a)

print("บวกแบบ row ไม่เท่ากัน = {}".format(arr_e + arr_c)) 
    # [1,2,3] + [[1,2,3]+[1,2,3]] = [[2 4 6],[2 4 6]] 
    # จะเห็นได้ว่า เป็นการบวกโดยเอา array ที่มี row น้อยกว่ามาบวกกับทุก row ของ array ที่มี row มากกว่า