#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab01_2 
# 229223 sec 002
import math
inputmilliseconds =int(input('Input milliseconds: '))

day=int(inputmilliseconds/86400000)
hour=int((inputmilliseconds%86400000)/(86400000/24))
minute=int((inputmilliseconds%(86400000/24))/(86400000/24/60))
second=int((inputmilliseconds%(86400000/24/60))/(86400000/24/60/60))
millisec=int((inputmilliseconds%(86400000/24/60/60)))

math.floor(day)
print("Day(s): ",day)
math.floor(hour)
print("Hour(s): ",hour)
math.floor(minute)
print("Minute(s): ",minute)
math.floor(second)
print("Second(s): ",second)
print("Millisec(s): ",millisec)