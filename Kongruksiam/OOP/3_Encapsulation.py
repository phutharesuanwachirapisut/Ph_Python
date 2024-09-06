
"""
Encapsulation (การห่อหุ้ม):
    1. ซ่อนรายละเอียดการทำงานไม่ให้ภายนอกเห็น
    2. ภายนอกแก้ไขไม่ได้
    3. ปลอดภัยแก่ผู้ให้ข้อมูล

Access Modifier(ระดับการเข้าถึงข้อมูล):
    1. Public = เรียกใช้ได้ทั้งในและนอก class
    2. Protected = เรียกใช้ได้ใน class แม่ และ class ลูก
                have one underscore (_) in attribute
    3. Private = เรียกใช้ได้แค่ใน class เท่านั้น
                have two underscore (__) in attribute

"""

class Employee:

    def __init__(self,name,salary,department):  # Always output when Calling Object
        # Public Attribute
        self.name = name                        # name will be collected in self
        # Protected Attribute
        self._salary = salary                   # salary will be collected in self
        # Private Attribute
        self.__department = department          # department will be collected in self     
        self.__showdata()

    # Public Method
    # def showdata(self):

    # Protected Method
    # def _showdata(self):

    # Private Method
    def __showdata(self):
        print("Employee Name = {}".format(self.name))

        print("Salary = {}".format(self._salary))

        print("Department = {}".format(self.__department))

obj1 = Employee("Tom",15555,"Accounting")
obj1._salary = 70000
obj1.__department = "Boss"                      # แก้ไขไม่ได้ จะไม่ output เป็น Boss

# obj1._showdata()
# obj1.__showdata()                             # will not find so we have to call in class (line25)