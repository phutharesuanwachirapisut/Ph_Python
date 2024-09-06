i=1
j=1
while i<=3:
    print("รอบที่ ",i)
    j=1
    while j<=5:
        print("รอบที่ ",i,"ตำแหน่งที่ ", j)
        j+=1
    i+=1
print("End")

for i in range(1,5,2):
    print("รอบที่ " ,i)
    for j in range(1,-2,-1):
        print(j)