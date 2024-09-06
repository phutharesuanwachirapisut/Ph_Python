#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab11_2
# 229223 Sec 002

import sys

def main():
    treasures = read_input()

    assert total_value('Gold', treasures) == 1090
    assert total_value('Ruby', treasures) == -1

def read_input():

    treasures = {}
    for line in sys.stdin:
        if line.strip() == "" or line.startswith("#"):
            continue

        data = [value.strip() for value in line.split(",")]

        location, treasure_type, value_str = data
        
        try:
            value = int(value_str)
        except ValueError:
            raise ValueError(f"Invalid value: {value_str}")

        if treasure_type not in treasures:
            treasures[treasure_type] = [(location, value)]
        else:
            treasures[treasure_type].append((location, value))

    return treasures


def total_value(treasure_type, treasures):
    total = 0
    if treasure_type in treasures:
        for value, quantity in treasures[treasure_type]:
            total += quantity
    else:
        total = -1
    return total

if __name__ == '__main__':
    main()

