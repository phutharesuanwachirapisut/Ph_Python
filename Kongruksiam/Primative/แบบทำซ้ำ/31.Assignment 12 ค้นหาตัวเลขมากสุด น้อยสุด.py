
max,min=0,999999999999999999

while  True:
    number=int(input("ป้อนตัวเลข :"))
    if number<=0 :
        break
    if number>max:
        max=number
    if number<min:
        min=number

print("ค่ามากสุด",max)
print("ค่าน้อยสุด",min)