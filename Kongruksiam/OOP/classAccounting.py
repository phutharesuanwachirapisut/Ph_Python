from classEmployee import Employee

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
