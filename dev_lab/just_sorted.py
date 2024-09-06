import copy
def main():
    list_a = []
    for i in range(5):
        input_ = input()
        list_a.append(input_)
    just_sorted(list_a)

def just_sorted(list_a):
    list_a = map(lambda x: int(x), list_a)
    list_b = copy.deepcopy(list_a) 
    list_b = sorted(list_a , reverse = True)
    for j in list_b:
        print(j)

if __name__ == "__main__":
    main()