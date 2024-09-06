a=int(input("ป้อนตัวเลข :"))
for row in range(a):
    for column in range(a):
        if row==0 or row==a-1 or column==0 or column==a-1:
            print("x",end="")
        else:
            print(" ",end="")
    print(" ")

