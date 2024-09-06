# ออกได้ 6 หน้า -> ระบบสุ่ม -> ผู้เล่นเดาเลขให้ถูก

import random
 
myrandom=random.randrange(1,7) # 1-6
a=random.randrange(1,4)
b=0

while True :
    if b==0 :
        print("คุณมีโอกาสแค่ ",a," ครั้งเท่านั้น")
    elif b==1:
        print("คุณเหลือโอกาสแค่",a)
        
    elif b==2:
        print("คุณเหลือโอกาสแค่",a)
    b+=1
    a=a-1
    number=int(input("คำตอบของคุณ :"))
    correct=(myrandom==number)
    if a==0 :
        print("Wrong"," ","คุณหมดโอกาสแล้ว")
        break
    if correct :
        print("Correct")
        break
    else:
        print("Wrong")
        continue
print("Ending Program")

    

