
a=int(input("ป้อนตัวเลข :"))
for row in range(a):
    for column in range(a):
        if (row+column)%2==0: # print("o",end="") if (row+column)%2==0 else print("o",end="")
            print("\tx",end="")
        else:
            print("\to",end="")
    print(" ")
