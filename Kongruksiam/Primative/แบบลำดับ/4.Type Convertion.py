#Type Conversion
from re import X
from tkinter import Y


x = 13
y = 1.924
Z = "100"
print(type(X))
print(type(Y))
print(type(Z))

#plus number
result1 = x+y
print(result1)

#string => int เอา int ไว้หน้า string
result2=x+int(Z) # z="100" => int(z)=100
print(result2)

#int => sting เอา str ไว้หน้า int
result3=str(x)+Z # x=13 => str(x)="13"
print(result3)

#string => float 
print(float(Z))
print(float(X))

#float => int ปัดเศษ
print(int(y))
print(type(result3))