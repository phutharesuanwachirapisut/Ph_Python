# idea = 1+2+3+4+5

i=1 #ตัวนับรอบ
summation = 0 #เก็บผลบวก
average=0 #ผลรวม/จำนวนรอบ
n=int(input("number : "))
while i<=n:
    summation+=i #เก็บบผลรวมของ i แต่ละรอบ
    i+=1
    print("รอบที่ =", i-1 ,",ค่า sum = ",summation)
average=summation/n
print("ผลรวมการบวกเลข = ",summation)
print("ค่าเฉลี่ย = ",average)