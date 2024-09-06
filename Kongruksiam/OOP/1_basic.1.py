# Name, Salary, Department
class Employee:                                 # Creating class , Let Employee is Class Name
                                                # First Digit of Class Name is Upperletter 

    # Creating Constructor
    def __init__(self):                         # Always output when Calling Object
        print("Default Constructor")

    # Creating Method
    def detail(self,name,salary,department):    # Important! variable is self by the way self is key word
        self.name = name                        # name will be collected in self
        self.salary = salary                    # salary will be collected in self
        self.department = department            # department will be collected in self
                                                # send self value that have name, salary and department to each variable

    def showdata(self):
        print(f"Employee Name = {self.name}")

        print("Salart = {}".format(self.salary))

        print("Department = {}".format(self.department))

# Creating Object
obj1 = Employee()

# Calling Method(function) have to start with object_name and follow by point and function in class
obj1.detail("Tom",15555,"Accounting")           # send value to detail function
obj1.showdata()

obj2 = Employee()
obj2.detail("Thomas",15557,"Manager")
obj2.showdata()

obj3 = Employee()
obj3.detail("Gosha",222222,"Head")
obj3.showdata()