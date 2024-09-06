#ต้องการหา summation a ถึง b และ average
'''a=int(input("ป้อนตัวเลขแรก :"))
b=int(input("ป้อนตัวเลขสุดท้าย :"))
summation=0
while a<=b:
    summation+=a #เก็บบผลรวมของ i แต่ละรอบ
    a+=1
    if a-1<b:
        continue
    if summation<b:
        continue
    
    print("รอบที่ :",a-1,"ผลรวม :",summation,"average :",summation//(a-1))'''#บวกเลขเรียง  


start=1
stop=int(input("จำนวนตัวเลข :"))
summation=0
while (start<=stop):
    number=int(input("ป้อนตัวเลข :"))
    summation+=number #บวกเลขที่ป้อนในแต่ละรอบ
    start+=1

print("ผลรวม ",summation,"ต่าเฉลี่ย ",summation/stop)