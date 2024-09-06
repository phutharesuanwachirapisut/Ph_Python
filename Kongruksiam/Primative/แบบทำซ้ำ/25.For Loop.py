'''for i in range(start,stop,step): #กำหนดรอบ 

for จะเขียนบรรทัดเดียว 
i = เก็บค่าที่ตัวแปร i
start = เริ่มต้นที่ค่าเท่าไหร่
stop = หยุดค่าที่เท่าไหร่
step = การเปลี่ยนแปลงของค่าในแต่ละรอบ'''

n=int(input("ใส่เลข :"))
summation=0
for i in range(-2,n): #เริ่มต้นที่ 0 # for i in range(0,3) เขียนย่อแค่ for i in range(3) 
    #for i in range(0,3,2) = เริ่มที่ 0 จบที่ 3 นับที่ละ 2
    summation+=i
    print("รอบที่ =",i,"sum =",summation) #summation = ผลรวมของเลข i ทบไปเรื่อยๆ
    
print("ผลรวม =",summation)
print("average =", summation/n)