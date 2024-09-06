def main():
    test_from_hundredthousand_to_one()

def from_hundredthousand_to_one(number):
    if len(str(number)) < 2:
        return number
    else:
        total = 0
        for item in range(len(str(number))):
            total += int(str(number)[item])
        return from_hundredthousand_to_one(total) 
    
def test_from_hundredthousand_to_one():
    assert from_hundredthousand_to_one(12345) == 6
    assert from_hundredthousand_to_one(67896789678967896879678967896789678967896789678969) == 6
    assert from_hundredthousand_to_one(123456) == 3
    print("OK")

if __name__ == "__main__":
    main()