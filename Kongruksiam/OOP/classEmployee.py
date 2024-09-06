
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
