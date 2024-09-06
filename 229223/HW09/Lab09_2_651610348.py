#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab09_2
# 229223 Sec 002

def main():
    sum_prime_in_range(3,20)

def sum_prime_in_range(x, y):
    prime_numbers = filter(boolean_is_prime, range(max(2, x), y + 1))
    return sum(prime_numbers)

def boolean_is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return boolean_is_prime(n, i + 1)

if __name__ == '__main__':
    main()