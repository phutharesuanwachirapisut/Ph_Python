#1.แบบลำดับ -> บนลงล่าง ซ้ายไปขวา
#2.แบบเลือก 
#3.แบบทำซ้ำ
'''
If (boolean) -> expression :
    -> statment
'''
age=int(input("ป้อนอายุของคุณ : "))
'''
name=Ozone
print(type(age>=15))
print(name==Ozone)
'''
'''
if age>=15 : 
    print("ตำนำหน้าเป็น นาย/นางสาว")
else : print("คำนำหน้าเป็น เด็กชาย/เด็กหญิง")
print("Ending Program")
'''
'''
if age>=15 and age<=20: 
    print("วัยรุ่น")
if age>=20 and age<=30 :
    print("วัยผู้ใหญ่")
if age>=30 :
    print("วัยทำงาน")
else : print("วัยเด็ก")
print("Ending Program")
'''
# elif = ถ้าเงื่อนไขใดเงื่อนไขหนึ่งเป็นจริง จะไม่แสดงเงื่อนไขอื่น
if age>=15 : 
    print("วัยรุ่น")
elif age>=20  :
    print("วัยผู้ใหญ่")
elif age>=30 :
    print("วัยทำงาน")
else : print("วัยเด็ก")
print("Ending Program")

