
class Employee:
    # class variable
    _minsalary = 12000
    _maxsalary = 100000
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
    
obj1 = Employee("Tom",15555,"Accounting")
print(Employee._minsalary)
