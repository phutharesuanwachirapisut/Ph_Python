# Inheritance (การสืบทอดคุณสมบัติ) -> นำสิ่งที่มีอยู่แล้ว นำมาใช้8
class Employee:
    # class variable
    __minsalary = 12000 # can inheritance to
    maxsalary = 100000 # can inheritance to
    company = "บริษัท ความอดทนมี จำกัด" # can inheritance to
    def __init__(self,name,salary,department):
        # Instace Variable
        self.__name = name
        self.__salary = salary 
        self.__department = department 

    # Protected Method
    def _showdata(self):
        print("Employee Name = {}".format(self.__name))

        print("Salary = {}".format(self.__salary))

        print("Department = {}".format(self.__department))

# Inheritanc
class Accounting(Employee):
    __department_name = "Accounting"
    def __init__(self):
        pass

class Programmer(Employee):
    __department_name = "Developer"
    def __init__(self):
        pass

class Sale(Employee):
    __department_name = "Saler"
    def __init__(self):
        pass

account = Accounting()
print(account.company)              # เป็นตัวอย่างที่ชัดเจนในการแสดงการสิบทอดคุณสบัติ นั่นคือ การเรียกใช้ class account แต่เรียก company ซึ่ง อยู่ใน class Employee 
                                    # แต่ class account เป็นคลาสลูกของ
programmer = Programmer()
print(account._Employee__minsalary) # ถ้าเป็น Private ต้องผ่านแม่ก่อน (Employee)
sale = Sale()
print(account.maxsalary)