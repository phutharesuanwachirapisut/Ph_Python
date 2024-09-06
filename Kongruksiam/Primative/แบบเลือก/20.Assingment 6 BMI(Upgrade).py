# BMi upgrade

weight=int(input("ป้อนน้ำหนัก (kg): "))
hight=int(input("ป้อนส่วนสูง (cm): "))/100
BMI=(weight//(hight**2))

if BMI>=0 and BMI<=18 :
    result="ต่ำกว่าเกณฑ์"
elif BMI>=18.5 and BMI<=22.9 :
    result=("สมส่วน")
elif BMI>=23.0 and BMI<=24.9 :
    result=("น้ำหนักเกิน")
elif BMI>=50 and BMI<29.9 :
    result=("โรคอ้วนระดับ 1")
elif BMI>=30 :
    result=("โรคอ้วนระดับอันตราย")
else :
    result="ไม่ทราบค่าที่ชัดเจน"
print("BMI = ",BMI,"ทำนายว่า =",result)