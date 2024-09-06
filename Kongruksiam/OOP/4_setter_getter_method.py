
"""
จุดประสงค์หลัก คือ เพื่อเรียกใช้ Private Attribute

Setter: # กำหนดค่าให้ Object
    def setName(self,newName):
        self.__name = newName

Getter: # ดึงค่าให้ Object
    def getName(self):
        return self.__name

จาก EP.03 เราจะเรียกใช้ Private Attribute เมื่ออยู่ใน class เท่านั้น 
ดังนั้น EP.04 นี้ เราจะสร้าง Function เพื่อให้สามารถเรียก Private Attribute ได้
"""

class Employee:

    def __init__(self,name,salary,department):
        # Private Attribute
        self.__name = name
        self.__salary = salary 
        self.__department = department 


    # Protected Method
    def _showdata(self):
        print("Employee Name = {}".format(self.getname()))

        print("Salary = {}".format(self.getsalary()))

        print("Department = {}".format(self.getdepartment()))
    
    # Setter Method
    def setname(self,newname):
        self.__name = newname               # set new value in Private Attribute

    def setsalary(self,newsalary):
        self.__salary = newsalary
    
    def setdepartment(self,newdepartment):
        self.__department = newdepartment
    
    # Getter Method 
    def getname(self):                      # Use this solution because we use private attribute so we can not output in directly
        return self.__name
    def getsalary(self):
        return self.__salary
    def getdepartment(self):
        return self.__department
    
obj1 = Employee("Tom",15555,"Accounting")

obj1.setname("Arthor")

# obj1.__salary = 70000 # not work
# obj1.setsalary(78888)

# obj1.__department = "Boss" # not work
# obj1.setdepartment("Manager")
print(obj1._showdata())
