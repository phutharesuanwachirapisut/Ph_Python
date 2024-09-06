#1 
#12
#123

a=int(input("ป้อนตัวเลข :"))
for row in range(1,a+1):
    for column in range(1,row+1):
        print(column,end='')  
    print(" ")