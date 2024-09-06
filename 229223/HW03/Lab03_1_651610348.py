#!/usr/bin/env python3
#Phutharesuan Wachirapisut
#651610348
#Pattrajit Chaiwut
#651610338
#Lab3_1
#229223 Sec 002


import math 
from math import isclose

def main():
	test_circle_intersect()

def circle_intersect(x1,y1,r1,x2,y2,r2,epsilon=10**-6):
	distance = ((x1-x2)**2+(y1-y2)**2)**0.5
	real_distance = (distance-(r1+r2))
	if real_distance>epsilon:
		return (-1)
	if (r1+r2)-distance<=epsilon or math.isclose(0,real_distance):
		return (0)
	else:
		return (1)

def test_circle_intersect():
	assert circle_intersect(2,3,5,5,7,1,epsilon=10**-6)==1
	assert circle_intersect(0,0,2.5,3,4,2.5,epsilon=10**-6)==0
	assert circle_intersect(2,8,3,2,10,1,epsilon=10**-6)==1
	assert circle_intersect(14,2,1,9,1,1,epsilon=10**-6)==-1
	assert circle_intersect(1,1,5,6,17,7,epsilon=10**-6)==-1
	assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon=1.5) == 0

	print ('All OK!')

if __name__ == '__main__':
	main()