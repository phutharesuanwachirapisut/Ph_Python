def main():
    my_input = int(input())
    factorial(my_input)

def factorial(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1
    print(result)
if __name__ == "__main__":
    main()