#!/usr/bin/env python3
# Phutharesuan_Wachirapisut
# 651610348
# HW06_1
# 229223 Sec 002

def main():

    print(decode("aceiklmr-", '''
3 .
5 3 4 2 .
3 1 2 8 1 7 2 0 86 .
'''))
# "aceiklmr-" คือ code_table
# 3 1 2 8 1 7 2 0 86 . คือ str_index

def decode_helper(code_table, str_index):  # รับรหัส 1 ตัว แล้วคืน 1 อักขระที่ถูกต้อง
    if str_index == ".":
        return "\n"
    elif abs(int(str_index)) < len(code_table): # 
        return code_table[abs(int(str_index))]
    else: 
        return "_"

def decode(code_table, text):
    # แยกรหัสทั้งหมด ให้กลายเป็น list เช่น ['3', '.', '5', '3', '4', '2', '.', ...]
    l_text = text.split()

    # เรียกใช้ฟังก์ชัน decode_helper() ที่มีหน้าที่รับรหัสหนึ่งตัว แล้วคืน 1 อักขระที่ถูกต้อง
    result_list = list(map(lambda x: decode_helper(code_table, x), l_text))

    # รวม list ของอักขระ ให้เป็น string
    result = "".join(result_list)
    return result


if __name__ == '__main__':
    main()
