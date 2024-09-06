# 1.การเข้าถึงตัวอักษรใน string เช่นการเลือกแสงผลตัวอักษรบางตัว
# 2.len function ระบุความยาวของตัวอักษรทั้งหมด
# 3.strip() ลบช่องว่าง
# 4.upper() lower() mำให้ตัวอักษรเป็นพิมพ์ใหญ่ และพิมพ์เล็ก
# 5.capitaliazed() ตัวหน้าสุดเป็นตัวพิมพ์ใหญ่
# 6.replace(ข้อความที่จะเปลี่ยน,ข้อความที่ถูกเปลี่ยน,ตำแหน่งของข้อความที่จะเปลี่ยน) การแทนที่
# 7.การต่อ string
# 8.การจัดรูปแบบการแสดงผลด้วย format และ {}
# 9.count = การนับจำนวนคำในประโยค 
# 10.startswith endswith = การเช็คคำขึ้นต้น และลงท้าย

# 1.การเข้าถึงตัวอักษรใน string เช่นการเลือกแสงผลตัวอักษรบางตัว
'''name=' phutharesuan wachirapisut : 18 ' # index มีค่า = ช่องของตัวอักษร
                    # index => 0
                    # [0:5] แสดงผลตัวอักษรแรกในข้อความถึงตัวที่6 ปล.เริ่มนับตัวแรกจาก 1
                    # ช่องว่างนับเป็น 1 ตัวอักษร

print("อายุเท่าไหร่ = ",name[-3:])'''


# 2.len function ระบุความยาวของตัวอักษรทั้งหมด
'''print(len(name)) # len ความยาวตัวอักษรทั้งหมด'''

# 3.strip() ลบช่องว่าง
'''
print(name)
name=name.strip() # strip ลบช่องว่างซ้ายขวา
                  # lstrip ลบช่องว่างทางซ้าย 
                  # rstrip ลบช่องว่างทางขวา
print(len(name))
'''
# 4.upper() lower() mำให้ตัวอักษรเป็นพิมพ์ใหญ่ และพิมพ์เล็ก
'''name="phutharesuan wachirapisut"
print(name.upper()) # upper ทำให้เป็นตัวพิมพ์ใหญ่ทั้งหมด
print(name.lower()) # lower ทำให้เป็นตัวพิมพ์เล็กทั้งหมด'''

# 5.capitaliazed() ตัวหน้าสุดเป็นตัวพิมพ์ใหญ่
'''print(name.capitalize()) #capitalize ทำตัวแรกเป็นตัวพิมพ์ใหญ่'''

# 6.replace(ข้อความที่จะเปลี่ยน,ข้อความที่ถูกเปลี่ยน,ตำแหน่งของข้อความที่จะเปลี่ยน) การแทนที่
'''name="phutharesuan phutharesuan wachirapisut"

print(name.replace("phutharesuan","Name : ",1)) 
'''
# replace แทนที่ ex. ("phutharesuan" <-- ข้อความที่จะเปลี่ยน,"Name : " <-- ข้อความที่จะแทนที่,1 <-- ตำแหน่งของข้อความที่จะเปลี่ยน)
'''
a = "phu" in name

if a : 
    name=name.replace("phutharesuan","wachirapisut")

print(name)'''

#จาก a ถ้ามี "phu" อยู่ใน name ให้แทนที่ phutharesuan ด้วย wachirapisut 
# ถ้าไม่มี ก็ไม่ต้องทำอะไร

# 7.การต่อ string
'''
Aname="phutharesuan "
Bname="ozone "
age="18"
fullname=Aname +Bname +age
#print(fullname+" 123")
print("ชื่อเล่น : "+ Bname+"\tชื่อจริง : " +"\tอายุ : "+age+"ปี")
'''
# 8.การจัดรูปแบบการแสดงผลด้วย format และ {}
'''
Aname="phutharesuan "
Bname="ozone "
salary=15000.586

text= "ชื่อเล่น : {0} \tชื่อจริง : {1} \tอายุ : {3} \tsalary : {2:.2f}" # {n} ; n = ตำแหน่งของข้อมูลใน format # .2F จากตัวอย่าง หมายถึง เอาทศนิยมแค่ 2 ตำแหน่ง
print(text.format(Aname,Bname,salary,"18 ปี"))   # text.format() = เซตที่มีข้อมูลเก็บเอาไว้ สามารถนำมาเรียกใช้ได้โดยระบุตำแหน่งด้วย {n}
'''

# 9.count = การนับจำนวนคำในประโยค 
'''fruit="มังคด มะละกอ กล้วย ส้ม ส้ม มะละกอ ละมุด"

print(fruit.count("ส้ม"))'''

# 10.startswith endswith = การเช็คคำขึ้นต้น และลงท้าย
'''name="นายภูธเรศวร วชิรพิศุทย์"

print(name.startswith("นาย"))

if name.startswith("นาย") :
    print("เพศชาย")
else :
    print("เพศหญิง เด็ก หรือบุคคลอื่น")

if name.endswith("วชิรพิศุทย์") :
    print("อยู่ในตระกูล")
else : 
    print("อยู่นอกตระกูล")'''
