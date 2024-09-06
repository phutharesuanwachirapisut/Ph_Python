#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# HW10_2
# 229223 Sec 002

def main():
    result = eratosthenes(20,True)
    print('OK')
    print(result)

def eratosthenes(n, show_step=False):
    result = list(range(2, n + 1))
    primes = []
    for num in result:
        primes.append(num)
        
        before_filtering_length = len(result)
        result = list(filter(lambda x: x % num != 0 or x / num == 1, result))
        after_filtering_length = len(result)

        if before_filtering_length != after_filtering_length:
            if show_step:
                print(f"{num}: {result}")
    return result

if __name__ == '__main__':
    main()