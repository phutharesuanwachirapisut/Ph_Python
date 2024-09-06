
def main():
    test_scaled_matrix()
def scaled_matrix(m, n, matrix_list):
    max_scale = max(matrix_list)
    min_scale = min(matrix_list)
    if max_scale >= 0 and min_scale <= 0:
        list_a = list(map(lambda x: "{:0.4f}".format((x + abs(min_scale)) / (abs(max_scale) + abs(min_scale))) , matrix_list))
    else:
        list_a = list(map(lambda x: "{:0.4f}".format(x / (max_scale + min_scale))))

    result = ""
    
    a = 0
    for row in range(0, n):
        for column in range(0, m):
            result = result + list_a[a] + " "
            a += 1
        result += "\n"
    
    return result

def test_scaled_matrix():
    assert scaled_matrix(2, 6,[-4605.16, # (-4605.16 + 9559.76) / (9198.68 + 9559.76) = 0.2641
4768.87,
-494.21,
6548.12,
9198.68,
-5335.41,
-7206.89,
-9559.76,
-731.66,
2229.36,
-8204.81,
1053.96]) == """0.2641 0.7638 
0.4833 0.8587 
1.0000 0.2252 
0.1254 0.0000 
0.4706 0.6285 
0.0722 0.5658 
"""
    print("K lei")

if __name__ == "__main__":
    main()