age=int(input("ป้อนอายุเพื่อบอกระดับชั้นเรียน : "))

if age<=15:
    if age==15 :
        print("ม.3")
    elif age==14 :
        print("ม.2")
    elif age==13:
        print("ม.1")
    else :
        print("ประถม")
if age>=15 :
    if age==16:
        print("ม.4")
    elif age==17:
        print("ม.5")
    elif age==18:
        print("ม.6")
    else : 
        print("มหาลัย")
print("จบโปรแกรม")