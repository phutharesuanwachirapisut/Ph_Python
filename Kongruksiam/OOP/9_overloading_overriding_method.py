"""
Overloading Method
    Method (หรือเรียกว่า function) ที่ชื่อเหมือนกัน อยู่ใน Class เดียวกัน
    แยกความต่างจาก parameter

Overriding Method
    Method (หรือเรียกว่า function) ที่ชื่อเหมือนกัน อยู่คนละ Class แแต่เป็น Class แม่ ลูกกัน
"""

class Employee:
    # class variable

    __minsalary = 12000             # can inheritance to
    maxsalary = 100000              # can inheritance to
    company = "บริษัท ความอดทนมี จำกัด" # can inheritance to

    def __init__(self, name, salary, department):
        # Instace Variable
        self.__name = name
        self.__salary = salary 
        self.__department = department 

    # Protected Method
    # แสดงผล
    def _showdata(self):
        print("Employee Name = " + self.__name)

        print("Salary = " + str(self.__salary))

        print("Department = " + self.__department)

    # คำนวณเงินเดือน
    def _getIncome(self):
        return self.__salary * 12
    
    def _getIncome(self,bonus=0):
        return self.__salary * 12 + bonus
    def __str__(self):
        return (f"Employe name = {self.__name} \nDepartment = {self.__department} \nSalary = {self.__salary} \nSalary per Y = {self._getIncome()} \n")

# Inheritanc คลาสลูก
class Accounting(Employee):
    __department = "Accounting"
    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__department)   # เรียกใช้ในคลาสแม่ โดยใช้ super
        self.age = age

    # OVerrinding Method
    def _showdata(self):
        # print("Employee Name = " + self.__name) หา self.__name ไม่เจอ

        # print("Salary = " + str(self.__salary))

        # print("Department = " + self.__department)
        super()._showdata()
        print(f"Age = {self.age}")

    def __str__(self):                                      # เอาไว้เพิ่มการแสดงค่านอกเหนือจากคลาสแม่ 
        return (super().__str__() + f"Age = {self.age}")


class Programmer(Employee):
    __department = "Developer"
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__department)
        self.exp = experience
        self.skill = skill

    # Overrinding
    def _showdata(self):
        super()._showdata()
        print(f"Experience = {self.exp}")
        print(f"Skill = {self.skill}")

    def __str__(self):
        return (super().__str__() + f"Experience = {self.exp} \nSkill = {self.skill}")
class Sale(Employee):
    __department = "Saler"
    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__department)
        self.area = area

    # Overriding
    def _showdata(self):
        super()._showdata()
        print(f"Area = {self.area}")

    def __str__(self):
        return (super().__str__() + f"Area = {self.area}")

# Output 
print("_________________________________________")

account = Accounting("Thomas", 52000,5)
print(account.__str__())
print("_________________________________________")

programmer = Programmer("Shell",122222, 10, 'Game Development')
print(programmer.__str__())
print("_________________________________________")

sale = Sale("Hella",500, 'Chiange Mai')
print(sale.__str__())
print("_________________________________________")

print(account._getIncome(bonus=500))