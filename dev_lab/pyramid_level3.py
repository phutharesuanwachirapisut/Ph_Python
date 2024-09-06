import copy
def main():
    test_pyramid_level3()

def pyramid_level3(number):
    a = ""
    
    list_a = []
    for item in range(1,number + 1):
        all_len = (2 * item) - 1
        a = (" " * (number - item)) + ("*" * all_len)
        list_a.append(a)
    list_b = copy.deepcopy(list_a)
    list_b = sorted(list_b,reverse=True)
    list_b = list_b[1:]
    result = list_a + list_b
    last_result = ""
    for j in result:
        last_result = last_result + j + "\n"
    return last_result
def test_pyramid_level3():
    assert pyramid_level3(4) == """   *
  ***
 *****
*******
 *****
  ***
   *
"""
    assert pyramid_level3(3) == """  *
 ***
*****
 ***
  *
"""
    print("ALL Coffee")

if __name__ == "__main__":
    main()