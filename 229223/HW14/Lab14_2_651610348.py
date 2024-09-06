#!/usr/bin/env python3
# Phutharesuan Wachirapisut
# 651610348
# Lab14_2
# 229223 Sec 002

import copy

def remove_row_col(list_a, row, col):
    list_x = copy.deepcopy(list_a)
    # ลบ row 
    if row < len(list_a):
        list_x = list_x[:row] + list_x[row + 1:]
    else:
        return list_x
    for i in list_x: # ลบ col
        if col < len(i) and col >= 0:  # Check for valid column index
            list_x[list_x.index(i)] = i[:col] + i[col + 1:]
        else:
            return list_x
    return list_x

def main():
    with open(filename, 'r') as file:
        lines = file.readlines()
    # filename = [line.strip('\n') for line in filename]
    filename = [line.split('\n') for line in filename]
    for line_index in range(0, len(filename), 3):
        list_a = filename[line_index]
        row = int(filename[line_index + 1])
        col = int(filename[line_index + 2])

        removed_list = remove_row_col(list_a, row, col)

        print(removed_list)
    # try:
    #     with open(filename, mode, encoding='utf-8') as readfile:
    #         file_content = readfile.readlines()

    #         file_content = [line.strip('\n') for line in file_content]

    #         for line_index in range(0, len(file_content), 3):
    #             list_a = file_content[line_index]
    #             row = int(file_content[line_index + 1])
    #             col = int(file_content[line_index + 2])

    #             removed_list = remove_row_col(list_a, row, col)

    #             print(removed_list)
    # except FileNotFoundError:
    #     return None
if __name__ == '__main__':
    main()

