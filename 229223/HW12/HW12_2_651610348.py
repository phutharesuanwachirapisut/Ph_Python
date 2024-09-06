#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW12_2
# 229223 Sec 002

def main():
    assert median_of_median([28, 14,  13,  21,  19,  27,  23,  30,  16,  3]) == 21.0
    assert median_of_median([28, 14,  13,  21,  19,  27,  23,  30,  16,  3, 1]) == 16.0
    assert median_of_median([2, 1, 1, 3]) == 1  # Fixed
    print('OK')
    print(median_of_median([5, 2, 9, 1, 7, 6, 3, 5]))

def median_of_median(list_a):
    list_ = list_a
    list_ = list(map(float,list_))
    while len(list_) > 2:
        sub = []
        sub.append(list_[:(len(list_)//3)])
        sub.append(list_[(len(list_)//3):(2 * len(list_))//3])
        sub.append(list_[(2 * len(list_))//3:])
        
        if len(sub[2]) - len(sub[1]) == 2 and len(list_) % 3 == 2:
            sub[2].append(sub[1][-1])
            sub[1] = sub[1][:-1]
                    
        if len(sub[0]) > 1 or len(sub[1]) > 1 or len(sub[2]) > 1:
            for i in sub:
                g = sub.index(i)
                if len(i) % 2 == 0 and len(i) != 2:
                    v = (i[-1] + i[-2]) / 2
                    i = i[:-2]
                    i.append(v)
                    sub[g] = i
                elif len(i) % 2 == 0 and len(i) == 2:
                    sub[g] = [(i[0] + i[1])/2]
            list_ = list(find_median(sub[0])) + list(find_median(sub[1])) + list(find_median(sub[2]))
        
        else:
            list_ = find_median(sum(sub,[]))
    
    if len(list_) == 2:
        return sum(list_)/2
    else:
        return float(list_[0])

def find_median(a):
    mn = min(a)
    mx = max(a)
    if len(a) > 2 and a.count(mx) == 1 and a.count(mn) == 1:
        a.remove(mn)
        a.remove(mx)
    elif a.count(mx) > 1:
        while a.count(mx) > 1:
            a.remove(mx)
        if len(a) == 2:
            a.remove(max(a))
            return a
    elif a.count(mn) > 1:
        while a.count(mn) > 1:
            a.remove(mn)
        if len(a) == 2:
            a.remove(min(a))
            return a
            
    if len(a) == 1:
        return a
    return a

if __name__ == '__main__':
    main()
