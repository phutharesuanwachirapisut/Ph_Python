# C = (F-32)5/9
# F = C*9/5 +32

temp=input("ป้อนอุณหภูมิ (องศา) :") #ต้องเติมตัวอักษรด้วย เช่น 45 C

degree=int(temp[:-2]) # number
unit=temp[-1].upper() # C

if unit=="C" :
    result=(9*degree)/5+32 #แปลงเป็นฟาเรนไฮน์
    unit_result="ฟาเรนไฮน์"
elif unit=="F" :
    result=((degree-32)*5/9) #แปลงเป็นเซลเซียส
    unit_result="เซลเซียส"

print("แปงตัวเลข = ", temp,"เป็น",unit_result,"=",result)