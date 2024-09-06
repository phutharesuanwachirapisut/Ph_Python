# !/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab12_2
# 229223 Sec 001
def main():
    assert multiply_polynomials([2, 0, 3],[4, 5]) == [8, 10, 12, 15]
    assert multiply_polynomials([2, 1],[2, 1]) == [4, 4, 1]
    assert multiply_polynomials([2, 0, 3],[2, 1, 2, 5]) == [4,2,10,13,6,15]
    print("All OK")
    print(multiply_polynomials([2, 0, 3],[2, 1, -3]))
    
def multiply_polynomials(p1, p2):
    result = []

    # p1a = p1
    # p1a.reverse()
    # p1_dict = {}
    
    # p2a = p2
    # p2a.reverse()
    # p2_dict = {}
    
    c = 0
    # while c < len(p1a):
    #     p1_dict[c] = p1a[c]
    #     c += 1
    # c = 0
    # while c < len(p2a):
    #     p2_dict[c] = p2a[c]
    #     c += 1
    dict_ = {}
    # c = 0
    # p1_keys_list = list(p1_dict.keys())
    # p2_keys_list = list(p2_dict.keys())
    
    for i in p1:
        d = 0
        for j in p2:
            coeff = i * j
            sum_key = c + d
            if sum_key not in dict_:
                dict_[sum_key] = coeff
            else:
                dict_[sum_key] += coeff              
            d += 1
        c += 1
        
    for key, value in dict_.items():
        result.append(value)
    
    return result

if __name__ == '__main__':
    main()