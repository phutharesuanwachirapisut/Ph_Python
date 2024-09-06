# Identity Matrix

import numpy as np
arr_a = np.identity(4,dtype="int")
print(arr_a)
arr_b = np.eye(5,5,dtype="int")
print(arr_b)
arr_c = np.eye(5,k=2,dtype="int") # เลื่อนเส้นทะแยงมุมของเลข 1 ไปทางขวา ตามค่า k
print(arr_c)

# Note: np.eye() กำหนดขนาดได้ แต่ np.identity() จะสร้างแบบจัตุรัส
