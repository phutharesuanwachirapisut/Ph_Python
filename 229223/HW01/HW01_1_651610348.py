# Phutharesuan Wachirapisut
# 651610348
# HW01_1
# 229223 sec 002

import math
m1=float(input('m1: '))
b1=float(input('b1: '))
m2=float(input('m2: '))
b2=float(input('b2: '))
x=(b2-b1)/(m1-m2)
y=(m2 * b1 - m1 * b2) / (m2 - m1) 
print("Lines intersection at ({:0.2f},{:0.2f})".format(x,y))