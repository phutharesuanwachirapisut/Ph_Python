#!/usr/bin/env python3
# ภูธเรศวร วชิรพิศุทย์ (โอโซน)
# 651610348
# ภัทราจิตร ไชยวุฒิ
# 651610338
# Lab02_1
# 229223 Sec 002
import math

def main():
    # รับข้อมูลพื้นที่ผิวจาก user
    surface_area = float(input("input surface area: "))

    # นำพื้นที่ผิวที่ได้มาคำนวณหารัศมี
    radius = find_r_from_surface_area(surface_area)

    # นำรัศมีที่คำนวณได้มาคำนวณหาปริมาตร
    volume = sphere_volume(radius)

    # แสดงปริมาตรทรงกลม แบบทศนิยมสองต่ำแหน่ง
    print("volume = {0:.2f}".format(volume))


def find_r_from_surface_area(surface_area):
    radius=(surface_area/(4*math.pi))**0.5
    return radius

def sphere_volume(radius):
    volume=(4/3)*math.pi*(radius**3)
    return volume

if __name__ == '__main__':
    main()
