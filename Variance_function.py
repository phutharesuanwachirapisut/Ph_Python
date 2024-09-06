
def main():
    list_age = list(range(20,34))
    list_px = [0.02 , 0.04 , 0.05 , 0.07 , 0.04 , 0.02 , 0.07 , 0.02 , 0.11 , 0.07 , 0.09 , 0.13 , 0.15 , 0.12]
    variance = list(map(lambda x, y: ((x - 27.87)**2)*y , list_age , list_px))
    result = sum(variance)
    print(result)

if __name__ == '__main__':
    main()