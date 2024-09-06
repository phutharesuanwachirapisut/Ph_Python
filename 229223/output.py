# "\n" ทำให้แสดงผลข้อความในบรรทัดต่อไป แทนที่จะต่อกันในบบรรทัดเดียวกัน
print("hello","\nrat")
#end="" ทำให้แสดงผลในบรรทัดเดียวกัน แทนที่จะแสดงในบรรทัดต่อไป โดยมี string ใน เครื่องหมายคำพูดของ end คั่นอยู่ 
#sep="" เหมือน end
print("hello",end="**")
print("world")

#.format 
print('{0} and {2} or {1}'.format('eggs','fire','you'))

import math
print('cad: {0:05.2f}'.format(math.pi)) 
    # 0:05.2f means แสดงผลตั้งแต่ตำแหน่งที่ 0 ถึง ทศนิยมลำดับที่ 2 
    # และแสดงผลทั้งหมด 5 ตัว โดยนับจุดด้วย ถ้าไม่ครบจะเติม 0 ข้างหน้า
    # ค่าที่แสดงจะมาจาก Aggrument ใน Format Function

#การหา %
point=17
total=30
print('Persentile: {:.2%}'.format(point/total))

#การใช้ comma คั่นเลขหลักพัน
print('{:,}'.format(1587))

#Date time
import datetime
d= datetime.datetime(2023,2,17,10,25,13)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))