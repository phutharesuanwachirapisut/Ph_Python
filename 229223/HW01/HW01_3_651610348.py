#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW01_3
# 229223 sec 002
import math
old_price=int(float(input("Old Price: ")))
old_price_hundred=math.floor(old_price/100)
old_price_ten=math.floor((old_price%100)/10)
old_price_unit=int(float(old_price%10))

if old_price_hundred>0:
    if old_price_ten>=5:
        old_price_ten=9
        old_price_unit=8
        print("New Price: " , old_price_hundred * 100 + old_price_ten * 10 + old_price_unit , sep="")
    else:
        old_price_hundred=old_price_hundred-1
        old_price_ten=9
        old_price_unit=8
        print("New Price: " , old_price_hundred * 100 + old_price_ten * 10 + old_price_unit , sep="")
else:
    print("New Price: " , 0)
