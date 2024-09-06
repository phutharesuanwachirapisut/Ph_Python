'''summation=0
while summation!=100 :
    number=int(input("ป้อนตัวเลข :"))
    summation+=number #บวกเลขที่ป้อนในแต่ละรอบ
    print("ผลรวม ",summation)'''# ป้อนตัวเลขจนกว่า summation = 100

summation=0
while True :
    number=int(input("ป้อนตัวเลข :"))
    summation+=number #บวกเลขที่ป้อนในแต่ละรอบ
    if summation>=100:
        break
    print("ผลรวม ",summation)
