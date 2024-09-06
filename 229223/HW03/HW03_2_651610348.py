#!/usr/bin/env python3
# ภูธเรศวร วชิรพิศุทย์
# 651610348
# HW03_2
# 229223 Sec 002

def main():
    test_min_diff()

def convert_to_24_hour_format(hour, min, period):
    
    if period == "AM" and hour == 12:
        hour = 0
    elif period == "PM" and hour != 12:
        hour += 12

    return (hour, min)


def min_diff(hour1, min1, period1, hour2, min2, period2):

    time_1 = convert_to_24_hour_format(hour1, min1, period1)

    time_2 = convert_to_24_hour_format(hour2, min2, period2)

    total_minutes_1 = time_1[0] * 60 + time_1[1]

    total_minutes_2 = time_2[0] * 60 + time_2[1]

    min_diff = abs(total_minutes_1 - total_minutes_2)

    return min_diff

def test_min_diff():
    assert min_diff(8, 23, 'AM', 8, 24, 'AM') == 1
    assert min_diff(8, 23, 'AM', 1, 24, 'PM') == 301
    assert min_diff(1, 24, 'PM', 8, 23, 'AM') == 301
    print("All Ok!")

if __name__ == '__main__':
    main()