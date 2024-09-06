#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW10_3
# 229223 Sec 002
def main():
    print(polynomial_addition([(3,4), (2, 6), (12, 34), (0, -8)], [(2, -6), (0, 2), (1, 1)]))

def polynomial_addition(p1, p2):
    p1 = sorted(p1)
    p2 = sorted(p2)
    result = []
    i, j = 0, 0

    while i < len(p1) and j < len(p2):
        exp1, coeff1 = p1[i]
        exp2, coeff2 = p2[j]

        if exp1 == exp2:
            coeff_sum = coeff1 + coeff2
            if coeff_sum != 0:
                result.append((exp1, coeff_sum))
            i += 1
            j += 1
        elif exp1 > exp2:
            if coeff2 != 0:
                result.append((exp2, coeff2))
            j += 1
        else:
            if coeff1 != 0:
                result.append((exp1, coeff1))
            i += 1    

    while i < len(p1):
        result.append(p1[i])
        i += 1

    while j < len(p2):
        result.append(p2[j])
        j += 1


    result.sort(reverse=True)
    return result

if __name__ == '__main__':
    main()