# #!/usr/bin/env python3
# # ชื่อ (ไม่ต้องใส่นามสกุล)
# # รหัสนศ
# # Sec00x


# def main():
#     list_a = ['a', 'quick', 'brown', 'fox']
#     word_len(list_a)
#     assert list_a == [1, 5, 5, 3]

#     list_a = ['empty', 'or', '', 'full']
#     word_len(list_a)
#     assert list_a == [5, 2, 0, 4]

#     print("All tests passed!")


# def word_len(list_a):
#     result = list(map(lambda x: len(x) , list_a))
#     list_a[:] = result

# if __name__ == '__main__':
#     main()
def patterned_message(message, pattern):
    message = message.replace(" ",'')
    def helper(result, message_index, pattern_index):
        if pattern_index == len(pattern):
           return result

        char = pattern[pattern_index]

        if char.isspace():
           return helper(result + char, message_index, pattern_index + 1)

        message_char = message[message_index % len(message)]
        result += message_char

        return helper(result, message_index + 1, pattern_index + 1)

    pattern = pattern.strip()
    print(helper("", 0, 0)) 

print(patterned_message("D and C",'''*************** 
******   ******
***************
'''))
assert patterned_message("D and C",'''***************
******   ******
***************
''') == '''DandCDandCDandC 
DandCD   andCDa 
ndCDandCDandCDa
'''