# super หมายถึงคลาสแม่ เป็นการเรียกใช้ในคลาสแม่
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
    def _showdata(self):
        print("Employee Name = " + self.__name)

        print("Salary = " + str(self.__salary))

        print("Department = " + self.__department)

# Inheritanc คลาสลูก
class Accounting(Employee):
    __department = "Accounting"
    def __init__(self,name,salary):
        super().__init__(name, salary, self.__department) # เรียกใช้ในคลาสแม่ โดยใช้ super
class Programmer(Employee):
    __department = "Developer"
    def __init__(self,name,salary):
        super().__init__(name, salary, self.__department)
        super()._showdata()
class Sale(Employee):
    __department = "Saler"
    def __init__(self,name,salary):
        super().__init__(name, salary, self.__department)
        super()._showdata()
        

account = Accounting("Thomas", 52000)
programmer = Programmer("Shell",122222)
sale = Sale("Hell",5)