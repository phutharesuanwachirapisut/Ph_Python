#!/usr/bin/env python3
# ภูธเรศวร วชิรพิศุทย์
# 651610348
# HW03_3
# 229223 Sec 002


def main():
    test_is_overlapped()

def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):

    # Check if l1,t1 is inside rectangle 2
    if l1 >= l2 and l1 <= l2 + w2 and t1 >= t2 and t1 <= t2 + h2:
        return True

    # Check if l1+w1,t1 is inside rectangle 2
    if l1 + w1 >= l2 and l1 + w1 <= l2 + w2 and t1 >= t2 and t1 <= t2 + h2:
        return True

    # Check if l1,t1+h1 is inside rectangle 2
    if l1 >= l2 and l1 <= l2 + w2 and t1 + h1 >= t2 and t1 + h1 <= t2 + h2:
        return True

    # Check if l1+w1,t1+h1 is inside rectangle 2
    if l1 + w1 >= l2 and l1 + w1 <= l2 + w2 and t1 + h1 >= t2 and t1 + h1 <= t2 + h2:
        return True

    # Check if any corner of rectangle 2 is inside rectangle 1
    if l2 >= l1 and l2 <= l1 + w1 and t2 >= t1 and t2 <= t1 + h1:
        return True

    # Check if l2+w2,t2 is inside rectangle 1
    if l2 + w2 >= l1 and l2 + w2 <= l1 + w1 and t2 >= t1 and t2 <= t1 + h1:
        return True

    # Check if l2,t2+h2 is inside rectangle 1
    if l2 >= l1 and l2 <= l1 + w1 and t2 + h2 >= t1 and t2 + h2 <= t1 + h1:
        return True
        
    # Check if l2+w2,t2+h2 is inside rectangle 1
    if l2 + w2 >= l1 and l2 + w2 <= l1 + w1 and t2 + h2 >= t1 and t2 + h2 <= t1 + h1:
        return True

    # If none of the above conditions are met, the rectangles do not overlap
    return False

def test_is_overlapped():
    assert(is_overlapped(10, 10, 50, 75, 30, 55, 60, 60)) == True
    assert(is_overlapped(10, 10, 50, 75, 70, 55, 60, 60)) == False

if __name__ =="__main__":
    main()