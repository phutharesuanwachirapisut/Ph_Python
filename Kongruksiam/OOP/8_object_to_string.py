# แปลง Object เป็น string
    # def __str__(self):
    #     return "ชุดข้อความ"

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
    
    def __str__(self):
        return (f"Employe name = {self.__name} \n Department = {self.__department} \n Salary = {self.__salary} \n Salary per Y = {self._getIncome()}")

# Inheritanc คลาสลูก
class Accounting(Employee):
    __department = "Accounting"
    def __init__(self,name,salary):
        super().__init__(name, salary, self.__department) # เรียกใช้ในคลาสแม่ โดยใช้ super
class Programmer(Employee):
    __department = "Developer"
    def __init__(self,name,salary):
        super().__init__(name, salary, self.__department)
class Sale(Employee):
    __department = "Saler"
    def __init__(self,name,salary):
        super().__init__(name, salary, self.__department)
        
# Output 

account = Accounting("Thomas", 52000)
print(f"รายได้ต่อปีของนักบัญชี = {account._getIncome()}")
print(account.__str__())
print("_________________________________________")

programmer = Programmer("Shell",122222)
print(f"รายได้ต่อปีของนักเขียนโปรแกรม = {programmer._getIncome()}")
print(programmer.__str__())
print("_________________________________________")

sale = Sale("Hella",500)
print(f"รายได้ต่อปีของพนักงานขาย = {sale._getIncome()}")
print(sale.__str__())
print("_________________________________________")

