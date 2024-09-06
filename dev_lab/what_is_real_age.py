
def main():
    # list_a = []
    # for item in range(1,4):
    #     myinput = int(input())
    #     list_a.append(myinput)
    test_what_is_real_age()

def what_is_real_age(list_a):
    n = list_a[0]
    m = list_a[1]
    y = list_a[2]
    b = ((-y)*(m-1) - n)/(1-m)
    a = n + b
    return a,b

def test_what_is_real_age():
    assert what_is_real_age([1,2,3]) == (5,4) 
    assert what_is_real_age([6,2,8]) == (20,14) 
    assert what_is_real_age([2,3,9]) == (12,10)
    print("Lers")

if __name__ == "__main__":
    main()