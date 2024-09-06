#!/usr/bin/env python3
# Phutharesuan_Wachirapisut
# 651610348
# Pattrajit Chaiwut
# 651610338
# Lab07_1
# 229223 Sec 002

def main():
    corner_frame(4)

def corner_frame(n):
    l_n = list(range(1,n+1))

    result = list(map(lambda x : list(range(x,x+1)) * (x-1) + list(range(x , n+1)) , l_n)) # list ซ้อน list -> [[1,2,3,4] , [2,2,3,4] , [3,3,3,4] , [4,4,4,4]]
    result = "\n".join(map(lambda x: " ".join(map(str, x)), result))
    result = result + "\n"
    return result

if __name__ == '__main__':
    main()
