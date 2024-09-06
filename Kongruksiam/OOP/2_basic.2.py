# Name, Salary, Department
class Employee:                                 # Creating class , Let Employee is Class Name
                                                # First Digit of Class Name is Upperletter 
    def __init__(self):
        print("Default Constructor")

    # Mixed Constructor Methodand 
    def __init__(self,name,salary,department):  # Always output when Calling Object
        self.name = name                        # name will be collected in self
        self.salary = int(salary)               # salary will be collected in self
        self.department = department            # department will be collected in self     
 
    def showdata(self):
        print("Employee Name = {}".format(self.name))

        print("Salart = {}".format(self.salary))

        print("Department = {}".format(self.department))
    
    def __del__(self):
        print("Call Destructor")

# Creating Object
obj1 = Employee("Tom",15555,"Accounting")       # Calling Default Constructor
                                                # Calling Method(function) have to start with object_name and follow by point and function in class

# Changing Value salary
obj1.salary = 70000 
obj1.showdata()

obj2 = Employee("Thomas",15557,"Manager")
obj2.showdata()

obj3 = Employee("Gosha",222222,"Head")
obj3.showdata()

print(isinstance(obj1,Employee))
print(dir(obj1)) # Show prompt that you can use in this object
print(obj1.__class__) # Show class name of obj1