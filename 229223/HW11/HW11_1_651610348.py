#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW11_1
# 229223 Sec 002

# h = (q + 13(m+1)/5 + k + k/4 + j/4 - 2j) % 7

# h is the day of the week (0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday)
#   เอาไปสร้างปฏิทิน
# q is the day of the month 
#   เอาไปวนลูป
# m is the month (3 = March, 4 = April, 5 = May, ..., 14 = February) 
#   month % 12
# K is the year of the century 
#   year % 100
# J is the zero-based century 
#   year/100
def main():
#     assert display_calendar(2, 2024) == """Su Mo Tu We Th Fr Sa 
# -- -- --  1  2  3  4 
#  5  6  7  8  9 10 11 
# 12 13 14 15 16 17 18 
# 19 20 21 22 23 24 25 
# 26 27 28
# """
#     print('OK')
    return(display_calendar(6, 2024))

def display_calendar(month, year):
    a = False

    if month < 3:
        month += 12
        year -= 1
    m = month
    k = year % 100
    j = year // 100
    print("Su Mo Tu We Th Fr Sa")
    day = 1
    h = (1 + ((13*(m+1))//5) + k + (k//4) + (j//4) - (2*j)) % 7
    year += 1

    if month % 12 == 2 and year % 4 == 0:
        b = 29
    elif month % 12 == 2:
        b = 28
    elif month % 12 in {0, 1, 3, 5, 7, 8, 10}:
        b = 31
    else:
        b = 30
    if h == 0:
        h = 7
    if h != 0:
        a = True
        print("-- " * (h - 1), end='')   
        if h == 0:
            h = 7
        
    for day in range(1, b + 1):
        if a == True:
            print(f"{day:2}", end=" ")
            if h % 7 == 0 and h != 0:
                print()
            h += 1
        else:
            if h % 7 == 0 and h != 0:
                print()
            h += 1
            print(f"{day:2}", end=" ")
    print()
if __name__ == '__main__':
    main()
    # while day <= b:
    #     if day < 10:
    #         if day == 1:
    #             print(" " + str(day), end = "")
    #         else:
    #             if h % 7 == 0:
    #                 print((" " * 2) + str(day))
    #             elif h % 7 == 1 and h != 1:
    #                 print((" ") + str(day), end = "")
    #             else:
    #                 print((" " * 2) + str(day), end = "")
    #         if h == 0:
    #             h += 1
    #     else:
    #         if h % 7 == 0: 
    #             print((" " * 1) + str(day))
    #         elif h % 7 == 1 and h != 1:
    #             print(str(day), end = "")
    #         else:
    #             print((" " * 1) + str(day), end = "")
    #     if day == b:
    #         print("\n")
    #     h += 1
    #     day += 1