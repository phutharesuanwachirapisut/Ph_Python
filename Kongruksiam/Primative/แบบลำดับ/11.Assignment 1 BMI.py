#BMI = Weight (kg) / (Hight (m) * Hight (m))
Hight=int(input("Hight (cm) : "))#Hight=int(input("Hight (cm) : "))/100
Weight=int(input("Weight (kg) : "))

Hight/=100

BMI=Weight/ (Hight**2)

print("BMI = ",BMI)#print("BMI = ",Weight/ (Hight**2))