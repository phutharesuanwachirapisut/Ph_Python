# เขียนโปรแกรมหาตัวเลข มาก / น้อย

from re import A


a = input("ป้อนตัวเลขที่ 1 : ")
b = input("ป้อนตัวเลขที่ 2 : ")

a=int(a)
b=int(b)

if a>b:
     print(a," มากกว่า ",b)
else :
    print(b," มากกว่า ",a)
print("End Program")
'''
if a>b:
     print(str(a)+" มากกว่า "+str(b))
else :
    print(str(b)+" มากกว่า "+str(a))
print("End Program")

'''