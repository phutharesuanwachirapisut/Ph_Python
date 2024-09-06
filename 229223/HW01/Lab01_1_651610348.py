# Phutharesuan Wachirapisut
# 651610348
# Lab01_1   
# 229223 sec 002
import math
a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))
s=(a+b+c)/2
area=math.ceil((s*(s-a)*(s-b)*(s-c))**(1/2))
print("area: ",area)