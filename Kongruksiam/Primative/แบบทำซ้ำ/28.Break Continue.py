i=1
'''while i<=10 :
    print("Round ",i)
    if (i==5):
        break #เมื่อเจอ 5 ให้หยุดโปรแกรม
    i+=1
else:
    print("Ending program")'''

while i<=10 :
    i+=1 
    if (i%2 !=0):
        continue #เป็นการกระโดดข้ามตัวที่ห้าม 2 ไม่ลงตัว
    print("Round ",i)
else:
    print("Ending program")

for i in range(1,11):
    if(i%2 ==0):
        continue
    print("นับเลข :",i)
else:
    print("Ending Program")