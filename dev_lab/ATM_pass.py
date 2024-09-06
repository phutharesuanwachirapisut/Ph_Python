import string

def main():
    # sentence = input()
    test_ATM_pass()

def ATM_pass(sentence):
    list_a = []
    indy = 0
    while indy <= len(sentence) - 1:
        test_ = str()
        d = sentence[indy]
        if sentence[indy] in string.digits:
            test_ = sentence[indy]
            indy += 1  
            if indy == len(sentence):
                list_a.append(test_) 
            else:
                while sentence[indy] in string.digits:
                    d = sentence[indy]
                    test_ += sentence[indy]
                    indy += 1
                list_a.append(test_)                        

        else:
            indy += 1
    result = list(map(lambda x: int(x) , list_a))
    result = sum(result)
    if len(str(result)) < 4:
        result = str(result).zfill(4)
    else:
        result = str(result)
    return result
def test_ATM_pass():
    assert ATM_pass('HE45L32LO458T6H359ISIS1BO589RNT34ODEVN80AJA') == '1604'
    assert ATM_pass('NPoeJ43OP-*!@#8805j3n62df0') == '8913'
    assert ATM_pass('a1b2c3d4e5f6g7h8i9') == '0045'
    print("OK")
if __name__ == "__main__":
    main()